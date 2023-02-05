from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
prompt = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = input()
    prompt.append(ele)
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe",service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
a=driver.find_element("name","q")
#driver.page_source (for getting the source code html file)
a.send_keys("wikipedia")
a.send_keys(Keys.RETURN)
c=driver.find_element(By.CLASS_NAME,"yuRUbf")
link=c.find_element(By.TAG_NAME,"a")
link.click()
for p in prompt:
    print(p)
    searchbox=driver.find_element(By.ID,"searchInput")
    searchbox.send_keys(p)
    searchbox.send_keys(Keys.RETURN)
    html=driver.page_source
    doc=BeautifulSoup(html,'html.parser')
    content=doc.find('main',{'id': 'content'})
    children = content.findChildren()
    # Print all children of an element
    for child in children:
            print(child.text)
    driver.get("https://www.wikipedia.org")
driver.quit()
