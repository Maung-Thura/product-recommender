from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dal import products, ingredients_info


def prepare_documents():
    docs = []

    for p in products:
        content = f"{p['name']} - {p['description']} Effects: {', '.join(p['effects'])}. Ingredients: {', '.join(p['ingredients'])}"
        docs.append(Document(page_content=content, metadata={"type": "product", "id": p["id"]}))

    for ing in ingredients_info:
        content = f"{ing['name']} - Properties: {ing['properties']}. Common effects: {', '.join(ing['common_effects'])}"
        docs.append(Document(page_content=content, metadata={"type": "ingredient"}))

    return docs


def build_faiss_index():
    embeddings = OpenAIEmbeddings()
    docs = prepare_documents()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_store")
    print("FAISS index saved to faiss_store/")


if __name__ == "__main__":
    build_faiss_index()
