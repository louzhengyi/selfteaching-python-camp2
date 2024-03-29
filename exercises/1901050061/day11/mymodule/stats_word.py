# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:58:18 2019
@author: PetalSaya
test by jiangzhenye 20190516
"""

import collections
import re
import jieba

def stats_text_en(text,input_num):
    if type(text) == str:
        Step1 = re.sub("u'[A-Za-z]","",text)
        Step2 = Step1.split()
        Step3 = collections.Counter(Step2).most_common(input_num)
        print (Step3)
    else:   
        raise ValueError("Input needs to be a string.")

def stats_text_cn(text,input_num):
    if type(text) == str:
        Step1 = re.findall(u'[\u4e00-\u9fff]+',text)
        Step2 = str(Step1)
        Step3 = jieba.cut(Step2,cut_all=True)
        new_list = []
        for word in Step3:
            if len(word) >= 2:
                new_list.append(word)
        Step4 = collections.Counter(new_list).most_common(input_num)
        Step5 = str(Step4)
        print (Step5)
    else:   
        raise ValueError("Input needs to be a string.")

def stats_text(text,input_num):
    if type(text) == str:
        return (stats_text_en(text,input_num)+stats_text_cn(text,input_num))
    else:    
        raise ValueError("Input needs to be a string.")