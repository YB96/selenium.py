from selenium import webdriver
from selenium.webdriver.chrome.options import Options

youtube_url = 'https://www.youtube.com/feed/trending'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('D:\python\chromedriver.exe',options=chrome_options)
driver.get(youtube_url)
print('page title',driver.title)