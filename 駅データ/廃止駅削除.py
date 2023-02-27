# 廃止した駅を削除する
import numpy as np
data = np.loadtxt('station_list_kari2.csv', dtype=str, delimiter=',', skiprows=1, encoding='utf8')
ans = []
for line in data:
    if line[13] != "2":
        ans.append(line)
np.savetxt("station_list_kari3.csv", ans, fmt='%s', delimiter=',', header='station_cd,station_g_cd,station_name,station_name_k,station_name_r,line_cd,pref_cd,post,address,lon,lat,open_ymd,close_ymd,e_status,e_sort', encoding='utf8')