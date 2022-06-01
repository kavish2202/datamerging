import csv

dataset_1 = []
dataset_2 = []

with open ("final.csv","r") as f :
    csvreader = csv.reader(f)
    for row in csvreader :
        dataset_1.append(row)

with open ("archive_dataset_sorted1.csv","r") as f :
    csvreader = csv.reader(f)
    for row in csvreader :
        dataset_2.append(row)

headers_1 = dataset_1[0]
#print(headers_1)
headers_2 = dataset_2[0]
#print(headers_2)
headers = headers_1 + headers_2

planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]
planet_data = []
for index,data_row in enumerate(planet_data_1) :
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("merged_dataset.csv","a+") as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

with open("merged_dataset.csv") as input, open("merged_dataset1.csv", "w", newline = "" ) as output :
  writer = csv.writer(output)
  for row in csv.reader(input) :
    if any(field.strip() for field in row ) :
      writer.writerow(row)