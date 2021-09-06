#imports
from bs4 import BeautifulSoup
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException

#setting options for chromedriver
options = Options()
options.add_argument("--headless")
options.add_argument("--enable-javascript")
driver = wb.Chrome(executable_path=r'chromedriver.exe',options=options)


#formatting query string
Query=input("Enter the Product to Search: ")
Query=Query.replace(" ","-")
Query="/q-"+Query
location=input("Enter City to Search: ")
count=0

#getting html request
driver.get("https://olx.com.pk/"+location+Query)


while True:
    try:
        
        loadMoreButton = driver.find_element_by_xpath("//span[text()='Load more']")
        loadMoreButton.click()
        #print("LOAD MORE button clicked")
        time.sleep(3)
        count=count+1
    except NoSuchElementException:
        #print("No More Load More")
        break


r=driver.page_source
doc=BeautifulSoup(r,"html.parser")


#finding prices and titles
prices=doc.find_all('span', {'class' : '_7978e49c _2e82a662'})
titles=doc.find_all('div', {'class' : 'c2b197f0'})
City=doc.find_all('div', {'class' : '_424bf2a8'})


#printing titles

s="No Products Found in this city"
for x in range(len(titles)):
        if (City[x].string == location.capitalize()):
                print(titles[x].string)
                print(prices[x].string)
                print(City[x].string+'\n')
                s="No more Products Found in the City"
        else:
            print(s)
            break