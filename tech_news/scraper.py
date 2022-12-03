import requests
import time
from requests.exceptions import Timeout
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
    except Timeout:
        None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h2 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": "".join(selector.css(".entry-content > p:nth-of-type(1) *::text").getall()).strip(),
        "tags": selector.css("section.post-tags ul li a::text").getall(),
        "category": selector.css(".category-style .label::text").get(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
