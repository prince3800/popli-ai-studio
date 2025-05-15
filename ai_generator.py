import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import replicate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get API token securely from environment variable
api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    raise ValueError("REPLICATE_API_TOKEN not found in environment variables")

os.environ["REPLICATE_API_TOKEN"] = api_token

model = replicate.models.get("damo-vilab/text-to-video-ms-1.7b")

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        output = model.predict(prompt=prompt)
        return jsonify({"video_urls": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)