'''
Simulated Data Access Layer (dal)
'''

products = [
    {
        "id": 1,
        "name": "Relaxation Tea",
        "type": "beverage",
        "description": "A soothing herbal tea blend designed for relaxation and stress relief.",
        "effects": ["relaxation", "stress relief"],
        "ingredients": ["Chamomile", "Lavender"],
        "price": 12.99,
        "sales_data": {
            "units_sold": 120,
            "last_month_revenue": 1558.8
        }
    }
]

ingredients_info = [
    {
        "name": "Chamomile",
        "properties": "Mild, floral aroma; known for calming effects",
        "common_effects": ["relaxation", "improved sleep"]
    }
]

sales_data = [
    {
        "product_id": 1,
        "daily_sales": [
            {"date": "2025-01-01", "units_sold": 5},
            {"date": "2025-01-02", "units_sold": 7}
        ]
    }
]
