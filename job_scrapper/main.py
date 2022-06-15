from flask import Flask, render_template, request, redirect, send_file
from scrappers import wework, relocate, remoteok
import csv

# APP, DB set
app = Flask(__name__)
fakeDB = {}

# get Jobs
def getJobs(query):
    wework_data = wework.getJobs(query)
    relocate_data = relocate.getJobs(query)
    remoteok_data = remoteok.getJobs(query)
    data = wework_data+relocate_data+remoteok_data
    fakeDB[query] = data
    with open(f"job_scrapper/{query}.csv", mode="w") as file:
        pen = csv.writer(file)
        pen.writerow(["Title", "Company", "Apply"])
        for info in data:
            pen.writerow([info.get("title"), info.get("company"), info.get("apply")])

# root route should render index.html
@app.route("/")
def home():
    return render_template("index.html")

# search route should render search.html with job data
@app.route("/search")
def search():
    query = request.args.get("query")
    if query:
        query = query.lower()
        try:
            if fakeDB.get(query):
                pass
            else:
                getJobs(query)
        except: redirect("/")
    else:
        return redirect("/")
    return render_template("search.html", query=query, data=fakeDB[query])
	
# download job data if it exists
@app.route("/download")
def download():
    query = request.args.get("query")
    if query:
        data = fakeDB.get(query)
        if data:
            return send_file(f"{query}.csv")
        else: return redirect("/")
    else: return redirect("/")

if __name__=="__main__":
    app.run()