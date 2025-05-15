import os
import replicate
from flask import Flask, request, jsonify
from flask_cors import CORS

# Set your Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_YOUR_ACTUAL_TOKEN_HERE"

app = Flask(__name__)
CORS(app)

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    input_image_url = data.get("image_url")
    prompt = data.get("prompt", "cinematic cartoon style")

    try:
        output = replicate.run(
            "cjwbw/video-to-video:1c1ec3",
            input={
                "image": input_image_url,
                "prompt": prompt,
                "num_frames": 16,
                "fps": 6
            }
        )
        return jsonify({"status": "success", "video_url": output})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)