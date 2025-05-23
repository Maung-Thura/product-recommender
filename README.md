# Product Recommender

AI-Powered Product Recommendation System with RAG. Please note that this system is a prototype and not ready for
Production.

## Overview

The core idea of this system is to combine retrieval-based search with generative language models to answer user
questions with contextually accurate responses drawn from a knowledge base, which are product and ingredient data.

## Implementation Steps

1. Knowledge Ingestion & Indexing

- Source: Your product, ingredient, and sales datasets (simulated as Python dicts/lists).
- These were transformed into LangChain Document objects combining:
    - Product names
    - Descriptions
    - Effects
    - Ingredients
    - Ingredient properties and common effects
- These documents were embedded using OpenAIEmbeddings and stored in a FAISS vector index.

2. Retrieval with FAISS

- At query time, the system uses vector similarity search to retrieve the top k most relevant chunks from FAISS.
- The retriever is configured to return relevant documents using semantic similarity (cosine distance in embedding
  space).

3. Generation with LangChain

- A RetrievalQA chain is used to:
    - Retrieve relevant documents.
    - Feed them along with the user query into a ChatOpenAI model (e.g., GPT-4).
    - Generate a grounded response based on retrieved content.

This ensures that the answer remains accurate, concise, and tied to your dataset.

## UI and API Integration

- The RAG system is exposed via a FastAPI endpoint /rag-query?q=....
- A simple Flask-based frontend lets users ask questions and view answers.
- The UI calls FastAPI, which invokes the LangChain pipeline and returns generated responses.

## Assumptions Made

| Area                | Assumption                                                     |
|---------------------|----------------------------------------------------------------|
| **Environment**     | Unix based                                                     |
| **Data Format**     | In-memory Python dicts simulate a DB                           |
| **LLM Access**      | OpenAI API is used for embeddings and generation               |
| **Vector Index**    | FAISS index is local and recreated if not found                |
| **Retrieval Logic** | Retrieval is semantic (based on embeddings), not keyword-based |
| **Frontend**        | Flask UI communicates with FastAPI via `localhost:8000`        |
| **Security**        | No authentication, CORS, or rate-limiting implemented          |

## Potential Improvements

- Switch to a persistent DB (PostgreSQL, Firestore) for products.
- Add chunking to support longer documents.
- Metadata filtering (e.g., filter by type: product or ingredient).
- User query logging for fine-tuning or analytics.
- UI enhancements (Streamlit dashboard, Vercel deployment, etc.).

## Prerequisites

1. [Python 3.12](https://www.python.org/downloads/release/python-3122/)
2. [OpenAI API Key](https://platform.openai.com/settings/organization/api-keys)

- Set the valid OpenAI API key in /project_root/.env file

  ```bash
  OPEN_AI_API_KEY=your_open_ai_api_key
  ```

3. [Postman](https://www.postman.com/downloads/)
4. Make sure your environment DO NOT have prior [uvicorn](https://www.uvicorn.org/) server setup. You can check by
   running below command.

  ```bash
  which uvicorn
  ```

## How to run (and test) the application in steps

1. Start backend APIs by executing *run_backend.sh* shell script under the project root directory and wait for the
   server startup to be completed (*e.g. INFO: Application startup complete.*)

```bash
cd /path/to/project_root
sh run_backend.sh
```

2. Open API test collection *product-recommender.postman_collection.json* in Postman
    1. Test *get-product-by-id*
    2. Test *get-recommendations*
    3. Test *get-enhanced-recommendations*
3. In a new terminal session, start frontend UI by executing **run_frontend.sh* shell script under the project root and
   directory and wait for the server startup to be completed (*e.g. Running on http://127.0.0.1:5000*)

```bash
cd /path/to/project_root
sh run_frontend.sh
```

4. Open http://127.0.0.1:5000 in the browser
5. Sample questions to test
    1. What is the best tea for stress relief?
    2. What is the best coffee for refreshment?

To stop both backend and frontend servers, press Ctrl + C (break) in each terminal session

## License

MIT License. Use and modify freely.

## Credits

- Powered by [LangChain](https://www.langchain.com/), [FAISS](https://github.com/facebookresearch/faiss),
  and [OpenAI](https://openai.com/)
- UI styled with [Tailwind CSS](https://tailwindcss.com/)




