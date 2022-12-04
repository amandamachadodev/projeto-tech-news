from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news


# Requisito 7
def search_by_date(date):
    news = []
    try:
        date_modificated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        data = search_news({"timestamp": date_modificated})
        for item in data:
            news.append((item["title"], item["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    data = search_news({"tags": {"$regex": f"{tag}", "$options": "i"}})
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news


# Requisito 9
def search_by_category(category):
    data = search_news({"category": {"$regex": f"{category}", "$options": "i"}})
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news
