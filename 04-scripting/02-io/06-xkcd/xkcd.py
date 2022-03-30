



def fetch_xkcd():
    return requests.get('https://xkcd.com/info.0.json').json()