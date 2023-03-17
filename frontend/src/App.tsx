import { useState, useEffect, useRef } from 'react';
import { API_URL, DEV_URL, FILE_URL, DOCS_URL} from './settings';
import './App.css';

type Result = {
    answer: string,
    sources: string,
    question: string
};

function App() {
    const [question, setQuestion] = useState('');
    const [result, setResult] = useState<Result | null>(null);
    const [loading, setLoading] = useState(false);
    const questionRef = useRef(question);
    questionRef.current = question;
    const submitRef = useRef(() => {});

    const [file, setFile] = useState<File | undefined>();

    function postFile(file: File) {
      
        const formData = new FormData();
        formData.append('file', file);
      
        fetch(FILE_URL, {
          method: 'POST',
          body: formData,
        })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then(data => {
            console.log('Upload successful:', data);
          })
          .catch(error => {
            console.error('Error uploading file:', error);
          });
      }


    function createFile(evt: React.ChangeEvent<HTMLInputElement>) {
        const file = evt.target.files?.[0];
        if (file) {
          setFile(file);
          postFile(file);
        }
    }

    function ingest(){

        fetch(DOCS_URL,
            {method: 'POST'}
        ).then(response =>
            {
                if (!response.ok){
                    throw new Error('Ingestion failed...');
                }
                return response.json();
            }).then( data => {console.log('Ingestion passed!')})
            .catch(error => {console.log('Error: ', error)})

    }

    function uploadData(input: string){

        if (input.length <= 5) {
            alert('Question must be > 5 characters in length!')
            return;
        }

        setResult(null);
        setLoading(true);

        const data = new FormData();
        data.append("text", input);

        fetch(DEV_URL, {
            method: "POST",
            body: data
        }).then(res => {
            if (!res.ok){
                throw new Error(`HTTP error! Status: ${res.status}`);
            }
            return res.json();
        }).then(data => {
            const json = JSON.parse(data as string)
            setQuestion('');
            setResult(json as Result);
            setLoading(false);
        }).catch(error => {
            console.log(error);
        })
    };    

    let answerFragments: string[] = [];
    let sourceFragments: string[] = [];

    if (result) {
        answerFragments = result.answer.split('\n');
        sourceFragments = result.sources.split(',');
    }

    const answerJSX = answerFragments.map(frag => (
        <p className="mb-1">{frag}</p>
    ));
    const sourceJSX = sourceFragments.map(frag => (
        <li className="mb-3 list-decimal">
            <p>{frag}</p>
        </li> 
    ));

    return (
        <div className="container mx-auto max-w-3xl px-5 md:mt-36 mt-20">
            { loading ?
                <div>
                    <div className="flex flex-row justify-center mb-3">
                        <div role="status">
                            <svg aria-hidden="true" className="w-12 h-12 mr-2 text-gray-200 animate-spin dark:text-gray-400 fill-black" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                            </svg>
                            <span className="sr-only">Loading...</span>
                        </div>
                    </div>
                    <p className="block text-center text-3xl text-slate-600 mb-3">Processing...</p>
                    <p className="block text-center text-base text-slate-600">This can take up to a minute</p>
                </div>
                :
                <>
                    <label className="text-2xl text-slate-700 font-bold block mb-3">
                        Ask a Frontend Question
                    </label>
                    <input 
                        type="text"
                        className="w-full rounded px-5 py-3 mb-5" 
                        placeholder="What is JSON?"
                        value={question}
                        onChange={e => setQuestion(e.target.value)}
                    />
                    <button
                        className="px-10 py-2 bg-slate-500 hover:bg-slate-400 text-white rounded"
                        onClick={() => uploadData(question)}
                    >
                        Ask!
                    </button>  

                    <button
                        className="m-2 px-4 py-2 bg-slate-500 hover:bg-slate-400 text-white rounded"
                        onClick={() => ingest()}
                    >
                        Ingest Files
                    </button>

                    <input type = 'file' accept = '.md' className='px-10 py-2' multiple onChange={(evt) => createFile(evt)}></input>

                    {/* <input id="fileSelector" type="file" accept=".mp4,.mp3,.m4a,.mov"  className='px-10 py-2 bg-slate-500 hover:bg-slate-400 text-white rounded'></input> */}

                </>
            }
            { result ?
                <article className="mt-20 mb-10">
                    <h1 className="text-2xl font-bold mb-3">{result?.question}</h1>
                    <div className="mb-8">
                        {answerJSX}
                    </div>
                    <h2 className="text-2xl font-bold mb-3">Sources</h2>
                    <ol>
                        {sourceJSX}
                    </ol>
                </article>
                : null
            }
        </div>
    );
}

export default App;
