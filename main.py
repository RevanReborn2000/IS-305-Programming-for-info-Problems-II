
#Load data and import dataset (Step 0)
import csv
import pathlib

infile = open('pokemon_names_and_descriptions (1).csv', 'r',  encoding='utf-8')
csvin = csv.reader(infile)
headers = next(csvin)
data = []
for row in csvin:
    data.append(row)


#Step 1
no_names = []
for index, row in enumerate(data):
    if row[1] == "":
        no_names.append(index)

#print(no_names)
#print(len(no_names))


#Step 2
main = []
list = []
for index, row in enumerate(data):
    if row[1] == "":
        list.append(index)
        if data[index + 1][1] != "":
            main.append(list)
            list = []

#print(main)


#Step 3

main2 = []
list2 = []
for index, row in enumerate(data):
    if row[1] == "":
        list2.append(index)
        if data[index + 1][1] != "":
            list2.insert(0, list2[0] - 1)
            main2.append(list2)
            list2 = []


#print(main2)


#Step 4

results = []
for i in main2:
    results.append([(data[x][0],data[x][1]) for x in i])
    #print(results)


#EZ PZ!


#Step 5: These instructions were very confusing. I did the first part of the
#required instructions and then solved the problem with my own solution.
chunk_list = []
for i in results:
    true_val = i[0]
    chunk_list.append(true_val)

for row in range(len(data)):
    if data[row][1] == "" and data[row][0] == "":
        data[row][1] = data[row - 1][1]
        data[row][0] = data[row - 1][0]


#Step 5 test code, everything checks out!
results2 = []
for i in main2:
    results2.append([(data[x][0], data[x][1]) for x in i])

#print(results2) uncommment this to see if test "passed"

#Step 6

outfile = open(pathlib.Path('updated_pokemon_names_and_descriptions.csv'), 'w', encoding='utf-8')
csvout = csv.writer(outfile)

csvout.writerow(headers)  # note the singular name here
csvout.writerows(data)  # your 2D list goes here
outfile.close()
