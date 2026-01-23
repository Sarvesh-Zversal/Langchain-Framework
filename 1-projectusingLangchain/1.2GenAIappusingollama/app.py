import os 
from  dotenv import load_dotenv
load_dotenv()

from langchain_community.llms.ollama import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


## for langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_NAME"] = "LangchainFramework"


#### designing prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please respond the question asked ."),
        ("user","Question: {question}")
    ]
)

## streamlit framework
st.title("GenAI App using Ollama and Langchain")
question=st.text_input("Enter your question here")


## llm model initialization
llm=Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if question:
    response=chain.invoke({"question":question})
    st.write("Answer:",response)
