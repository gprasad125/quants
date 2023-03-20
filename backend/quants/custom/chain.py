from langchain.chains import VectorDBQAWithSourcesChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from typing import Any, Dict, List, Tuple

from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.chains.qa_with_sources.map_reduce_prompt import (
    COMBINE_PROMPT,
    EXAMPLE_PROMPT,
    QUESTION_PROMPT,
)
from langchain.docstore.document import Document
from langchain.llms.base import BaseLLM
from langchain.prompts.base import BasePromptTemplate

class CustomMapReduceChain(MapReduceDocumentsChain):
        """Combining documents by mapping a chain over them, then combining results."""
        
        def _process_results(
            self,
            results: List[Dict],
            docs,
            token_max: int = 3000,
            **kwargs: Any,
        ) -> Tuple[str, dict]:
            
            # overriding _process_results() in MapReduceDocumentsChain in main method to return result_docs
            question_result_key = self.llm_chain.output_key
            result_docs = [
                Document(page_content=r[question_result_key], metadata=docs[i].metadata)
                # This uses metadata from the docs, and the textual results from `results`
                for i, r in enumerate(results)
            ]
            length_func = self.combine_document_chain.prompt_length
            num_tokens = length_func(result_docs, **kwargs)
            while num_tokens is not None and num_tokens > token_max:
                new_result_doc_list = _split_list_of_docs(
                    result_docs, length_func, token_max, **kwargs
                )
                result_docs = []
                for docs in new_result_doc_list:
                    new_doc = _collapse_docs(
                        docs, self._collapse_chain.combine_docs, **kwargs
                    )
                    result_docs.append(new_doc)
                num_tokens = self.combine_document_chain.prompt_length(
                    result_docs, **kwargs
                )
            if self.return_intermediate_steps:
                _results = [r[self.llm_chain.output_key] for r in results]
                extra_return_dict = {"intermediate_steps": _results}
            else:
                extra_return_dict = {}
            output, _ = self.combine_document_chain.combine_docs(result_docs, **kwargs)

            return output, extra_return_dict, result_docs
        
class CustomChain(VectorDBQAWithSourcesChain):
    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        document_prompt: BasePromptTemplate = EXAMPLE_PROMPT,
        question_prompt: BasePromptTemplate = QUESTION_PROMPT,
        combine_prompt: BasePromptTemplate = COMBINE_PROMPT,
        **kwargs: Any,
    ):
        """Construct the chain from an LLM."""
        llm_question_chain = LLMChain(llm=llm, prompt=question_prompt)
        llm_combine_chain = LLMChain(llm=llm, prompt=combine_prompt)
        combine_results_chain = StuffDocumentsChain(
            llm_chain=llm_combine_chain,
            document_prompt=document_prompt,
            document_variable_name="summaries",
        )
        combine_document_chain = CustomMapReduceChain(
            llm_chain=llm_question_chain,
            combine_document_chain=combine_results_chain,
            document_variable_name="context",
        )
        return cls(
            combine_documents_chain=combine_document_chain,
            **kwargs,
        )

    @property
    def output_keys(self) -> List[str]:
        """Return output key.
        :meta private:
        """
        return [self.answer_key, self.sources_answer_key, 'docs', 'result_docs']
    
    def _call(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        docs = self._get_docs(inputs)
        # print(docs[0])
        answer, _, result_docs = self.combine_documents_chain.combine_docs(docs, **inputs)
        if "SOURCES:" in answer:
            answer, sources = answer.split("SOURCES:")
        else:
            sources = ""
        return {self.answer_key: answer, self.sources_answer_key: sources, 'docs': docs, 'result_docs': result_docs}
    

