from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from dal import products
from rag import answer_product_query

app = FastAPI()


# Endpoint: Get product information by ID
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# Endpoint: Get product recommendations by desired effect
@app.get("/recommendations")
def get_recommendations(effect: Optional[str] = Query(None, description="Desired effect like relaxation")):
    matched_products = [
        product for product in products
        if effect in product["effects"]
    ] if effect else products

    if not matched_products:
        raise HTTPException(status_code=404, detail="No products match the given effect")

    return matched_products


@app.get("/rag-query")
def ask_about_product(q: str = Query(..., description="Ask about a product or ingredient")):
    response = answer_product_query(q)
    return {"query": q, "answer": response}
