#jst learning github
#fefefefe



from bs4 import BeautifulSoup
import requests
u="1mv15cs"
for i in range(1,135):
    if (i<10):
        pre='00'
    elif (i<100):
        pre='0'
    else:
        pre=''
    no=str(i)
    usn=u+pre+no
    url="http://result.vtu.ac.in/cbcs_results2016.aspx?usn="+usn+"&sem=2"
    reqfile = requests.get(url)
    soup = BeautifulSoup(reqfile.content,"html5lib")
    #print soup.prettify()
    #print soup.title.text
    if(soup.title.text=="cbcs_result"):
        continue
    print usn
    print soup.find(id="txtName")['value'],soup.find(id="lblSGtgtgA").text
    print ''
