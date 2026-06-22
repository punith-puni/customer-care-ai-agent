from rag.retriever import search_docs

result = search_docs(
    "What is your return policy?"
)

print(result)