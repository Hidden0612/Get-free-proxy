import requests
from bs4 import BeautifulSoup

def get_proxiesـone():
    url = "https://free-proxy-list.net/"
    resp = requests.get(url).content
    soup = BeautifulSoup(resp , "html.parser")
    proxies = []
    for rw in soup.find("table", {"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        td = rw.find_all("td")
        try:
            proxies.append(
                {
                    "ip":td[0].text.strip(),
                    "port":td[1].text.strip(),
                    "country":td[3].text.strip(),
                    "protocols":"https" if td[6].text.strip() == "yes" else "http"
                }
            )
        except:
            continue
    return proxies

def get_proxies_two(limit):
    url = f"https://proxylist.geonode.com/api/proxy-list?limit={limit}&page=1&sort_by=lastChecked&sort_type=desc"
    resp = requests.get(url).json()
    proxies = []
    for prx in resp["data"]:
        proxies.append(
                {
                    "ip":prx["ip"],
                    "port":prx["port"],
                    "country":prx["country"],
                    "protocols":prx["protocols"][0]
                }
            )
    return proxies

if __name__ == "__main__":
    prx_two = get_proxies_two(200)
    prx_one = get_proxiesـone()
    

