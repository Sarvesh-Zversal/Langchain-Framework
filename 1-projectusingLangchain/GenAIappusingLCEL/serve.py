from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes

from dotenv import load_dotenv
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(api_key=groq_api_key, model="llama-3.3-70b-versatile", temperature=0.7)



## Create prompt using ChatPromptTemplate
template = "Translate the following into: {language}."
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("user", "{text}")
    ]
)
parser = StrOutputParser()  


## chain the components together
chain = model|parser

## app route for prediction

app = FastAPI(title="LangServe GenAI API",
              description="An API to demonstrate LangServe with LangChain and Groq LLM",
              version="1.0.0")

add_routes(app, chain, path="/chain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
