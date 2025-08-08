import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc():
    url = "https://www.bbc.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all(["h2", "h3"])
    return [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

def scrape_hindustantimes():
    url = "https://www.hindustantimes.com/latest-news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h3")
    return [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

def scrape_toi():
    url = "https://timesofindia.indiatimes.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all(["h3", "span"])
    return [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

# Collect headlines
news_data = {
    "BBC News": scrape_bbc(),
    "Hindustan Times": scrape_hindustantimes(),
    "Times of India": scrape_toi()
}

# Create timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = f"headlines_{timestamp}.txt"

# Remove duplicates & save
seen = set()
with open(filename, "w", encoding="utf-8") as file:
    for source, headlines in news_data.items():
        file.write(f"\n===== {source} =====\n")
        print(f"\n===== {source} =====")
        count = 0
        for headline in headlines:
            if headline not in seen:
                seen.add(headline)
                count += 1
                file.write(f"{count}. {headline}\n")
                print(f"{count}. {headline}")
        print(f"✅ {source}: {count} headlines saved")

print(f"\nAll headlines saved to '{filename}'")

