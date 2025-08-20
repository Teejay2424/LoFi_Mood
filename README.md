## Demo

![Demo of Lofi Mood.fm](demo.gif.gif)





### Click Below to see the whole demo vid !

[![Watch the demo](https://img.youtube.com/vi/WM1paWCGdCw/hqdefault.jpg)](https://youtu.be/WM1paWCGdCw) <br>
(P.S: The demo shows what kindof beats may pop up when you may feel sleepy/tired; you can try it out with some other mood specifc prompts and notice how the songs' tempos and instrumentation differ)


# LoFi_Mood

**LoFi_Mood** is my personal take on a mood-based lo-fi playlist curator generator that uses natural language processing to recommend songs, depending on the user prompt.


## How it works

- Users input a short text description of how they're feeling.
- A fine-tuned **RoBERTa** model from **Hugging Face Transformers** analyzes the emotional tone (e.g., feeling down, happy).
- Additional keyword parsing refines the mood context (e.g., sleepy, nostalgic, study, chill).
- Based on the detected emotion and mood, the system selects tracks from a curated dataset of **3,500+ lo-fi YouTube beats**. For example, entering a more positive feeling prompt may make the model output some higher tempo, drum forward songs whereas a more negative prompt may give out beats with a slower tempo that focus on the synths.

## Features

- Frontend: Pure **HTML/CSS/JavaScript**, responsive and animated UI
- Backend (optional): **FastAPI** with **RoBERTa-based emotion analysis**
- Docker support for full deployment
- Real-time playlist generation with mood tagging
- Input example:  
  _"Feeling anxious and need something calm to work with"_ → Generates a chill, focus-driven lo-fi mix with less drums, slower tempo, and looser transitions.

## Getting Started

### Run without backend

```bash
git clone https://github.com/Teejay2424/lo-fi_mood.git
cd lo-fi_mood
# Open index.html directly in your browser
```

### Run with backend (FastAPI + AI)

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Run with Docker

```bash
docker build -t lofi-playlist-app .
docker run -p 8000:8000 lofi-playlist-app
```















Licensed under MIT. 
Made with 💖 for lo-fi lovers ( myself included :) ).
