import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if request.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = request.form["data"]
        max_length = int(request.form["maxL"])
        min_length = max_length // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": min_length, "max_length": max_length},
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()