# 駅名と緯度経度のみ残す
import numpy as np
data = np.loadtxt('station_list_kari3.csv', dtype=str, delimiter=',', skiprows=1, encoding='utf8')
ans = []
for line in data:
    ans.append([line[2], line[9], line[10]])
np.savetxt("station_list_20230301.csv", ans, fmt='%s', delimiter=',', header='station_name,lon,lat', encoding='utf8')