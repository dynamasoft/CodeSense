from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")
# print("test")d


@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_model(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
