from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


# Requisito 12
def analyzer_menu():
    menu = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    message = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:"
    }

    if menu in message:
        select = input(message[menu])
        if menu == "0":
            print(get_tech_news(select))
        elif menu == "1":
            print(search_by_title(select))
        elif menu == "2":
            print(search_by_date(select))
        elif menu == "3":
            print(search_by_tag(select))
        else:
            print(search_by_category(select))
    elif menu in ["5", "6", "7"]:
        if menu == "5":
            print(top_5_news())
        elif menu == "6":
            print(top_5_categories())
        else:
            print("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")

    
