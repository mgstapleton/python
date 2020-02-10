import requests
import base64
import json

### Parameters ###
api_login = 'Michael.Stapleton' ###Username
api_password = 'pwd123'  ###password

###https://jira.cubictelecom.com/sr/jira.issueviews:searchrequest-csv-current-fields/12850/SearchRequest-12850.csv?jqlQuery=&tempMax=1000&pager/start=0
start = '0'
tempMax = '1000'
iterations = 100
base_url = "https://jira.cubictelecom.com/sr/jira.issueviews:searchrequest-csv-current-fields/12850/SearchRequest-12850.csv?jqlQuery=&tempMax=" + tempMax + "&pager/start=" + start
results_data = ""

print("Starting...")

#### FUNCTIONS ###
def getJiraData(base_url,api_login,api_password, start):
    base_url = 'https://jira.cubictelecom.com/sr/jira.issueviews:searchrequest-csv-current-fields/12850/SearchRequest-12850.csv?jqlQuery=&tempMax=' + tempMax + '&pager/start=' + str(start)
    print (base_url)
    r = requests.get(base_url, auth=(api_login, api_password))
    if r.ok:
        ###print (r.text)
        print ("Length of results data = " , len(r.text))
        if len(r.text) == 1:
            return 1
        f = open("jira_output.csv","a")
        print("Printing results to file")
        f.write(r.text)
        f.close()
        return 0
    else:
        print ("Error encountered: " , r.status_code)
        print (r.headers)
        ###print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))
        return 1
def main():
    iterator = 0
    x=0
    while iterator < 1:
        ###x = 0 to 5
        start = x * 1000
        print ("Iteration: " + str(x) + " starting from: " + str(start))
        iterator = getJiraData(base_url,api_login,api_password, start)
        x=x+1
    else:
        print ("Done")
main()
