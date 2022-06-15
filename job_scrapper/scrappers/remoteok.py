import requests
from bs4 import BeautifulSoup

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
headers = {"User-Agent":userAgent}

def getJobs(keyword):

	# first, we need an empty list to store jobs
	data = []

	# set URL -> send request -> take response -> parse
	url = f"https://remoteok.com/{keyword}"
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, "html.parser")
	jobsBoard = soup.find("div", {"class":"container"}).find("table")
	jobs = jobsBoard.findAll("tr")
	for job in jobs:
		try:
			company = job.find("span", {"class":"companyLink"}).get_text().strip()
			title = job.find("h2").get_text().strip()
			apply = "https://remoteok.com"+job.find("a")["href"]
			data.append(
				{
					"company":company,
					"title":title,
					"apply":apply
				})
		except: pass
	# end of the function, we should return data
	return data