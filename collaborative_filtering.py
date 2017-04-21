"""
This program calculates the cosine similarity between users in order to implement collaborative filtering
Author: Haoyou Liu
"""

import csv
import numpy
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine

user = []
artists = []
train_data = []
with open('train_data.csv') as inf:
    incsv = csv.reader(inf)
    next(incsv)

    for line in incsv:
        if line[0] in artists:
            continue
        else:
            artists.append(line[0])

count = 0
with open('train_data.csv') as inf:
    incsv = csv.reader(inf)
    next(incsv)

    temp = [0]*len(artists)
    for line in incsv:
        if line[1] in user:
            index = artists.index(line[0])
            temp[index] = float(line[3])
        else:
            if temp != [0]*len(artists):
                train_data.append(temp)
            user.append(line[1])
            temp = [0]*len(artists)
            index = artists.index(line[0])
            temp[index] = float(line[3])
            count += 1

        if count == 5001:
            break


cos_sim = 1 - pairwise_distances(train_data, metric='cosine')

with open('user_sim.csv', 'wb') as outf:
    outcsv = csv.writer(outf)

    outcsv.writerow(['user1', 'user2', 'cosine'])

    for i in range(len(user) - 1):
        for j in range(len(user) - 1):
            if i == j:
                continue
            outcsv.writerow([user[i]]+[user[j]]+[cos_sim[i][j]])
