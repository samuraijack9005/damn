
import bs4 as sb
import urllib.request as r
s=r.urlopen("http://vtu.ac.in/affiliated-institutes/affiliated-institutes-mysore/")
soup=sb.BeautifulSoup(s)
print(soup.title)
