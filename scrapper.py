#!/usr/bin/python

# -*- coding: utf-8 -*-


from requests import get
from bs4 import BeautifulSoup
import requests
import time
import os
from selenium import webdriver

class Scrapper():
    
    def __init__(self, link, saveFolder):
        self.link = link
        self.save_folder = saveFolder
        #self.chap_num = 0
        self.chap_progress = 0
        
        web = self.link.split('/')[2]
        print(web)
        if "full" in web:
            self.w = 0
        elif "tangthuvien" in web:
            self.w = 1
        elif "webtruyen" in web:
            self.w = 2
        elif "sstruyen" in web:
            self.w = 3
        elif "falun" in web:
            self.w = 4
    
    def get_infos(self, link):
        #truyenfull
        if(self.w == 0):
            novel_name = link.split('/')[3]
            page = requests.get(link,verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_chap = str(soup.find(class_="list-chapter").a["href"])
            return novel_name, first_chap
        #tang thu vien            
        elif(self.w == 1):
            novel_name = link.split('/')[4]
            page = requests.get(link,verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_chap = soup.find(id="max-volume").a["href"]
            return novel_name, first_chap
        #webtruyen
        elif(self.w == 2):
            novel_name = link.split('/')[3]
            page = requests.get(link,verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_chap = str(soup.find(id="divtab").a["href"])
            return novel_name, first_chap
        elif(self.w == 3):
            novel_name = link.split('/')[4]
            page = requests.get(link,verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_chap = "http://sstruyen.com" + str(soup.find_all(class_="chuongmoi")[-1].a["href"])
            return novel_name, first_chap
        elif(self.w == 4):
            novel_name = link.split('/')[4]
            page = requests.get(link,verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_chap = soup.find(class_="mybody").p.a["href"]
            return novel_name, first_chap
            
    
                
    def content_opf_def(self, novel_name):
        content_opf =               '<?xml version="1.0"  encoding="UTF-8"?>'+ '\n' 
        content_opf = content_opf + '<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">'+ '\n' 
        content_opf = content_opf + '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">'+ '\n' 
        content_opf = content_opf + '    <dc:title>'+novel_name+'</dc:title>'+ '\n' 
        content_opf = content_opf + '    <dc:identifier id="BookId" opf:scheme="UUID">urn:uuid:e5cb99bd-0e41-4213-b61e-1b93b7240d30</dc:identifier>'+ '\n' 
        content_opf = content_opf + '    <dc:date>0101-01-01T00:00:00+00:00</dc:date>'+ '\n' 
        content_opf = content_opf + '    <dc:publisher>www.dtv-ebook.com</dc:publisher>'+ '\n' 
        content_opf = content_opf + '    <dc:contributor opf:role="bkp">calibre (3.30.0) [https://calibre-ebook.com]</dc:contributor>'+ '\n' 
        content_opf = content_opf + '    <dc:language>vi</dc:language>'+ '\n' 
        content_opf = content_opf + '    <dc:identifier opf:scheme="calibre">ea7f674d-6ee8-4154-a0a2-70a5bdabd402</dc:identifier>'+ '\n' 
        content_opf = content_opf + '    <meta name="cover" content="cover"/>'+ '\n' 
        content_opf = content_opf + '    <meta content="2.0" name="Ebook Builder"/>'+ '\n' 
        content_opf = content_opf + '    <meta name="calibre:title_sort" content="'+novel_name+'"/>'+ '\n' 
        content_opf = content_opf + '    <meta name="calibre:author_link_map" content="{&quot;Habom&quot;: &quot;&quot;}"/>'+ '\n' 
        content_opf = content_opf + '  </metadata>'+ '\n' 
        content_opf = content_opf + '  <manifest>'+ '\n' 
        content_opf = content_opf + '    <item id="mucluc" href="Text/mucluc.html" media-type="application/xhtml+xml"/>'
        return content_opf

    def toc_prefix_def(self, novel_name):
        toc_prefix =              '<?xml version="1.0" encoding="utf-8" ?>'+ '\n' 
        toc_prefix =  toc_prefix +'<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"'+ '\n' 
        toc_prefix =  toc_prefix +' "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">'+ '\n' 
        toc_prefix =  toc_prefix +'<ncx version="2005-1" xmlns="http://www.daisy.org/z3986/2005/ncx/">'+ '\n' 
        toc_prefix =  toc_prefix +'  <head>'+ '\n' 
        toc_prefix =  toc_prefix +'    <meta content="urn:uuid:e5cb99bd-0e41-4213-b61e-1b93b7240d30" name="dtb:uid"/>'+ '\n' 
        toc_prefix =  toc_prefix +'    <meta content="0" name="dtb:depth"/>'+ '\n' 
        toc_prefix =  toc_prefix +'    <meta content="0" name="dtb:totalPageCount"/>'+ '\n' 
        toc_prefix =  toc_prefix +'    <meta content="0" name="dtb:maxPageNumber"/>'+ '\n' 
        toc_prefix =  toc_prefix +'  </head>'+ '\n' 
        toc_prefix =  toc_prefix +'  <docTitle>'+ '\n' 
        toc_prefix =  toc_prefix +'    <text>'+novel_name+'</text>'+ '\n' 
        toc_prefix =  toc_prefix +'  </docTitle>'+ '\n' 
        toc_prefix =  toc_prefix +'  <navMap>'+ '\n' 
        toc_prefix =  toc_prefix +'    <navPoint id="mucluc" playorder="0">'+ '\n' 
        toc_prefix =  toc_prefix +'      <navLabel>'+'\n' 
        toc_prefix =  toc_prefix +'        <text>Mục lục</text>'+ '\n' 
        toc_prefix =  toc_prefix +'      </navLabel>'+ '\n' 
        toc_prefix =  toc_prefix +'      <content src="Text/mucluc.html"/>'+ '\n' 
        return toc_prefix

    def mucluc_prefix_def(self,novel_name):
        mucluc_prefix =                 '<?xml version="1.0" encoding="utf-8" standalone="no"?>'+ '\n' 
        mucluc_prefix = mucluc_prefix + '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"'+ '\n' 
        mucluc_prefix = mucluc_prefix + '  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'+ '\n' 
        mucluc_prefix = mucluc_prefix + '<html xmlns="http://www.w3.org/1999/xhtml">'+ '\n' 
        mucluc_prefix = mucluc_prefix + '  <head>'+ '\n' 
        mucluc_prefix = mucluc_prefix + '    <title>Mục lục</title>'+ '\n' 
        mucluc_prefix = mucluc_prefix + '    <link href="../stylesheet.css" rel="stylesheet" type="text/css" />'+ '\n' 
        mucluc_prefix = mucluc_prefix + '    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'+ '\n' 
        mucluc_prefix = mucluc_prefix + '  </head>'+ '\n' 
        mucluc_prefix = mucluc_prefix + '  <body>'+ '\n' 
        mucluc_prefix = mucluc_prefix + '  <h4>Mục lục</h4>'+ '\n' 
        return mucluc_prefix
        
        
    def toc_file(self, chapter_number, chapter_title):
        toc =      '    <navPoint id="nav'+ chapter_number+'" playorder="'+chapter_number+'">'+ '\n' 
        toc = toc +'      <navLabel>'+ '\n' 
        toc = toc +'        <text>'+chapter_title+'</text>'+ '\n' 
        toc = toc +'      </navLabel>'+ '\n' 
        toc = toc +'      <content src="Text/C'+chapter_number+'.html"/>'+ '\n' 
        toc = toc +'    </navPoint>'+ '\n' 
        return toc

    def mucluc(self, chapter_number, chapter_title):
        return '    <div class="lv2"><a href="../Text/C'+ chapter_number +'.html">'+ chapter_title +'</a></div>' + '\n' 

    def content_opf_item(self, chapter_number):
        return '\n'+'    <item id="C'+chapter_number+'" href="Text/C'+chapter_number+'.html" media-type="application/xhtml+xml"/>'
        
    def content_opf_ref(self, chapter_number):
        return '\n'+'    <itemref idref="C'+chapter_number+'"/>'



    def run(self):
            novel_name, first_chap = self.get_infos(self.link)
            self.novelname = novel_name
            
            #cac file ko thay doi gi ca
            cover_img = b''
            with open('cover.jpg',mode ="rb") as file:
                cover_img = file.read()
                
            css = b''
            with open('stylesheet.css',mode = 'rb') as file:
                css = file.read()
            
            mimetype = b''
            with open('mimetype',mode = 'rb') as file:
                mimetype = file.read()
            
            container = b''
            with open('container.xml', mode = 'rb') as file:
                container = file.read()
            #----------------------------
        
        
            mucluc_html = ""
            toc = ""
            opf_item = ""
            opf_ref = ""
            new_dir = self.save_folder + '/' + novel_name + "/"
            
            if not os.path.exists(self.save_folder + '/' + novel_name):
                os.makedirs(self.save_folder+ '/' + novel_name)
                os.makedirs(self.save_folder+ '/' + novel_name + '/Text')
                
            if not os.path.exists(new_dir + "META-INF"):
                os.makedirs(new_dir +"META-INF")
            

            self.next_chap = first_chap
            self.has_next_chapter = 1
            chapter = 0
            while(self.has_next_chapter==1):
                self.chap_progress = chapter
                chap = ""
                title_text = ""
                #truyenfull
                if(self.w==0):
                    time.sleep(0.4)
                    print(self.next_chap)
                    chap_page = requests.get(self.next_chap,verify=False)
                    chap_soup = BeautifulSoup(chap_page.content, 'html.parser')
                    
                    title_text = chap_soup.find("h2").get_text()
                    chap = str(chap_soup.find(class_="chapter-c"))   
                    
                    next_button = chap_soup.find(id="next_chap")
                    if("disabled" in str(next_button)):
                        self.has_next_chapter = 0
                        break
                    
                    self.next_chap = str(next_button["href"])
                    
                    
                #tangthuvien
                elif(self.w==1):
                    print(self.next_chap)
                    chap_page = requests.get(self.next_chap,verify=False)
                    chap_soup = BeautifulSoup(chap_page.content, 'html.parser')
                    
                    lst = self.next_chap.split("-")
                    lst[-1] = str(int(lst[-1])+1)
                    self.next_chap = "-".join(lst)
                    
                    b = chap_soup.find('div',{'class':'chapter-c-content'})
                    if(b==None):
                        self.has_next_chapter = 0
                        break
                    children = b.findChildren("div" , recursive=False)
                    chap = "<p> "+'\n' 
                    chap = chap + "    " + children[0].get_text().replace("\r\n","<br>") + '\n' 
                    chap = chap + "    </p>" 
                    title_text = str(chap_soup.find("h2").get_text())
                    
                #webtruyen
                elif(self.w==2):
                    print(self.next_chap)
                    chap_page = requests.get(self.next_chap,verify=False)
                    chap_soup = BeautifulSoup(chap_page.content, 'html.parser')
                    
                    title_text = str(chap_soup.find("h3").get_text())
                    chap = str(chap_soup.find(id="divcontent"))   
                    
                    next_button = chap_soup.find(id="nextchap")
                    if(next_button==None):
                        self.has_next_chapter = 0
                        break
                    
                    self.next_chap = str(next_button["href"])
                    
                    
                #sstruyen
                elif(self.w==3):
                    print(self.next_chap)
                    options = webdriver.ChromeOptions()
                    options.add_argument('headless')
                    
                    browser = webdriver.Chrome(r"D:\11102018\Ha_Nguyen\workspace\project\chromedriver.exe", chrome_options=options)
                    # browser = webdriver.PhantomJS(r"D:\11102018\Ha_Nguyen\workspace\project\phantomjs-2.1.1-windows\bin\phantomjs.exe")
                    browser.get(self.next_chap)
                    html = browser.page_source
                    
                    chap_soup = BeautifulSoup(html, 'html.parser')
                    
                    title_text = str(chap_soup.find("h3").get_text())
                    chap = str(chap_soup.find(id="chapt-content"))
                
                    next_button = chap_soup.find(class_="mybutton btnNext")
                    if(next_button==None):
                        self.has_next_chapter = 0
                        break
                    
                    self.next_chap = str(next_button["href"])
                
                #falun
                elif(self.w==4):
                    prefix = r"https://vi.falundafa.org/book/zfl_html/"
                    self.next_chap = prefix + self.next_chap
                    print(self.next_chap)
                    chap_page = requests.get(self.next_chap,verify=False)
                    chap_soup = BeautifulSoup(chap_page.content, 'html.parser')
                    
                    title_text = str(chap_soup.find("h2").get_text())
                    chap = ""
                    parts = chap_soup.find_all("p")
                    for p in parts:
                        chap = chap + p.get_text()
                    
                    buttons = chap_soup.find_all("img")
                    
                    for i,button in enumerate(buttons):
                        if "right" not in str(button):
                            if i == len(buttons)-1:
                                self.has_next_chapter = 0
                        else:
                            self.next_chap = button.parent["href"]
                            break
                            
                    
                file_name = "Text/C"+str(chapter)+".html" 
                
                html = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'+ '\n' 
                html =  html + '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN' +'\n' 
                html =  html + '  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' +'\n' 
                html =  html + '<html xmlns="http://www.w3.org/1999/xhtml">' +'\n' 
                html =  html + '  <head>' +'\n' 
                html =  html + '    <title>' + title_text + '</title>' + '\n' 
                html =  html + '    <link href="../stylesheet.css" rel="stylesheet" type="text/css" />' + '\n' 
                html =  html + '    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />' + '\n' 
                html =  html + '  </head>' + '\n' 
                html =  html + '  <body>' + '\n' 
                #html =  html + '    <div class="header">'+novel_name+'</div>' +'\n' 
                html =  html + '    <h4 id="C'+str(chapter)+'">'+title_text+'</h4>' +'\n' +'\n' +'\n'
                html =  html + '    ' + chap +'\n' 
                html =  html + '  </body>' +'\n' 
                html =  html + '</html>'
                        
                mucluc_html = mucluc_html + self.mucluc(str(chapter),title_text)
                toc = toc + self.toc_file(str(chapter),title_text)
                opf_item = opf_item + self.content_opf_item(str(chapter))
                opf_ref = opf_ref + self.content_opf_ref(str(chapter))
                opf = opf_item
                opf = opf + '\n'+'    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
                opf = opf + '\n'+'    <item id="stylesheet.css" href="stylesheet.css" media-type="text/css"/>'
                opf = opf + '\n'+'    <item id="cover" href="cover.jpg" media-type="image/jpeg"/>'
                opf = opf + '\n'+'  </manifest>'
                opf = opf + '\n'+'  <spine toc="ncx">'
                opf = opf + '\n'+'    <itemref idref="mucluc"/>'
                opf = opf + opf_ref
                
                
                #luu file html
                with open(new_dir + file_name, encoding='utf-8',mode ="w") as file:
                    file.write(html)
                
                chapter = chapter + 1
            
            #luu file content.opf
            with open(new_dir + 'content.opf', encoding='utf-8',mode ="w") as file:
                file.write(self.content_opf_def(novel_name) + opf)
                file.writelines('\n'+'  </spine>'+'\n')
                file.writelines('  <guide>'+'\n')
                file.writelines('  </guide>'+'\n')
                file.writelines('</package>')

            #luu file toc.ncx
            with open(new_dir + 'toc.ncx', encoding='utf-8',mode ="w") as file:
                file.write(self.toc_prefix_def(novel_name) + toc)
                file.writelines('  </navMap>' + "\n")
                file.writelines('</ncx>')

            #luu file mucluc.html
            with open(new_dir + "Text/mucluc.html", encoding='utf-8',mode ="w") as file:
                file.write(self.mucluc_prefix_def(novel_name) + mucluc_html)
                file.writelines("  </body>\n")
                file.writelines("</html>\n")
            
            #write file ko thay doi gi
            with open(new_dir + 'mimetype',mode ="wb") as file:
                file.write(mimetype)
            
            with open(new_dir + 'stylesheet.css',mode ="wb") as file:
                file.write(css)
        
            with open(new_dir + 'META-INF/container.xml', mode ="wb") as file:
                file.write(container)
            
            with open(new_dir + 'cover.jpg', mode = "wb") as file:
                file.write(cover_img)
            
            print("DONE!")
        
       
        