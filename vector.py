from langchain_ollama import OllamaEmbeddings, embeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
df=pd.read_csv("extracted_data.csv")
embeddings = OllamaEmbeddings(model="nomic-embed-text")
db_location="./chroma_langchain_db"

add_documents=not os.path.exists(db_location)

if add_documents:
    docs=[]
    ids=[]

    for i, row in df.iterrows():
        doc = Document(page_content=row["Input sentence"], metadata={                
            "skill": row["Skill"],
            "technology": row["Technology"],
            "language": row["Language"]
            })
        id=str(i)
        ids.append(str(i))
        docs.append(doc)
vector_store= Chroma(
    collection_name="Candidate_Resume",
    persist_directory=db_location,
    embedding_function=embeddings,
)
if add_documents:
    vector_store.add_documents(documents=docs, ids=ids)
    print(f"Added {len(docs)} documents to Chroma.")

retriever = vector_store.as_retriever(search_kwargs={"k": 10})