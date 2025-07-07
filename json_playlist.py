import subprocess
import json
import os

playlist_urls = {
    'sad': [
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCMxlI3EASrMmTkP0q4L5DJg',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCPMny5ShmfEZdTVboj4Z0h5',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCNDk1xHAKv30MAD4zWDqtmp'
    ],
    'happy': [
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCNAuJ3VX8z_7rcjhtvL4OM3',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCOTXBTjCJRK2Ukyt6937lkA',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCPou9-N15Io91lEDRKvzhSl'
    ],
    'study':[
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCMKLWH1J_L1Ga06beVVLmdc',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCNOv_X1q8pC8ps1iDdMCM77',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCM-CuxCUxFZhA5qJfUIEb5a'
    ],
    'sleep':[
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCMa-OzzbMPHFtqaPZ3kppFZ',
        'https://www.youtube.com/playlist?list=PLyHb1UhvByCPYak-KHLRs4tsx6ymChmG3'   
    ]
}

songs_by_mood = {}

for mood, urls in playlist_urls.items():
    print(f"Scraping mood: {mood}")
    songs_by_mood[mood] = []
    for url in urls:
        try:
            result = subprocess.run(
                ["yt-dlp", "-j", "--flat-playlist", url],
                capture_output=True, text=True
            )
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    data = json.loads(line)
                    song = {
                        "title": data.get("title"),
                        "url": f"https://www.youtube.com/watch?v={data.get('id')}"
                    }
                    songs_by_mood[mood].append(song)
        except Exception as e:
            print(f"Failed to scrape playlist: {url}\nError: {e}")

# Save to JSON file
with open("songs.json", "w", encoding="utf-8") as f:
    json.dump(songs_by_mood, f, indent=2)

print("Saved scraped songs to songs.json")
