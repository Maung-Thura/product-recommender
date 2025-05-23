from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


def get_rag_chain():
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local("faiss_store", embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(temperature=0.7, model="gpt-4")

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return chain


def answer_product_query(query: str):
    rag_chain = get_rag_chain()
    response = rag_chain.run(query)
    return response
