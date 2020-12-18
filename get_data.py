#API_get.pyのファイルのデータをすべて読み込む
import API_get
import json

def fromJSON():
    with open("result.json", "r") as f2:
        res_data = json.load(f2)
        return res_data["json"][0]

def main():
    # トークン取得
    # token = API_get.get_token()
    # # print(token)
    # # token = ""
    
    # # 水温取得
    # res_data = API_get.get_water(token)
    # water = API_get.get_water(token)
    # api叩きすぎない様に ロード
    f2 = open("result.json", "r")
    res_data = json.load(f2)
    # values = [v for k, v in res_data.items() if k == 'json']

    # for key,value in res_data.items(): 
    #     for v in res_data['json']:
    #         for v_key in v.keys():
    #             # print(f'key:{v_key}  　value:{v[v_key]}')
    #               print(f"{v_key}は{v[v_key}です")
    #               print(res_data["json"][0])
    print(res_data["json"][0])
    f2.close()

if __name__ == '__main__':
    main()