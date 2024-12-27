# Module to run/implements core functionality for RAG_SERVICE

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
class RAGService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None
        self.prompt_template = PromptTemplate(
            template="""
                Human: You are an AI assistant. Answer questions using the information provided. 
                Where appropriate, include relevant URLs in your response if necessary.
                <context>
                {context}
                </context>
                <question>
                {question}
                </question>
                Assistant:""",
            input_variables=["context", "question"]
        )
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    def prepare_data(self, web_paths):
        loader = WebBaseLoader(web_paths)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(documents)

        # Print the first few document contents to verify
        for doc in split_docs[:5]:  # Print the first 5 documents
            print(f"Document: {doc.page_content[:200]}...")  # Print the first 200 characters

        return split_docs


    def initialize_vectorstore(self, docs, uri="./milvus_demo.db"):
        self.vectorstore = Milvus.from_documents(
            documents=docs,
            embedding=self.embeddings,
            connection_args={"uri": uri},
            drop_old=True,
        )

    def query_rag(self, question):
        retriever = self.vectorstore.as_retriever()
        rag_chain = {
                        "context": retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)),
                        "question": RunnablePassthrough()
                    } | self.prompt_template | self.llm | StrOutputParser()
        return rag_chain.invoke(question)




