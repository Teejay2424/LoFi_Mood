Lo-fi_mood.fm is my personal take on a mood-based lo-fi playlist curator and generator that uses natural language processing to recommend personalized YouTube playlists based on your emotional state.

How it works
Users input a short text description of how they're feeling.

A fine-tuned RoBERTa model from Hugging Face Transformers analyzes the emotional tone (e.g., sad, happy).

Additional keyword parsing refines the mood context (e.g., sleepy, glee, study, chill).

Based on the detected emotion and mood, the system selects tracks from a curated dataset of 3,500+ lo-fi YouTube songs.

Features
Frontend: Pure HTML/CSS/JavaScript, responsive and animated UI

Backend (optional): FastAPI with RoBERTa-based emotion analysis

Docker support for full deployment

Real-time playlist generation with mood tagging

Input example:
"Feeling anxious and need something calm to work with" → Generates a chill, focus-driven lo-fi mix

Getting Started
Run without backend
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Teejay2424/lo-fi_mood.fm.git
Open index.html in your browser

Run with backend (FastAPI + AI)
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the backend:

bash
Copy
Edit
uvicorn app:app --reload
Run with Docker
Build the image:

bash
Copy
Edit
docker build -t lofi-playlist-app .
Run the container:

bash
Copy
Edit
docker run -p 8000:8000 lofi-playlist-app












Licensed under MIT. 
Made with 💖 for lo-fi lovers.
