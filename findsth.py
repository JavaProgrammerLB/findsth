import webbrowser
import sys
import requests
import logging

protocol='http'
topDomainName=['.com','.cn','.net','.de','.fi','.co.jp', '.ru','me']
argv=sys.argv[1:]
print(argv)

logging.basicConfig(level=logging.INFO)
urls=[]
for i in range(len(topDomainName)):
	aTop=topDomainName[i]
	for j in range(len(argv)):
		domainName=argv[j]
		url=protocol + '://' + 'www.' + domainName + aTop
		logging.info('url is: %s',url)
		try:
			req=requests.get(url, timeout=10)
			code=req.status_code
		except requests.exceptions.ReadTimeout:
			code=-1
		except requests.exceptions.ConnectionError:
			code=-1
		except requests.exceptions.TooManyRedirects:
			code=-1
		logging.info('code is: %d',code) 
		if code == 200:
			urls.append(url)
			logging.info('Available url:%s',url)

for i in range(len(urls)):
	logging.info('Openning: %s',urls[i])
	webbrowser.open_new_tab(urls[i])
#webbrowser.open_new_tab(url)

