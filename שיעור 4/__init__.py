import  csv
from os import write
import json

# תרגיל 1
with open('cou.txt', 'r',encoding="utf-8") as file:
    content = file.read()
    count = content.count(" ")
    print(count + 1 )

# תרגיל 2
def write_in_csv_file(first_name, last_name, age, address):
   with open("people.csv" ,"w" , newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["firsName" , "lastName" , "Age" , "address"])
        writer.writerow([first_name, last_name, age, address])

write_in_csv_file("John", "Smith", 22, "haifa")

# תרגיל 3
def write_in_json_file(first_name, last_name, age, address):
    data = {"first_name": first_name, "last_name": last_name, "age": age, "address": address}
    with open("data.json" ,"w" , newline="") as file2:
        json.dump(data, file2)

    with open("data.json" ,"r" , newline="") as file3:
        data = json.load(file3)
        print(data)

write_in_json_file("John", "Smith", 22, "haifa")