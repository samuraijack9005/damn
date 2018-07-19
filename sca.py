import bs4 as sb
import urllib.request as r
city=input("enter the city")
str1="http://vtu.ac.in/affiliated-institutes/affiliated-institutes-"
sto=str1+city.strip()
str2=sto.strip()
s=r.urlopen(str2)
soup=sb.BeautifulSoup(s)
#for pa in soup.find_all('p'):
    #print(pa.text)
#for u in soup.find_all('a'):
        #print(u.get('href'))
print(soup.title)
