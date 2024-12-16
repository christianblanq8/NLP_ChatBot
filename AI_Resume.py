from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from langchain.document_loaders.pdf import PyPDFDirectoryLoader

llm = OllamaLLM(model="vicuna", temperature=0)

prompt = PromptTemplate(
    input_variables=["content", "question"],
    template="""
You are an expert summarizer and analyzer. Given the following webpage content:

{content}

Answer the user's question below:

Question: {question}

Answer:
"""
)

def load_documents():
    file_path =  '...'
    document_loader  = PyPDFDirectoryLoader(file_path)
    return document_loader.load()

documents = load_documents()



chain = RunnableSequence(prompt | llm)

def analyze_link(question):
    content = documents[0]
    if "Error" in content:
        return content
    return chain.invoke({"content": content, "question": question})


if __name__ == "__main__":
    user_gateway = input("Enter 1 to access bot! Enter 0 to exit: ")

    while user_gateway == "1":
        question = input('Enter a question: ')
        print("Answer:", analyze_link(question))
        user_gateway = input("Enter 1 to continue! Enter 0 to exit: ")
    
    if user_gateway == "0":
        print("Goodbye")






