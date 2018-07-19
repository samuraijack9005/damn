import bs4 as sb
import urllib.request as r
city=input("enter the city :bengaluru:mysore:gulbarga:belgaum \n")

print("***********Affiliated Institutes Of "+city+"*********\n")
str1="http://vtu.ac.in/affiliated-institutes/affiliated-institutes-"
sto=str1+city.strip()
str2=sto.strip()
s=r.urlopen(str2)
soup=sb.BeautifulSoup(s)
#for pa in soup.find_all('p'):
    #print(pa.text)
#for u in soup.find_all('a'):
        #print(u.get('href'))
#print(soup.title)
table=soup.find('table')
#print(table)
rows=table.findAll('tr')
#print(rows)
for tr in rows:
    cols=tr.findAll('td')
    for ele in cols:
        if ele==cols[2]:
            print(ele.text.strip())
        
        
       
    
