import requests
from bs4 import BeautifulSoup


# res = requests.get(url)
# print(res.content)
def get_citations_needed_count(url):
    # function to get citations_needed takes in a url and returns an integer
    

    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    citation_needed = soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    return len(citation_needed)

def get_citations_needed_report(url):
    # function to get citations_needed_report takes in a url and returns a string

    paragragh = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    result=soup.find_all('p')
    for p in result:
        citations=p.find_all('a',title='Wikipedia:Citation needed')
        for citation in citations:
            paragragh.append(p.text)

    return(paragragh)
# soup = BeautifulSoup(res.content, "html.parser")


if __name__ == "__main__":
    url ='https://en.wikipedia.org/wiki/History_of_Mexico'

    print(get_citations_needed_count(url))
    print((get_citations_needed_report(url)))