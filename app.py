from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)

# Load your Replicate token from environment
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        prompt = data.get("prompt", "")
        duration = data.get("duration", 15)   # default 15s
        model = "facebook/musicgen:latest"

        output = replicate.run(
            model,
            input={
                "prompt": prompt,
                "duration": duration
            }
        )

        return jsonify({"status": "success", "audio_url": output})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
