from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import summarize_terms

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/summarize", methods=["POST", "OPTIONS"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text or len(text) < 100:
        return jsonify({"summary": "Not enough content to summarize."})

    summary = summarize_terms(text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
