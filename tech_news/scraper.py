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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
