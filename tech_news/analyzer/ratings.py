from tech_news.database import find_news


# Requisito 10
def top_5_news():
    data = find_news()
    news = []
    create_return = sorted(
        data,
        key=lambda new: new["comments_count"],
        reverse=True,
    )
    for item in create_return[:5]:
        news.append((item["title"], item["url"]))
    return news



# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
