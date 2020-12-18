import requests
import json
# import numpy as np
# from io import BytesIO


# トークンの取得
def get_token():
    url = "https://umilog.cloud/web/api/authenticate"
    headers = {'Content-Type': 'application/json'}
    data={"username":"09099999999","password":"09099999999"}
    res = requests.post(url, headers=headers, json=data)
    return res.json()["token"]


# 水温の取得
def get_water(token):
    device_id = 3014
    sensor_grp = "water"
    sensor_key = "top"
    # eqgreat = "2020-11-27%2011:11"
    # eqsamll = "2020-11-27%2015:00"
    eqgreat = "2020-12-11%2012:00"
    eqsamll = "2020-12-11%2016:00"

    url = f"https://umilog.cloud/web/api/sensor_logs?device_id={device_id}&sensor_grp={sensor_grp}&sensor_key={sensor_key}&arrived_at[EQGREAT]={eqgreat}&arrived_at[EQSMALL]={eqsamll}"
    headers = {'Authorization': "Bearer " + token}

    res = requests.get(url, headers=headers)

    return res.json()





def main():

    # # トークン取得
    # token = get_token()
    # # print(token)
    # # token = ""
    
    # # 水温取得
    # res_data = get_water(token)

    # # APIに接続しすぎないように保存する
    # with open("result.json", "w") as f:
    #     json.dump(res_data, f, ensure_ascii=False, indent=4)
    
    # api叩きすぎない様に ロード
    f2 = open("result.json", "r")
    res_data = json.load(f2)
    f2.close()

    print(f"データ\n{res_data}")


if __name__ == '__main__':
    main()