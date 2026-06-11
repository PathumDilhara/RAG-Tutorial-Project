from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

db_path = "db/chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", # all-MiniLM-L12-v2, all-MiniLM-L6-v2, all-mpnet-base-v2
    model_kwargs={"device":"cpu"},
    encode_kwargs={"normalize_embeddings":True}
)

db = Chroma(
    persist_directory=db_path,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}
)

# Search for relevant document
query = "In what year tesla begin production of the roadster?"

retreiver = db.as_retriever(search_kwargs={"k":3})

relevant_docs = retreiver.invoke(query)

print(f"### User query : {query}\n")

print("### Content\n")
for i, doc in enumerate(relevant_docs, 1):
    print(f"### Document {i} : \n {doc.page_content}\n------------------\n")