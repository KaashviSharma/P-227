import json
import csv
data_from_csv = []
with open("data_set.txt",'r')as f:
	data_from_text = json.loads(f.read())
fn = ["brake","hand_brake","throttle","steer"]
csvfilestore = open("project227.csv",'w',newline = "")
writer = csv.DictWriter(csvfilestore,fieldnames = fn)
writer.writeheader()
writer.writerows(data_from_text)
with open("project227.csv","r")as file:
	reader = csv.reader(file)
	for row in reader:
		data_from_csv.append(row)
print(data_from_csv)