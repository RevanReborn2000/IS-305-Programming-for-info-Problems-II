from pathlib import *
import csv
with open('pokemon_names_and_descriptions (1).csv', 'r') as filein:
          csvin = csv.reader(filein)
          headers = next (csvin)
          data = [row for row in csvin]
        
# extra data-cleaning function that was asked for
def checkNum(stringval):
    if stringval.isnumeric() is not True:
        return False

for row in list(data):
    #print(row)
    description = row[2]
    name = row[1]
    number = row[0]
    if len(name.strip()) == 0 or checkNum(number) == False:
        data.remove(row)
        
datafolder = Path('description_text')

if not datafolder.exists():
    datafolder.mkdir()
        
for pokemon in data:
    outfile = datafolder / Path(str(pokemon[0]).zfill(3) + "-" + pokemon[1] + ".txt")
    outfile.write_text(pokemon[2])
   