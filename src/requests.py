import requests

def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return 'valid'
        else:
            return 'invalid'
    except requests.RequestException:
        return 'invalid'



url= 'https://www.linkedin.com/feed/'
a = check_url_status(url)
print(a)
