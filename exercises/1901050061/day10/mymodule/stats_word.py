# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:58:18 2019
@author: PetalSaya
test by jiangzhenye 20190509
"""

import operator
import re
from collections import Counter 
import jieba

count = int()

def stats_text_en(text,count):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    Step1 = re.sub("[\u4e00-\u9fa5，。：？！「」、]","",text.strip())
    #Step1 deletes the non-word character
    Step2 = dict()   #Step2 creates the empty dictionary 
    Step3 = Step1.split()   #Step3 splits each word in text into a single unit 
    print (collections.Counter(Step3).most_common(count))

'''
    for word in Step3:   #for...in loop counts the unit and records into the dictionary
        if word in Step2:
            Step2[word] += 1  
        else:
            Step2[word] = 1   #New word counts for one
    Step4 = sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each word appealed in the text
    print (Step4)   # Print result
'''
    

def stats_text_cn(text,count):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    #Step1 = ''.join(re.findall(u'[\u4e00-\u9fa5]+',text))
    #Step2 = dict()   #Step2 creates the empty dictionary 
    #Step3 = range(len(Step1))  #Step3 gives each cn word a position 
    text = re.sub('[^\u4e00-\u9fa5]','',text) #[^\u4e00-\u9fa5]表示所有非中文
    
    seg_list = jieba.lcut(text, cut_all=False)
    seg_dic = dict([(word,seg_list.count(word)) for word in seg_list if len(word)>=2])  # /// day10 /// 遍历seg_list，生成词典seg_dic，该词典的”key“长度均 >=2
    c = Counter(seg_dic)                                                               # /// day10 /// 创建计数器 c
    stats = dict(c.most_common(count))                                                 # /// day9 ///  返回一个列表stats，该列表包含了count个最常见元素和它们对应的值
    
    print(stats)
    #print (collections.Counter(seg_dic).most_common(count))
    
    
'''
    for word in Step3:   #for...in loop counts the cn word and records into the dictionary
        if Step2.get(Step1[word]):   #get() the cn word from each position #  
            Step2[Step1[word]] += 1  
        else:
            Step2[Step1[word]] = 1   #New cn word counts for one
    Step4 = sorted(Step2.items(),key=operator.itemgetter(1),reverse=False)
    # operator modulate helps rank the # of times of each cn word appealed in the text
    print (Step4)   # Print result
'''
    

def stats_text(text,count):
    if type(text) != str:
        raise ValueError("Input needs to be a string.")
    stats_text_en(text,count)
    stats_text_cn(text,count)