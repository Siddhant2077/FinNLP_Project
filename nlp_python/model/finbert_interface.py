import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Import master scraper
from nlp_python.scraper.master_scraper import collect_all_news

# ----------------------------
# FinBERT Model Load (once)
# ----------------------------
MODEL_NAME = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

labels = ["negative", "neutral", "positive"]

HEADLINES_FILE = "nlp_python/data/headlines.csv"


# --------------------------------------------------
# Step 1: Run Scraper + Sentiment for a Company
# --------------------------------------------------
def analyze_company(company_name, symbol, sector):
    """
    Full pipeline:
    1. Collect news (company + sector + announcements + Google)
    2. Run FinBERT
    """

    print(f"Starting analysis for: {company_name} ({symbol}) - Sector: {sector}")

    # Step 1: Collect news
    total_headlines = collect_all_news(company_name, symbol, sector)

    if total_headlines == 0:
        return {
            "company": company_name,
            "positive": 0,
            "neutral": 0,
            "negative": 0,
            "overall_trend": "No News Found"
        }

    # Step 2: Analyze sentiment
    return analyze_news(company_name)


# --------------------------------------------------
# Step 2: FinBERT Analysis
# --------------------------------------------------
def analyze_news(company_name):
    try:
        df = pd.read_csv(
            HEADLINES_FILE,
            encoding="utf-8",
            on_bad_lines="skip"
        )
    except Exception as e:
        return {
            "company": company_name,
            "error": "Headlines file not found",
            "details": str(e)
        }

    if "headline" not in df.columns:
        df.columns = ["headline"]

    scores = {"positive": 0, "neutral": 0, "negative": 0}

    # Limit to avoid heavy load
    for text in df["headline"].dropna().head(100):

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        prediction = torch.argmax(outputs.logits).item()
        scores[labels[prediction]] += 1

    total = sum(scores.values())

    # Sentiment score
    avg_score = (scores["positive"] - scores["negative"]) / max(total, 1)

    if avg_score > 0.3:
        trend = "Positive Outlook"
    elif avg_score < -0.3:
        trend = "Negative Outlook"
    else:
        trend = "Stable Outlook"

    return {
        "company": company_name,
        "total_news": total,
        "positive": scores["positive"],
        "neutral": scores["neutral"],
        "negative": scores["negative"],
        "overall_trend": trend,
        "sentiment_score": round(avg_score, 2)
    }
def generate_comparison_insight(r1, r2):

    score1 = r1["sentiment_score"]
    score2 = r2["sentiment_score"]

    company1 = r1["company"]
    company2 = r2["company"]

    news1 = r1["total_news"]
    news2 = r2["total_news"]

    diff = round(abs(score1 - score2), 2)

    if score1 > score2:
        better = company1
        worse = company2
    elif score2 > score1:
        better = company2
        worse = company1
    else:
        return f"Both {company1} and {company2} show similar sentiment levels in recent financial news coverage."

    return (
        f"{better} currently shows stronger market sentiment than {worse}. "
        f"The sentiment score difference is {diff}. "
        f"Based on analysis of {news1 + news2} recent financial news headlines using FinBERT, "
        f"media coverage appears more optimistic towards {better} compared to {worse}."
    )