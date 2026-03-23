import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}


def scrape_economic_times(query):
    headlines = []
    q = query.replace(" ", "-")
    url = f"https://economictimes.indiatimes.com/topic/{q}"

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a"):
            text = a.get_text(strip=True)
            if len(text) > 30:
                headlines.append(text)
    except:
        pass

    return headlines[:20]

def scrape_moneycontrol(query):
    headlines = []
    q = query.replace(" ", "%20")
    url = f"https://www.moneycontrol.com/news/tags/{q}.html"

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for h in soup.find_all("h2"):
            text = h.get_text(strip=True)
            if len(text) > 30:
                headlines.append(text)
    except:
        pass

    return headlines[:20]



def scrape_business_standard(query):
    headlines = []
    q = query.replace(" ", "-")
    url = f"https://www.business-standard.com/search?q={q}"

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a"):
            text = a.get_text(strip=True)
            if len(text) > 30:
                headlines.append(text)
    except:
        pass

    return headlines[:20]


def scrape_company_announcements(symbol):
    headlines = []
    url = f"https://www.nseindia.com/api/corporate-announcements?symbol={symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)

        res = session.get(url, headers=headers)
        data = res.json()

        for item in data[:20]:
            headlines.append(item.get("subject", ""))
    except:
        pass

    return headlines


def scrape_google_news(query):
    headlines = []
    q = query.replace(" ", "+")
    url = f"https://news.google.com/search?q={q}"

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a"):
            text = a.get_text(strip=True)
            if len(text) > 30:
                headlines.append(text)
    except:
        pass

    return headlines[:20]