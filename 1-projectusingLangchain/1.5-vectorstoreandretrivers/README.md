# Vector Store and Retrievers with LangChain

## Overview

This notebook demonstrates how to work with **LangChain's vector stores and retrievers** for implementing **Retrieval-Augmented Generation (RAG)** pipelines. These abstractions are essential for building applications that fetch and reason over external data using Large Language Models.

## Key Concepts Covered

### 1. **Documents**
- Core abstractions for handling data in RAG pipelines
- Used for data retrieval and processing workflows
- Each document contains:
  - `page_content`: The actual text content
  - `metadata`: Additional information like source, page number, etc.

### 2. **Vector Stores**
- Databases that store document embeddings
- Enable semantic search through similarity matching
- Used in this notebook: **FAISS** (Facebook AI Similarity Search)
- Implemented with **HuggingFace embeddings** (all-MiniLM-L6-v2 model)

### 3. **Retrievers**
- Interfaces that return documents given an unstructured query
- More general than vector stores - they only retrieve, not necessarily store
- Accept string queries and return Document objects
- In LangChain, retrievers are **Runnables** - compatible with LCEL chains

### 4. **RAG (Retrieval-Augmented Generation)**
- Combines LLMs with external knowledge sources
- Retrieves relevant documents based on user query
- Uses those documents as context for the LLM to answer questions

## Prerequisites

### Required Libraries
```bash
pip install langchain langchain-groq langchain-huggingface langchain-community python-dotenv
pip install -U langchain-chroma
```

### Environment Variables
Create a `.env` file with:
```
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT_NAME=LangchainFramework
```

## Notebook Structure

### Section 1: Document Creation
Creates sample documents about LangChain and dogs with metadata.

### Section 2: Configuration
- Loads environment variables
- Configures GROQ LLM with `meta-llama/llama-4-scout-17b-16e-instruct`
- Sets up LangSmith tracing for monitoring

### Section 3: Embedding Model Setup
- Loads HuggingFace embedding model (`all-MiniLM-L6-v2`)
- Used to convert text into vector embeddings

### Section 4: Vector Store Creation
- Creates FAISS vector store from documents
- Enables semantic similarity search

### Section 5: Similarity Search Examples
- Simple queries: `vectorstore.similarity_search()`
- Async queries: `await vectorstore.asimilarity_search()`
- Search with scores: `vectorstore.similarity_search_with_score()`

### Section 6: Retriever Implementation
Two approaches demonstrated:

**Approach 1: RunnableLambda (Advanced)**
```python
retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)
```
- Converts any function into a LCEL-compatible Runnable
- Useful for custom retrieval logic

**Approach 2: as_retriever() (Standard)**
```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}
)
```
- Built-in method on vector stores
- Cleaner and more standard approach

### Section 7: RAG Chain Setup
Creates a complete RAG chain:
1. **Input**: Dictionary with a question
2. **Retrieval**: Uses the retriever to fetch relevant documents
3. **Prompt**: Formats question and context into a prompt
4. **LLM**: Generates answer based on retrieved context

## Important Fix Applied

The original RAG chain had an issue where the retriever wasn't being called with the question. The fixed version uses:

```python
rag_chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question")
    } 
    | prompt 
    | llm
)
```

**Key changes:**
- Uses `itemgetter` to extract the question from input
- Passes the question to the retriever to fetch relevant documents
- Both context and question are provided to the prompt template

## Usage Example

```python
response = rag_chain.invoke({"question": "tell me about dogs"})
print(response.content)
```

The chain will:
1. Extract the question: "tell me about dogs"
2. Search the vectorstore for similar documents
3. Retrieve the most relevant document about dogs
4. Pass it as context to the LLM
5. Return an answer based on the retrieved context

## Expected Output

For the query "tell me about dogs", the LLM will reference the dog-related documents in the vectorstore and provide an informed answer about dogs' characteristics, breeds, and care requirements.

## Customization Options

### Change Retrieval Strategy
```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # Retrieve top 3 documents
)
```

### Modify the System Prompt
Edit the `message` variable to change how the LLM interprets the context and answers questions.

### Use Different Embeddings
Replace the HuggingFace embeddings with other providers:
- OpenAI embeddings
- Cohere embeddings
- Ollama embeddings

## Troubleshooting

**Q: No answer about dogs?**
- Ensure documents about dogs are in the vectorstore
- Check that the retriever is properly configured
- Verify the RAG chain syntax is correct

**Q: Wrong documents retrieved?**
- Adjust the `k` parameter to retrieve more documents
- Consider changing the embedding model
- Modify the similarity search type

**Q: Connection errors?**
- Verify API keys in `.env` file
- Check internet connection for GROQ API
- Ensure HuggingFace token is valid

## References

- [LangChain Documentation](https://python.langchain.com/)
- [RAG Explained](https://python.langchain.com/docs/use_cases/question_answering/)
- [FAISS Vector Store](https://python.langchain.com/docs/integrations/vectorstores/faiss/)
- [Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/)

## Author Notes

This notebook demonstrates the complete workflow for building RAG applications with LangChain:
- ✅ Document management
- ✅ Vector embeddings and storage
- ✅ Semantic retrieval
- ✅ Integration with LLMs
- ✅ Full LCEL chain implementation

The RAG pattern is fundamental for building production-grade LLM applications that can leverage external knowledge sources.
