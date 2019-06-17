
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/?nm_mc=KNC-GoogleKWLess&cm_mmc=KNC-GoogleKWLess-_-Branding-_-Main-_-Misspelled&&s_kwcid=AL!5844!3!40646928410!e!!g!!neweggs&gclid=Cj0KCQiA1sriBRD-ARIsABYdwwGAZ3y42C7GZh9-eg0IQynZxljWSApgmW__UnVdOpK-xCAhXB9Ovx0aAmNREALw_wcB&gclsrc=aw.ds'
#open up connction and prabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')
print(page_soup.h1)


print (134)