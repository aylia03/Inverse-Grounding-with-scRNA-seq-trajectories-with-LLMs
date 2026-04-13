import requests

def search_pubmed(query):
    # make api call
    request = requests.get(query).json()
    return request['esearchresult']['idlist']


def fetch_abstracts(ids):
    ids_str = ",".join(ids)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids_str}&retmode=text&rettype=abstract"
    response = requests.get(url).text
    return response

def get_rag_context():
    return fetch_abstracts(search_pubmed("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=t+cell+exhaustion+marker&retmode=json&retmax=30"))


print(get_rag_context())