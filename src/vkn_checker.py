import numpy as np
import re

class VKN_Checker:
    @classmethod
    def validate_vkn(cls, vkn):
        if not (isinstance(vkn, int) or (isinstance(vkn, str) and vkn.isdecimal())):
            return False
        vkn_str = str(vkn)
        vkn = np.array(list(map(int,vkn_str)))
        
        if len(vkn) != 10:
            return False
        
        reverse_indices = 9 - np.arange(9)
        tmp1 = (vkn[:9] + reverse_indices) % 10
        tmp2 = (tmp1 * (2 ** reverse_indices)) % 9
        
        for i in range(9):
            if tmp1[i] != 0 and tmp2[i] == 0:
                tmp2[i] = 9
        
        total = np.sum(tmp2)
        
        if total % 10 == 0:
            check_num = 0
        else:
            check_num = 10 - (total % 10)

        return vkn[9] == check_num

    @classmethod
    def find_vkn(cls, text):
        vkn_list = []
        for regex_result in re.findall(r"\d{10}", text):
            if cls.validate_vkn(regex_result):
                vkn_list.append(regex_result)
        return vkn_list
