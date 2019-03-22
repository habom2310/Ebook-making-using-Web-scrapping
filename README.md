# Ebook-making-using-Web-scrapping
## _Make your own favourite ebooks. Why not?_

![Alt text](https://github.com/habom2310/Ebook-making-using-Web-scrapping/blob/master/result.PNG)

_It looks ordinary, but it works_

# Abstract
- I am a book worm. I read a lot of novels but sometimes, I only can read in websites, e.g truyenfull.vn, tangthuvien.vn. Reading in the website can be corrupted sometimes due to unstable internet (which happens quite often) and it hurts my eyes when I look into the screen for so long. Therefore I bought a Kindle. The only problem is ebooks. That's why I make this application (basically, every idea is based on your truly demand).

# Method
1. Scrape every chapter of the novel from the website.
   - You will need some knowledge of this package if you want to scrape your own need. Have a look at https://www.dataquest.io/blog/web-scraping-tutorial-python/.
2. Secondly, build the ebook file.
   - Ebook file is a zip file, which contains multiples files in it. To understand how is an ebook file, have a look at https://www.lifewire.com/create-epub-file-from-html-and-xml-3467282.
   
# Requirements
- python 3.5
- BeautifulSoup (for web scrapping)

# Implementation
- run `main.py`
- replace `cover.jpg` by any other cover image that you want. Remember to keep the file name as `cover.jpg`.
# Result
- For my own use, the application can make ebook file from 2 websites: truyenfull.vn and tangthuvien.vn, they all are Vietnamese websites for reading novels. You just need to enter the link of the novel, press start, wait and you will have a DIY ebook.

# TODO
- If you want to scrape from somewhere else, you need to examine the construct of the site (if you use Chrome, F12 to enter developer mode and find where the data is). It requires you some knowledge about html but don't worry, you have Google by your side :).
- Inform me if you have any problem running the code.
- Any related idea is welcome at khanhhanguyen2310@gmail.com.
