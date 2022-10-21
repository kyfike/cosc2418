## Ky Fike, 1 Oct 2022
## 

# data: fish_code, species, site, date (mm/dd/yy), weight (g), fork length (cm)
# iso: fish_code, del13C, std err, del15N, std err

import sqlite3
# create empty database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

##### FIRST TABLE
cur.execute('DROP TABLE IF EXISTS fish_data')
cur.execute('CREATE TABLE fish_data (fish_code TEXT, species TEXT, site TEXT, date TEXT, weight FLOAT, fork_length FLOAT)')

import csv  # to read in a csv file
# open file here
fhand = open('Fish_data.csv')
i = 0
for line in fhand:
    if i != 0: # we don't want to read in the first line!
        c = list(line.split(','))
        cur.execute('INSERT INTO fish_data (fish_code, species, site, date, weight, fork_length) VALUES (?, ?, ?, ?, ?, ?)', 
            (c[0], c[1], c[2], c[3], c[4], c[5]))
    i = 1
conn.commit()

# # TEST: print the first database
# print('fish_data:')
# cur.execute('SELECT fish_code, species, site, date, weight, fork_length FROM fish_data')
# for row in cur:
#      print(row)


##### SECOND TABLE
cur.execute('DROP TABLE IF EXISTS fish_isotopes')
cur.execute('CREATE TABLE fish_isotopes (fish_code TEXT, del13C FLOAT, std_err13 FLOAT, del15N FLOAT, std_err15 FLOAT)')

fhand = open('Fish_isotopes.csv')
i = 0
for line in fhand:
    if i != 0: # we don't want to read in the first line!
        c = list(line.split(','))
        cur.execute('INSERT INTO fish_isotopes (fish_code, del13C, std_err13, del15N, std_err15) VALUES (?, ?, ?, ?, ?)', 
            (c[0], c[1], c[2], c[3], c[4]))
    i = 1
conn.commit()

# # TEST: print the second database
# print('fish_isotopes:')
# cur.execute('SELECT fish_code, del13C, std_err13, del15N, std_err15 FROM fish_isotopes')
# for row in cur:
#      print(row)

# query with JOIN: fish data from both tables, when fish weight is between 4 and 5 (g)
cur.execute('SELECT * FROM fish_data d LEFT JOIN fish_isotopes i ON d.fish_code = i.fish_code WHERE d.weight < 5 AND d.weight > 4')
for row in cur:
     print(row)

# query 2: date fish was measured, ordered by date
cur.execute('SELECT date, fish_code, species FROM fish_data ORDER BY date ASC')
for row in cur:
     print(row)

# query 3: total how many measurements there are of each species
cur.execute('SELECT species, COUNT(*) FROM fish_data GROUP BY species')
for row in cur:
     print(row)