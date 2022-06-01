import csv
data = []

with open ("archived_dataset.csv", "r") as f :
    csvreader = csv.reader(f)
    for row in csvreader :
        data.append(row)

headers = data[0]
planet_data = data[1:]
# converting all the planet names into lower case

for data_point in planet_data :
    print(data_point[0])
    data_point[0] = data_point[0].lower()
    data_point = "\n".join(data_point)

planet_data.sort(key = lambda planet_data : planet_data[0])


with open("archived_dataset_sorted.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
        
with open("archived_dataset_sorted.csv") as input, open("archived_dataset_sorted1.csv", "w", newline = "" ) as output :
  writer = csv.writer(output)
  for row in csv.reader(input) :
    if any(field.strip() for field in row ) :
      writer.writerow(row)