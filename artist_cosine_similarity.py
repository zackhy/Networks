"""
This program calculates the cosine similarity between artists
Author: Haoyou Liu
"""

import csv
import math

def cosine_data(ratio):
    with open('train_data.csv', encoding='utf-8') as inf:
        incsv = csv.reader(inf)
        next(incsv)

        user_dic = {}
        artist_dic = {}
        count = 1

        for line in incsv:
            try:
                if float(line[3]) < ratio:
                    continue
            except:
                pass
            if line[0] in artist_dic:
                if line[1] in user_dic:
                    artist_dic[line[0]][user_dic[line[1]]] = line[3]
                else:
                    artist_dic[line[0]][count] = line[3]
            else:
                artist_dic[line[0]] = {}
                if line[1] in user_dic:
                    artist_dic[line[0]][user_dic[line[1]]] = line[3]
                else:
                    artist_dic[line[0]][count] = line[3]

            if line[1] not in user_dic:
                user_dic[line[1]] = count
                count += 1

    return artist_dic

with open('train_cosine_similarity.csv', 'w', newline='', encoding='utf-8') as outf:
    outcsv = csv.writer(outf)
    outcsv.writerow(['artist1', 'artist2', 'cosine similarity'])

    artist_dic = cosine_data(0.1)

    for art1 in artist_dic.keys():
        art1_dict = artist_dic[art1]
        denom_art1 = 0
        for user in art1_dict.keys():
            denom_art1 = denom_art1 + float(art1_dict[user])*float(art1_dict[user])

        for art2 in artist_dic.keys():
            numerator = 0
            denominator = 0
            art2_dict = artist_dic[art2]

            denom_art2 = 0
            for user in art2_dict.keys():
                denom_art2 = denom_art2 + float(art2_dict[user])*float(art2_dict[user])

                if user in art1_dict.keys():
                    numerator = numerator + float(art1_dict[user])*float(art2_dict[user])

            denominator = math.sqrt(denom_art1)*math.sqrt(denom_art2)
            cosine = numerator / denominator
            outcsv.writerow([art1] + [art2] + [cosine])
