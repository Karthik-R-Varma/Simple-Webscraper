import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None


def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    quotes = soup.find_all('span', class_='text')

    for idx, quote in enumerate(quotes, start=1):
        text = quote.get_text(strip=True)
        print(f"{idx}. {text}")


def main():
    url = 'http://quotes.toscrape.com/'  # URL of the Quotes to Scrape website
    html_content = fetch_webpage(url)

    if html_content:
        parse_html(html_content)


if __name__ == "__main__":
    main()
