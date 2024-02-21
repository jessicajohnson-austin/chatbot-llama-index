import os
import streamlit as st
from llama_index.core import ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv
import openai
load_dotenv()
openai.api_key =os.getenv("OPENAI_API_KEY")


with st.sidebar:
    st.title("🤗💬 Chat with our API")
    st.markdown('''
  
                ''')
def main():
    st.header("Chat with our API")
    reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4-0125-preview", temperature=0.6, system_prompt="You are an expert on the API and your job is to answer technical questions."))
    index  = VectorStoreIndex.from_documents(docs, service_context=service_context)
    query=st.text_input("Ask questions related to the API")
    if query:
        chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
        response = chat_engine.chat(query)
        st.write(response.response)
if __name__=='__main__':
    main()    
ServiceContext.from_defaults(llm=OpenAI(model="gpt-4-0125-preview", temperature=0.6, system_prompt="You are an expert on the API"))