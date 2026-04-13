import requests

def search_pubmed(query):
    # make api call
    request = requests.get(query).json()
    return request['esearchresult']['idlist']


def fetch_abstracts(ids):
    return ""

def get_rag_context(abstracts):
    return ""


print(search_pubmed("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=t+cell+exhaustion&retmode=json"))