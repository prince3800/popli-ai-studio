import replicate
import uuid
import os

# Get your Replicate API key from https://replicate.com/account/api-tokens
os.environ["REPLICATE_API_TOKEN"] = "your_replicate_api_key_here"

def generate_ai_video(prompt, voice_type="female", add_music=True, language="english"):
    output = replicate.run(
        "lucataco/text-to-video:latest",  # You can change to any Replicate model
        input={
            "prompt": prompt,
            "num_frames": 24,
            "fps": 8,
            "width": 512,
            "height": 512,
        }
    )

    video_url = output  # Replicate returns a video URL
    return video_url