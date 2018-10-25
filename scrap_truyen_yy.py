from requests import get
from bs4 import BeautifulSoup
import requests
import time
import os



link_homepage = 'https://truyen.tangthuvien.vn/doc-truyen/ma-phap-chung-toc-dai-xuyen-viet'

home_page = requests.get(link_homepage)

soup_home = BeautifulSoup(home_page.content, 'html.parser')

link_lastchapter = soup_home.find('div',{'class':'catalog-content-wrap'}).find('div',{'class':'volume'}).find_all('li')[0].find('a').get('href')

novel_name = link_lastchapter.split('/')[-2]

a = link_lastchapter.split('/')[-1].split('-')
chapter_number = a[1]






for i in range(1, int(chapter_number)):
    link = 'https://truyen.tangthuvien.vn/doc-truyen/'+novel_name+'/'+ a[0] + '-' + str(i)
    print(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    
    title_text = soup.find("h2").get_text()
    b = soup.find('div',{'class':'chapter-c-content'})
    children = b.findChildren("div" , recursive=False)
    # print(children[0].get_text().encode('utf-8'))
    
    html = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'+ '\n' 
    html =  html + '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN' +'\n' 
    html =  html + '  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' +'\n' 
    html =  html + '<html xmlns="http://www.w3.org/1999/xhtml">' +'\n' 
    html =  html + '  <head>' +'\n' 
    html =  html + '    <title>' + title_text + '</title>' + '\n' 
    html =  html + '    <link href="stylesheet.css" rel="stylesheet" type="text/css" />' + '\n' 
    html =  html + '    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />' + '\n' 
    html =  html + '  </head>' + '\n' 
    html =  html + '  <body>' + '\n' 
    #html =  html + '    <div class="header">'+novel_name+'</div>' +'\n' 
    html =  html + '    <h4 id="C'+str(i)+'">'+title_text+'</h4>' +'\n' +'\n' 
    html =  html + '    <p>'+'\n'
    html =  html + children[0].get_text().replace("\r\n","\n")
    html =  html + '    </p>'+'\n'
    html =  html + '  </body>' +'\n' 
    html =  html + '</html>'
    
    
    if not os.path.exists(novel_name):
        os.makedirs(novel_name) 
        os.makedirs(novel_name +"/Text")
                
    with open(novel_name +'/' + str(i) + '.html', encoding = 'utf-8', mode = 'w+')as f:
        f.write(html)


