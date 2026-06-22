from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

documents = []

POLICY_FOLDER = "policies"

for file in os.listdir(POLICY_FOLDER):

    path = os.path.join(POLICY_FOLDER, file)

    with open(path, "r", encoding="utf-8") as f:
        documents.append(f.read())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = []

for doc in documents:
    chunks.extend(splitter.split_text(doc))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(
    chunks,
    embeddings
)

vectorstore.save_local("faiss_index")

print("FAISS Index Created Successfully")