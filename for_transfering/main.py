import re

import UnivScr.kyushu as kyushu
import UnivScr.kumamoto as kumamoto

univ_name = ['kyushu','kumamoto']
num_info = 3

def call():
    for name in univ_name :
        print(name + '--------------')
        info, date , url= eval( name +'.get()')

        #数字のみに正規化
        date = norm_dt(date)
        #info = norm_dt(info)


        #debag
        
        # num_infoの数のみ出力
        if ( len(info) > num_info -1 ) and ( len(date) > num_info -1 ) :
            for i in range(num_info):
                print(date[i] + ' : ' + info[i])
                print(url[i])
        else :
            for i in range(min( len(info), len(date))):
                print(date[i] + ' : ' + info[i])
                print(url[i])
        
        
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

def upload():
    print()

if __name__ == '__main__':
    call();
    
    