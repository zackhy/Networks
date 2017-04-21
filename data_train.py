"""
This program splits the data into train data and test data
Author: Haoyou Liu
"""

import csv
import json
import random

with open('artists_users_playcount.txt', encoding='utf-8') as inf, \
    open('train_data.csv', 'w', newline='', encoding='utf-8') as outf:
    outcsv = csv.writer(outf)
    outcsv.writerow(['artists', 'users', 'playcount', 'ratio'])

    random_artist = {}
    for line in inf:
        line = line.strip()
        js = json.loads(line)
        flag = True
        for user, artist in js.items():
            if len(artist) < 10:
                continue
            if flag:
                random_artist[user] = random.choice(list(artist.keys()))
                flag = False
            tot_playcount = sum({int(x) for y, x in artist.items() if int(x) > 50 and y != random_artist[user]})
            if tot_playcount == 0:
                del random_artist[user]
                continue
            for key, value in artist.items():
                if int(value) < 50:
                    continue
                ratio = int(value)/tot_playcount
                flag = False
                if key != random_artist[user]:
                    outcsv.writerow([key] + [user] + [value] + [ratio])

with open('test_data.csv', 'w', newline='', encoding='utf-8') as ouf:
    outcsv = csv.writer(ouf)
    outcsv.writerow(['user', 'artist'])

    for key, value in random_artist.items():
        outcsv.writerow([key] + [value])
