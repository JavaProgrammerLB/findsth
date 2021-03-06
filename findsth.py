import webbrowser
import sys
import requests
import logging
import time
from multiprocessing.dummy import Pool as ThreadPool

protocol='http'
topDomainName=['.com','.cn','.net','.de','.fi','.co.jp', '.ru','.me', '.edu', '.af', '.ag', '.ai', '.ar', '.au', '.bd', '.bh', '.bn', '.bo', '.br', '.bz', '.co', '.cu', '.cy', '.do', '.ec', '.eg', '.et', '.fj', '.gh', '.gi', '.gt', '.hk', '.jm', '.kh', '.kw', '.lb', '.ly', '.mm', '.mt', '.mx', '.my', '.na', '.nf', '.ng', '.ni', '.np', '.om', '.pa', '.pe', '.pg', '.ph', '.pk', '.pr', '.py', '.qa', '.sa', '.sb', '.sg', '.sl', '.sv', '.tj', '.tr', '.tw', '.ua', '.uy', '.vc', '.vn']
argv=sys.argv[1:]
print(argv)
start = time.time()

logging.basicConfig(level=logging.INFO)
domains = []
urls=[]
for i in range(len(topDomainName)):
    aTop=topDomainName[i]
    for j in range(len(argv)):
        domainName=argv[j]
        url=protocol + '://' + 'www.' + domainName + aTop
        logging.info('url is: %s',url)
        domains.append(url)
        url=protocol + '://' + domainName + aTop
        domains.append(url)

print(domains)

def con(url):
    try:
        res = requests.get(url, timeout=10)
        code = res.status_code
    except requests.exceptions.ReadTimeout:
        code = -1
    except requests.exceptions.ConnectionError:
        code = -1
    except requests.exceptions.TooManyRedirects:
        code = -1
    logging.info('url: %s, code: %d'%(url, code))
    if code == 200:
        urls.append(url)

pool = ThreadPool(10)
pool.map(con, domains)
pool.close()
pool.join()

availableCount = len(urls)
logging.info('availableCount: %d',availableCount)
for i in range(availableCount):
	logging.info('Openning: %s',urls[i])
	webbrowser.open_new_tab(urls[i])
end  = time.time()
logging.info('Costs seconds: %f s', end - start)
#webbrowser.open_new_tab(url)

