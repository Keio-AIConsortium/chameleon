# 都道府県名をつけたうえで重複している駅名を発見し手動で修正
import numpy as np
data = np.loadtxt('station_list_kari3.csv', dtype=str, delimiter=',', skiprows=1, encoding='utf8')
a = set()
for line in data:
    if line[2] in a:
        print(line[2])
    else:
        a.add(line[2])