import requests
from bs4 import BeautifulSoup

def getJobs(keyword):

	# first, we need an empty list to store jobs
	data = []

	# set URL -> send request -> take response -> parse
	url = f"https://relocate.me/search?query={keyword}"
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	# relocate has pages, we should get every page
	lastPage = int(soup.find("span", {"class":"pages"}).findAll("span")[-1].get_text())
	for _ in range(1, lastPage+1):
		res = requests.get(f"https://relocate.me/search?query=python&page={_}")
		soup = BeautifulSoup(res.text, "html.parser")
		jobsList = soup.find("div", {"class":"jobs-list"}).find("div").findAll("div", {"class":"jobs-list__job"})
		for job in jobsList:
			company = job.find("div", {"class":"job__info"}).find("div", {"class":"job__company"}).get_text().strip()
			title = job.find("div", {"class":"job__title"}).find("b").get_text()
			apply = "https://relocate.me"+job.find("div", {"class":"job__title"}).find("a")["href"]
			data.append(
				{
					"company":company,
					"title":title,
					"apply":apply
				})

	# end of the function, we should return data
	return data