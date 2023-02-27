# 新しい駅名リスト1が出たら実行(動作は未確認)
import numpy as np
# 新ファイル
new_data = np.loadtxt('station_list_kari.csv', dtype=str, delimiter=',', skiprows=1, encoding='utf8')
# 旧ファイル
old_data = np.loadtxt('station_list_kari.csv', dtype=str, delimiter=',', skiprows=1, encoding='utf8')

new_station1 = set()
old_station1 = set()
new_station2 = set()
old_station2 = set()
for new_line in new_data:
    if new_line[13] == "2":
        new_station2.add(new_line[0])
    else:
        new_station1.add(new_line[0])
for old_line in old_data:
    if old_line[13] == "2":
        old_station2.add(old_line[0])
    else:
        old_station1.add(old_line[0])

print("#####新駅#####")
for i in new_station1.difference(old_station1):
    print(j[2] for j in new_data if j[0] == i)
print("#####廃駅#####")
for i in new_station2.difference(old_station2):
    print(j[2] for j in new_data if j[0] == i)