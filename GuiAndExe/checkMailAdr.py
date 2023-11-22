#-*- coding:utf-8 -*-
import re

def check_address(input_address):
    search_str = '.*@.*jp'
    ret = bool(re.search(search_str,input_address))
    return ret

def check_address_vec(input_address_vec):
    search_str = '.*@.*jp'
    # ind = list(map(lambda x: bool(re.search(search_str,x)), input_address_vec))
    # ind = list(filter(lambda x: bool(re.search(search_str,x)), input_address_vec))
    ret = list(filter(lambda x: bool(re.search(search_str,x)), input_address_vec))
    return ret
    # data1 = [1, 3, 6, 50, 5]
    # data2 = map(lambda x: x * 2, data1)
    # return list(data2)

    

if __name__ == '__main__':
    print(check_address("xxx"))
    print(check_address("mm@da"))
    print(check_address("mm@da.jp"))
    print(check_address("mda.jp"))
    if (check_address("mm@da.")):
        print("True!")
    else:
        print("false")
    print("-------------------------")
    input = ["daxd","asejoi@d.se.jp","","saei@se","ss@ss.jp"]
    print(check_address_vec(input))