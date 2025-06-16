import requests
import re
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

print(parsed_html.title.text)


top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'', '', p.text).strip())
    print(top_jobs_heading.text)
