import requests
from bs4 import BeautifulSoup # This allows us to use that data we've gathered to do whatever we want to it scrape it.
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')


mega_links = links + links2
mega_subtext = subtext + subtext2
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        hrefs = item.select('a')
        hrefs_first_link = hrefs[0]
        title = item.getText()
        href = hrefs_first_link.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

final_result = create_custom_hn(mega_links, mega_subtext)
pprint.pprint(final_result)