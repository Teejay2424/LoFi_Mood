Lo-fi_mood.fm is a mood-based lo-fi playlist curator and generator that takes a short text description of how you're feeling and returns a personalized YouTube playlist. 
Built with a blend of frontend aesthetics and AI-powered backend mood analysis, it's designed for chill vibes, study sessions, or just vibing. 
Features include mood analysis from freeform text input, curated lo-fi playlists from a YouTube song database, a clean animated UI with a pure HTML/CSS/JS frontend. It’s Docker-ready and optionally supports a Python backend. 
To get started, clone the repo (git clone https://github.com/Teejay2424/lo-fi_mood.fm.git) and open index.html in your browser. 
If you're using a backend (like FastAPI), **run uvicorn app:app --reload**. For Docker, run **docker build -t lofi-playlist-app** . and then **docker run -p 8000:8000 lofi-playlist-app**. 
The project includes an index.html, optional backend (app.py), and a Dockerfile. Input examples like “I’m feeling sleepy and want something chill to listen to while studying” generate tailored lo-fi mixes. 











Licensed under MIT. 
Made with 💖 for lo-fi lovers.
