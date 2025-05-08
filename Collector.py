import os
import requests

N = int(os.getenv("NUMBER_TO_REVIEW"))
PLAYER = os.getenv("PLAYER")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.85 Safari/537.36"
}

# FETCH_ARCHIVES
url = f"https://api.chess.com/pub/player/{PLAYER}/games/archives"
response = requests.get(url, headers=HEADERS)
response.raise_for_status()
ARCHIVES = response.json().get("archives", [])
ARCHIVES.reverse()

print(f"{ len(ARCHIVES) } Archives found!")


# GET LATEST N GAMES
final_urls = []

# Go through archives in order until 10 unreviewed games have been found
for archive in ARCHIVES:

    # Get all Games
    response = requests.get(archive, headers=HEADERS)
    response.raise_for_status()
    games = response.json().get("games", [])

    #Filter Games
    pre_urls = []
    for game in games:
        if not game.get("accuracies"):
            continue

        if len(game.get("pgn", "")) > 850: # Length Check to get an estimated of atleast 5 moves per game
            pre_urls.append(game.get("url", ""))
    
    # Reverse the URLs to ensure latest are checked first
    pre_urls.reverse()

    for url in pre_urls:
        if len(final_urls) == N:
            break

        final_urls.append(url.replace("/game/", "/analysis/game/") + "?tab=review")
        
    if len(final_urls) == N:
        break

print(f"Successfully Collected { len(final_urls) }")

with open("games.txt", "w", encoding="utf-8") as f:
        for url in final_urls:
            f.write(url + "\n")