from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from ai_generator import generate_ai_video

app = FastAPI()

# Allow CORS for mobile/web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    voice: str = "female"
    music: bool = True
    language: str = "english"

@app.post("/generate")
async def generate(prompt_data: PromptRequest):
    result = generate_ai_video(
        prompt_data.prompt,
        voice_type=prompt_data.voice,
        add_music=prompt_data.music,
        language=prompt_data.language
    )
    return {"status": "success", "video_url": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)