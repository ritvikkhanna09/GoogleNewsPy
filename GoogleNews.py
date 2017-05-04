from bs4 import BeautifulSoup
import mechanize
import urllib
def main():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    url = "http://news.google.co.in"
    page = br.open(url)
    html = page.read()	
    soup = BeautifulSoup( html,"html.parser")
    
    for text in soup.findAll('span'):
        print(text)
        if text.has_attr('class') and text['class'] == ['titletext']:
            print ("->")
            print (text.contents[0])
			
if __name__=="__main__":
	main()	
