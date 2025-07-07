

import json
import random
from typing import Dict, List

#
with open("songs.json", "r", encoding="utf-8") as f:
    SONG_DB = json.load(f)


def generate_playlist(mood_scores: Dict[str, float], num_songs: int = 5) -> List[Dict[str, str]]:
    
    sorted_moods = sorted(mood_scores.items(), key=lambda x: x[1], reverse=True)

    playlist = []
    for mood, _ in sorted_moods:
        songs = SONG_DB.get(mood, [])
        if not songs:
            continue

        random.shuffle(songs)

        for song in songs:
            if len(playlist) < num_songs:
                playlist.append(song)
            else:
                break

        if len(playlist) >= num_songs:
            break

    return playlist


