import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
# from dotenv import load_dotenv

# load_dotenv()


# Load the all text files from given paths
def load_documents(doc_path="docs"):

    print(f'Loading documents from {doc_path}')

    # dir path validation
    if not os.path.exists(doc_path):
        raise FileNotFoundError(f"The directory {doc_path} does note exists")
    
    # document loading
    loader = DirectoryLoader(
        path=doc_path,
        glob="*.txt",
        loader_cls=TextLoader, # what type of loader to use for each file > TextLoader = a loader designed for plain .txt files
        loader_kwargs= {"encoding":"utf-8"}, # if we didnt provide this it uses windows defualt encoding cp1252, it cant reads UTF-8 characters (emoji, special symbols, smart quotes)
    )

    documents = loader.load() # list of lungchain documents

    if len(documents) == 0:
        raise FileNotFoundError(f"No .txt files found in {doc_path} directory")
    
    # print("### page_content = ", documents[0].page_content) # contains entire documents here
    # print("### metadata = ", documents[0].metadata) # other info of document

    ''' one file:
    Document(
        page_content="...text here...",
        metadata={"source": "file path"}
    )
    '''
    # for i, doc in enumerate(documents[:2]):
    #     print("\n###", type(doc))
    #     print(f"Doc {i+1}")
    #     print(f"Source : {doc.metadata['source']}")
    #     print(f"Content length : {len(doc.page_content)} characters\n")
    
    return documents

# Split given documents into chunks
def split_documents(documents, chunk_size=800, chunk_overlap=0):
    print(f"### Splitting documents into chunks (size={chunk_size})")

    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents=documents)
    
    # if chunks:
    #     # only first 5 chunks
    #     for i, chunk in enumerate(chunks[:5]):
    #         print(f"### Chunk {i+1}")
    #         print(f"Source : {chunk.metadata}")
    #         print(f"Chunk length : {len(chunk.page_content)} chars")
    #         print(f"Chunk content : {chunk.page_content}")

    #     if len(chunks) > 5:
    #         print(f"more {len(chunks) -5} are there...")

    return chunks # list of all chunkns of all files
    
# Creating vector db to store embeded chunks
def create_vector_store(chunks, db_path="db/chroma_db"):
    print("### Creating embeddings and storing them in a vector database")

    # embedding_model = OpenAIEmbeddings(model="text-embedding-3-small") # must pay for api key
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", # all-MiniLM-L12-v2, all-MiniLM-L6-v2, all-mpnet-base-v2
        model_kwargs={"device":"cpu"},
        encode_kwargs={"normalize_embeddings":True}
        )

    # Create chromo vector database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=db_path,
        collection_metadata={"hnsw:space":"cosine"}
    )
    print("### vector db created")

    return vector_store




def main():
    print("### Main")

    # # API KEY
    # api_key = os.getenv("OPENAI_API_KEY")
    # if not api_key:
    #     raise ValueError("OPENAI_API_KEY not found in .env file")
    # print(f"API key loaded: {api_key[:10]}...")  # Shows first 10 chars

    # load documents
    docs = load_documents() # list of txt files in type Document()

    # chunking loaded docs
    chunks = split_documents(documents=docs)

    vector_store = create_vector_store(chunks=chunks)


if __name__ == "__main__":
    main()