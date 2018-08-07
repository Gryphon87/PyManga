from WebScraper import simple_get
from bs4 import BeautifulSoup

urlList = ["goblin_slayer", "neet_dakedo_hello_work_ni_ittara_isekai_ni_tsuretekareta"]

for url in urlList:
	raw_html = simple_get('http://mangakakalot.com/manga/' + url)
	html = BeautifulSoup(raw_html, 'html.parser').encode("ascii")


	if len(html) > 0: 
		print ("Pagina " + url + " trovata")
	f = open("./files/"+ url[:5] + ".html", "w+")
	f.write(str(html))
	f.close()

	print ("File " + url + " scritto")

