import pandas as pd
from nlp_python.scraper.news_source import (
    scrape_google_news,
    scrape_economic_times,
    scrape_moneycontrol,
    scrape_business_standard,
    scrape_company_announcements
)

HEADLINES_FILE = "nlp_python/data/headlines.csv"


def collect_all_news(company_name, symbol, sector):
    all_headlines = []

    print("Collecting company announcements...")
    all_headlines += scrape_company_announcements(symbol)

    print("Collecting company news from websites...")
    all_headlines += scrape_economic_times(company_name)
    all_headlines += scrape_moneycontrol(company_name)
    all_headlines += scrape_business_standard(company_name)

    print("Collecting sector news...")
    all_headlines += scrape_economic_times(sector)
    all_headlines += scrape_moneycontrol(sector)

    print("Fallback: Google News...")
    all_headlines += scrape_google_news(company_name)
    all_headlines += scrape_google_news(sector)

    # Remove duplicates
    all_headlines = list(set(all_headlines))

    # Filter small text
    all_headlines = [h for h in all_headlines if len(h) > 30]

    # Save
    df = pd.DataFrame(all_headlines, columns=["headline"])
    df.to_csv(HEADLINES_FILE, index=False, encoding="utf-8")

    print(f"Total headlines collected: {len(all_headlines)}")
    return len(all_headlines)