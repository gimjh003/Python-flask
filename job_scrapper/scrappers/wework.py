import requests
from bs4 import BeautifulSoup

def getJobs(keyword):

	# first, we need an empty list to store jobs
	data = []

	# set URL -> send request -> take response -> parse
	url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "html.parser")

	# find jobs categories and find all jobs of each section
	jobsContainer = soup.find("div", {"class":"jobs-container"})
	jobsCategories = jobsContainer.findAll("section", {"class":"jobs"})
	for jobsCategory in jobsCategories:
		sectionJobs = jobsCategory.findAll("li")[:-2]
		for sectionJob in sectionJobs:
			jobData = sectionJob.findAll("a")[-1]
			company = jobData.find("span", {"class":"company"})
			title = jobData.find("span", {"class":"title"})
			apply = "https://weworkremotely.com"+jobData["href"]
			try:
				data.append(
					{
						"company":company.get_text(),
						"title":title.get_text(),
						"apply":apply
					})
			except: pass
				
	# end of the function, we should return data
	return data