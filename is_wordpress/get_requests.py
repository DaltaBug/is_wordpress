import requests
def get_page_requests(url):
    if (not url.startswith('http')):
        url = 'http://'+url
    page_code = requests.get(url)
    return page_code.text