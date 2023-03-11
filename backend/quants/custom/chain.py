from langchain.chains import VectorDBQAWithSourcesChain
from typing import Any, Dict, List

class CustomChain(VectorDBQAWithSourcesChain):

    @property
    def output_keys(self) -> List[str]:
        """Return output key.
        :meta private:
        """
        return [self.answer_key, self.sources_answer_key, 'docs']
    
    def _call(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        docs = self._get_docs(inputs)
        # print(docs[0])
        answer, _ = self.combine_documents_chain.combine_docs(docs, **inputs)
        if "SOURCES:" in answer:
            answer, sources = answer.split("SOURCES:")
        else:
            sources = ""
        return {self.answer_key: answer, self.sources_answer_key: sources, 'docs': docs}