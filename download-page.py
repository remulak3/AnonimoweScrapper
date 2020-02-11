import requests
from bs4 import BeautifulSoup
from models.articleDto import articleDto


def main():
    URL = 'https://www.anonimowe.pl'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('article', class_='story on-list')
    articles = []
    for i in results:
        author = results[i].attrs['data-story']
        story = results[i].contents[3].contents
        points = results[i].contents[5].contents[1].contents[1].contents[1].contents[3].contents[0]
        date = results[i].contents[1].contents[3].attrs['title']

        x = articleDto(author, story, points, date)
        articles.append(x)

    return articles


if __name__ == "__main__":
    main()
