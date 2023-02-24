'''
やったこと
同名かつ位置が同じ駅を削除
同名かつ位置が異なる駅には都道府県を追加

やっていないこと
全く同じ駅だが大きい駅だったり別会社のがいっぱいあったりしてホームが遠すぎて別の座標が登録されている駅の区別
同一都道府県の同名の駅だが位置が異なる駅の区別
'''
import numpy as np
from collections import  defaultdict
data = np.loadtxt('station20230105free.csv', dtype=str, delimiter = ',', skiprows = 1, encoding = 'utf8')
station_code = defaultdict(set)
station_name = set()
same_station_name = set()
kenmei = ["北海道", "青森", "岩手", "宮城", "秋田", "山形", "福島", "茨城", "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川", "新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜", "静岡", "愛知", "三重", "滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山", "鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川", "愛媛", "高知", "福岡", "佐賀", "長崎", "熊本", "大分", "宮崎", "鹿児島", "沖縄"]
ans = []
for line in data:
    # 全く同じ駅を削除(乗換可能な別名駅は分ける)
    if line[1] in station_code.keys():
        if not line[2] in station_code[line[1]]:
            station_code[line[1]].add(line[2])
            ans.append([line[i] for i in range(15)])
    else:
        station_code[line[1]].add(line[2])
        ans.append([line[i] for i in range(15)])

for line in ans:
    # 同じ駅名に都道府県追加
    if line[2] in station_name:
        same_station_name.add(line[2])
        line[2] = line[2] + "({})".format(kenmei[int(line[6]) - 1])

    else:
        station_name.add(line[2])
for line in ans: # 最初の駅だけ引っかからないので
    if line[2] in same_station_name and not '(' in line[2]:
        line[2] = line[2] + "({})".format(kenmei[int(line[6]) - 1])

# print(ans)
np.savetxt("station_list_kari.csv", ans, fmt='%s', delimiter=',', header='station_cd,station_g_cd,station_name,station_name_k,station_name_r,line_cd,pref_cd,post,address,lon,lat,open_ymd,close_ymd,e_status,e_sort', encoding='utf8')
# line[9], line[10]は緯度経度
