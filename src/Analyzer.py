import os
import json
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"
FINISH = ".tab-review-start-review-wrapper"

PLAYER = os.getenv("PLAYER")
USERNAME = os.getenv("BOT_USER")
PASSWORD = os.getenv("BOT_PASS")

TIME = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Get URLS
urls = []
with open("dump/games.txt", "r", encoding="utf8") as f:
    line = f.readline().strip()
    while line != "":
        urls.append(line)
        line = f.readline().strip()
    f.seek(0)
    line_count = sum(1 for line in f)

# Initialize Move Counts
brilliant  = 0
great      = 0
best       = 0
excellent  = 0
good       = 0
book       = 0
inaccuracy = 0
mistake    = 0
miss       = 0
blunder    = 0

# Initialize brilliant record
brilliant_urls = []

# Crawl through URLs and count Moves
def Crawl():
    with sync_playwright() as playwright:
        global urls
        failed = []
        global brilliant
        global great
        global best
        global excellent
        global good
        global book
        global inaccuracy
        global mistake
        global miss
        global blunder
        global brilliant_urls

        # Open Browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        # Open Tab and Login to chess.com
        page = context.new_page()
        page.goto(LOGIN_URL, timeout=60000)
        page.get_by_role("textbox", name="Username, Phone, or Email").click(timeout=60000)
        page.get_by_role("textbox", name="Username, Phone, or Email").fill(USERNAME, timeout=60000)
        page.get_by_role("textbox", name="Password").click(timeout=60000)
        page.get_by_role("textbox", name="Password").fill(PASSWORD, timeout=60000)
        page.get_by_role("button", name="Log In").click(timeout=60000)

        # Click Drop-Down once
        page.goto(urls[-1], timeout=60000)
        page.wait_for_selector(FINISH, timeout=60000)
        page.locator(".chevron-down").click(timeout=60000)
        # Change Engine Settings
        page.get_by_role("button", name="Settings").click(timeout=60000)
        page.get_by_label("Strength").select_option("22", timeout=60000)
        page.get_by_label("Chess Engine").select_option("STOCKFISH (NNUE)", timeout=60000)
        page.get_by_label("Number of Lines").select_option("5", timeout=60000)
        page.get_by_role("button", name="Close").click(timeout=60000)

        #Sequentially go through urls and sum the moves
        for i in range(len(urls)):
            url = urls[i]
            page.goto(url, timeout=60000)
            try:
                page.wait_for_selector(FINISH, timeout=60000)
                index = 0 if page.locator(".game-overview-player").nth(0).inner_text() == PLAYER else 1
                brill = int(page.locator(".analysis-brilliant" ).nth(index).inner_text())
                brilliant  = brilliant  + brill
                great      = great      + int(page.locator(".analysis-greatFind" ).nth(index).inner_text())
                best       = best       + int(page.locator(".analysis-bestMove"  ).nth(index).inner_text())
                excellent  = excellent  + int(page.locator(".analysis-excellent" ).nth(index).inner_text())
                good       = good       + int(page.locator(".analysis-good"      ).nth(index).inner_text())
                book       = book       + int(page.locator(".analysis-book"      ).nth(index).inner_text())
                inaccuracy = inaccuracy + int(page.locator(".analysis-inaccuracy").nth(index).inner_text())
                mistake    = mistake    + int(page.locator(".analysis-mistake"   ).nth(index).inner_text())
                miss       = miss       + int(page.locator(".analysis-miss"      ).nth(index).inner_text())
                blunder    = blunder    + int(page.locator(".analysis-blunder"   ).nth(index).inner_text())

                if brill:
                    page.locator(".analysis-brilliant" ).nth(index).click()
                    brilliant_urls.append([brill, page.url])

            except Exception as e:
                print(f"\tCouldn't get from {i + 1}{'st' if i == 0 else ('nd' if i == 1 else ('rd' if i == 2 else 'th' ))} game\n\t\t{str(e).replace('\n', '\n\t\t')}\n")
                failed.append(url)

        urls = failed
        context.close()
        browser.close()
    
for i in range(3):
    print(f"Iteration {i + 1}")
    Crawl()
    if len(urls) == 0:
        break
    print("Sleeping for 2mins")
    time.sleep(120)

print(brilliant)
print(great)
print(best)
print(excellent)
print(good)
print(book)
print(inaccuracy)
print(mistake)
print(miss)
print(blunder)
print(brilliant_urls)

moveCounts = {
    "time" : TIME,
    "brilliant": brilliant,
    "great" : great,
    "best" : best,
    "excellent" : excellent,
    "good" : good,
    "book" : book,
    "inaccuracy" : inaccuracy,
    "mistake" : mistake,
    "miss" : miss,
    "blunder" : blunder,
    "games": line_count,
    "brilliant_urls": brilliant_urls
}

os.makedirs(os.path.dirname("dump/moves.json"), exist_ok=True)
with open("dump/moves.json", "w") as f:
    json.dump(moveCounts, f, indent=4)