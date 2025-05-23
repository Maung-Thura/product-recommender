from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Q&A (RAG)</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 min-h-screen flex flex-col items-center justify-center p-4">
    <div class="w-full max-w-xl">
        <h1 class="text-3xl font-bold mb-6 text-center">Product Q&A (RAG-powered)</h1>
        <form method="POST" class="bg-white p-6 rounded shadow-md">
            <input name="query" class="w-full p-2 border border-gray-300 rounded mb-4" placeholder="Ask about a product or ingredient..." required>
            <button class="w-full bg-blue-600 text-white p-2 rounded" type="submit">Submit</button>
        </form>
        {% if answer %}
        <div class="mt-6 p-4 bg-white rounded shadow">
            <h2 class="font-semibold">Answer:</h2>
            <p class="text-gray-800 mt-2">{{ answer }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            res = requests.get("http://localhost:8000/rag-query", params={"q": query})
            answer = res.json().get("answer", "No response from backend.")
        except Exception as e:
            answer = f"Error contacting backend: {e}"

    return render_template_string(TEMPLATE, answer=answer)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
