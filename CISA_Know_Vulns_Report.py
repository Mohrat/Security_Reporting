// This program fetches known exploited vulnerabilities data published by CISA and converts that to CSV
// Learning goals: Request URL, fetch and parsing JSON data, and storing as a CSV file

from urllib.request import urlopen
import csv
import json
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
response = urlopen(url)
data_json = json.loads(response.read())
vulnerabilities_data = data_json['vulnerabilities']
data_file = open("C:\\Users\\moha\\Downloads\\CISA_Vulnerability_Data_"+timestr+".csv", 'w', newline='')
//Change file path accordingly
csv_writer = csv.writer(data_file)
count = 0
 
for vul in vulnerabilities_data:
    if count == 0:
        header = vul.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(vul.values())
    
data_file.close()
