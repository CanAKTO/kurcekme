import requests
from bs4 import BeautifulSoup

respons = requests.get(url="https://www.doviz.com/")


# Hata denetimi: İstek başarısız olursa hata mesajını yazdır
if respons.status_code != 200:
    print(f"Web sayfasına erişim başarısız. Hata kodu: {respons.status_code}")
    exit()

# HTML içeriğini çözümleyin
soup = BeautifulSoup(respons.text, 'html.parser')
kurlar=soup.find_all("span",{"class" : "value"})
kurlarad=soup.find_all("span",{"class" : "name"})
liste=list(kurlar)
listekurlarad=list(kurlarad)

a=0
b=0
genel=[]
for i in kurlarad:
    genel.append(listekurlarad[a].text +"-"+liste[a].text)
    a=a+1

with open("kurlar.txt" , "w") as dosya:
    for i in genel:
        dosya.write(genel[b]+"\n")
        b=b+1






