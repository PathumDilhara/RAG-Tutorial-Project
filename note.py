# pip install langchain langchain-community langchain_text_splitters langchain_openai langchain_chroma python_dotenv
# pip install sentence-transformers

''' langchain
The core LangChain framework

Provides:
    Chains
    Prompts
    Runnables
    Retrievers interfaces
    Document abstractions
The main framework that connects all the AI components together
Without it, the other LangChain packages don't have much meaning
'''

'''langchain-community
Contains integrations maintained by the community
    FAISS
    HuggingFace models
    PDF loaders
    Web loaders
    Various vector databases
A collection of connectors to external tools and services
'''

'''langchain_text_splitters
Used to split large documents into smaller chunks
'''

'''langchain_openai
Connects LangChain to OpenAI models
'''

'''langchain_chroma
Integration between LangChain and ChromaDB(vector database)
'''
# NOTE
'''Since langchain-community is being deprecated (sunset) as of May 22, 2026

replace langchain-community imports with standalone packages. Common replacements:

Instead of this from langchain-community	    Use this standalone package
document_loaders (PDF, text, etc.)	            langchain-document-loaders
embeddings (OpenAI, HuggingFace)	            langchain-openai, langchain-huggingface
vectorstores (Chroma, Pinecone)	                langchain-chroma, langchain-pinecone
chat_models	                                    langchain-openai, langchain-anthropic
'''


# Free HuggingFaceEmbeddings
'''
First, install the required package:
pip install sentence-transformers


Best Overall: All-MiniLM-L6-v2
    Size: 80MB (small, runs on any computer)
    Speed: Fast
    Quality: Good (85% as good as OpenAI)
    Memory: ~500MB RAM

Higher Quality (Slower): all-mpnet-base-v2
    Size: 420MB
    Speed: Slower
    Quality: Better (92% as good as OpenAI)
    Memory: ~1.5GB RAM

Lightest & Fastest: all-MiniLM-L12-v2
    Size: 120MB
    Speed: Very fast
    Quality: Medium (80% as good)
    Memory: ~700MB RAM
'''