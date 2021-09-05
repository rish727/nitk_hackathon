import re
import pprint
import requests
import json as js

import UnivScr.kyushu as kyushu
import UnivScr.kumamoto as kumamoto
import UnivScr.iwate as iwate
import UnivScr.kagawa as kagawa
import UnivScr.kochi as kochi
import UnivScr.miyazaki as miyazaki
import UnivScr.muroran as muroran
import UnivScr.nagasaki as nagasaki
import UnivScr.nagoya as nagoya
import UnivScr.oita as oita
#---
import UnivScr.hiroshima as hiroshima
import UnivScr.hokkaido as hokkaido
import UnivScr.kanazawa as kanazawa
#--
import UnivScr.kobe as kobe
import UnivScr.kyotoseni as kyotoseni
import UnivScr.nagasaki as nagasaki
#--
import UnivScr.nagoya as nagoya
import UnivScr.ryukyu as ryukyu
import UnivScr.shinshu as shinshu
#--
import UnivScr.tiba as tiba

univ_name = [
    'kyushu','kumamoto','iwate', 'kagawa',
    'kochi','miyazaki','muroran','nagoya','oita',
    'hiroshima', 'hokkaido','kanazawa',
    'kobe', 'kyotoseni', 'nagasaki',
    'nagoya','ryukyu', 'shinshu',
    'tiba'
    ]

univ_char = [
    '九州大学','熊本大学','岩手大学', '香川大学',
    '高知大学','宮崎大学','室蘭工業大学','名古屋大学','大分大学',
    '広島大学','北海道大学','金沢大学',
    '神戸大学', '京都工芸繊維大学','長崎大学',
    '名古屋大学', '琉球大学', '信州大学',
    '千葉大学'
]


# univ_name = [
#     'kyushu'
#     ]
num_info = 5


def call():
    for name in univ_name :
        print(name + '--------------')
        info, date , url= eval( name +'.get()')
        
        n = univ_name.index(name)

        #数字のみに正規化
        date = norm_dt(date)
        #info = norm_dt(info)


        #debag
        
        # num_infoの数のみ出力
        if ( len(info) > num_info -1 ) and ( len(date) > num_info -1 ) :
            for i in range(num_info):
                print(date[i] + ' : ' + info[i])
                print(url[i])
                db_upload(univ_char[n], date[i], info[i], url[i])
        else :
            for i in range(min( len(info), len(date))):
                print(date[i] + ' : ' + info[i])
                print(url[i])
                db_upload(univ_char[n], date[i], info[i], url[i])
        
        
def norm_dt(dt):
    num = []
    for d in dt:
        num += [re.sub(r"\D", "", d)]
    
    return num

def norm_info(info):
    txt = []
    pattern=r"\s+"
    for i in info:
        print(i)
        txt += [re.sub(pattern, "", i)]
        
    return txt

def db_upload(db_name, db_date, db_info, db_url):
    # print(type(db_name))
    # print(type(db_date))
    #POSTパラメータは二つ目の引数に辞書で指定する
    response = requests.post(
        'https://1ff5-240f-c1-bd4e-1-983c-767a-bedb-1253.ngrok.io/update',
            data = js.dumps(
                {
                    "name" : db_name,
                    "date" : db_date,
                    "information" : db_info,
                    "url" : db_url
                }
            )
        )
    #レスポンスオブジェクトのjsonメソッドを使うと、
    #JSONデータをPythonの辞書オブジェクトに変換して取得できる
    # pprint.pprint(response.json())
    print(response.status_code)

if __name__ == '__main__':
    call()
    
    
    