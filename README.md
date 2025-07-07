## Demo

![Demo of Lofi Mood.fm](demo.gif.gif)





### Click Below to see the whole demo vid !

[![Watch the demo](https://img.youtube.com/vi/WM1paWCGdCw/hqdefault.jpg)](https://youtu.be/WM1paWCGdCw)

# Lo-fi_mood.fm

**Lo-fi_mood.fm** is my personal take on a mood-based lo-fi playlist curator generator that uses natural language processing to recommend songs, for you personally based on your text input!


## How it works

- Users input a short text description of how they're feeling.
- A fine-tuned **RoBERTa** model from **Hugging Face Transformers** analyzes the emotional tone (e.g., feeling down, glee).
- Additional keyword parsing refines the mood context (e.g., sleepy, nostalgic, study, chill).
- Based on the detected emotion and mood, the system selects tracks from a curated dataset of **3,500+ lo-fi YouTube beats**.

## Features

- Frontend: Pure **HTML/CSS/JavaScript**, responsive and animated UI
- Backend (optional): **FastAPI** with **RoBERTa-based emotion analysis**
- Docker support for full deployment
- Real-time playlist generation with mood tagging
- Input example:  
  _"Feeling anxious and need something calm to work with"_ → Generates a chill, focus-driven lo-fi mix

## Getting Started

### Run without backend

```bash
git clone https://github.com/Teejay2424/lo-fi_mood.fm.git
cd lo-fi_mood.fm
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
