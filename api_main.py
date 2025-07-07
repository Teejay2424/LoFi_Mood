from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mood_analyzer import LofiMoodAnalyzer
from playlist_generator import generate_playlist

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
analyzer = LofiMoodAnalyzer()
class MoodRequest(BaseModel):
    text: str
    num_songs: int = 15     

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze_mood")
async def analyze_mood(data: MoodRequest):
    scores = analyzer.analyze_mood(data.text)
    return JSONResponse(content=scores)

@app.post("/recommend_from_text")
async def recommend_from_text(data: MoodRequest):
    mood_scores = analyzer.analyze_mood(data.text)
    playlist = generate_playlist(mood_scores, data.num_songs)
    return JSONResponse(content=playlist)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
