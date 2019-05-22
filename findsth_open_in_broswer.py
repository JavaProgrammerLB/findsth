from selenium import webdriver

def open_in_chrome_incognito(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(url)

def main():
    open_in_chrome_incognito("https://www.baidu.com")
    open_in_chrome_incognito("https://www.qq.com")

if __name__ == '__main__':
    main()

