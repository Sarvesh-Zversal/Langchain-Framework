# LangChain Framework

A comprehensive framework for building and learning Generative AI applications using LangChain. This project covers the complete pipeline from data ingestion to vector database storage with practical examples and implementations.

## Project Structure

### 1. Project Using LangChain (`1-projectusingLangchain/`)
- **gettingStarted.ipynb** - Introduction to LangChain basics and setup
- **simplegenaiapp.ipynb** - A simple GenAI application demonstrating core LangChain concepts
- **converted_project/** - JavaScript/Node.js version of the LangChain project

### 2. Data Ingestion (`2-dataingestion/`)
- **documentsloader.ipynb** - Learn how to load documents from various sources
- Document loading strategies and best practices

### 3. Data Transformation (`3-Data-transformation/`)
- **textsplitters.ipynb** - Text splitting techniques for chunking documents
- **202507010000PROQUESTJOURNALS_3283986629.xml** - Sample XML data for processing
- Explore different text splitting strategies (RecursiveCharacter, Token-based, etc.)

### 4. Embeddings (`4-Embedings/`)
- **embeddingusinghuggingface.ipynb** - Generate embeddings using HuggingFace models
- **geminiembedingsusingChromadb.ipynb** - Google Gemini embeddings with ChromaDB
- **ollamaembedding.ipynb** - Local embeddings using Ollama
- Multiple embedding model options for different use cases

### 5. Vector Databases (`5-vectordatabases/`)
- **faiss.ipynb** - FAISS vector database implementation
- **faiss_vectorstore/** - Stored FAISS indices for retrieval
- Vector storage and similarity search capabilities

## Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

```bash
# Install required dependencies
pip install -r requirements.txt
```

### Running Notebooks

1. **Start with the basics:**
   - Open `1-projectusingLangchain/gettingStarted.ipynb`
   - Run `1-projectusingLangchain/simplegenaiapp.ipynb` for a complete example

2. **Explore data pipelines:**
   - Learn data ingestion in `2-dataingestion/documentsloader.ipynb`
   - Understand text splitting in `3-Data-transformation/textsplitters.ipynb`

3. **Work with embeddings:**
   - Try different embedding models in `4-Embedings/`
   - Start with HuggingFace, then explore Gemini or Ollama

4. **Implement vector search:**
   - Learn FAISS implementation in `5-vectordatabases/faiss.ipynb`
   - Use pre-built indices from `faiss_vectorstore/`

## Key Features

- 📚 **Data Ingestion** - Load documents from web and local sources
- ✂️ **Text Processing** - Advanced text splitting and chunking
- 🧠 **Embeddings** - Multiple embedding model support (HuggingFace, Gemini, Ollama)
- 🗂️ **Vector Databases** - FAISS for efficient similarity search
- 🔄 **RAG Pipeline** - Complete Retrieval-Augmented Generation workflow

## Environment Setup

Create a `.env` file in the root directory with your API keys:

```
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT_NAME=LangchainFramework
```

## Technologies Used

- **LangChain** - LLM orchestration framework
- **LangChain Community** - Additional integrations
- **HuggingFace** - Embedding models
- **Google Gemini** - Advanced embeddings
- **Ollama** - Local model inference
- **ChromaDB** - Vector database
- **FAISS** - Efficient similarity search
- **Groq** - Fast LLM inference

## Resources

- [LangChain Documentation](https://python.langchain.com)
- [LangSmith Tracing](https://smith.langchain.com)
- [HuggingFace Hub](https://huggingface.co)

## License

This project is provided for educational and learning purposes.

## Getting Help

Refer to individual notebook files for detailed implementations and comments. Each notebook includes markdown cells explaining concepts and code cells with practical examples.
