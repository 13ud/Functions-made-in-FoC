import json

# serialise
with open('temp.json', 'w') as out:
    data = [(2, 'hello'), 'world', [1,2,3]]
    json.dump(data, out)


# deserialise, OPENING json file for reading
with open('temp.json', 'r') as ins:
    data = json.load(ins)
    print(data)



# writing to a file
FILENAME = 'file.txt'
text = open(FILENAME,'w')
text.write('Tim woz ere ')
text.close()

# Appending to a file
FILENAME = 'file.txt'
text = open(FILENAME, 'a')
text.write('Tim woz ere again ')
text.close()

# BETTER USING A GENERATOR
with open ('file.txt') as f:
    for line in f:
        print(line)



# Parsing CSV Files, csv.DictReader, Dictionary per row with Headers as keys
import csv
FNAME = 'rainfall.csv'
table = []
for line in csv.DictReader(open(FNAME)):
    table.append(line)
for row in table:
    print(row['city'], row['Dec'])


# List of Lists Parsing, csv.reader

import csv
FNAME = 'rainfall.csv'
table = []
for line in csv.reader(open(FNAME)):
    table.append(line)
print(table[-1][2])

table.pop(0) # to remove first row of values

