#coding:utf-8
import re

"""
function match_location(location, rules):
    pass  # TODO: 根据 location 和 rules 返回匹配的 rule 的 index 或者 -1

# 输入举例
rules = [
    '= /foo',
    '/foo/bar',
    '~* \.(gif|jpg|jpeg)$',
]
location = '/foo'  # 函数返回 0
location = '/foo/bar  # 函数返回 1
location = '/foo/bar.jpg  # 函数返回 2
location = '/bar/foo'  # 函数返回 -1
"""

result=''
def match_location(localtion,rules):
    n1,n2,n3,n4,n5=[-1 for i in range(5)]
    for r in range(len(rules)):
        rulesSplit=rules[r].split(" ")
        reg=""
        if len(rulesSplit)==2:
            reg,rule=rulesSplit
        elif len(rulesSplit)==1:
            rule=rulesSplit[0]
            if rule=="/":
                reg="/"
        #非正则严格匹配 n1
        if reg=="=":
            if localtion == rule:
                n1=r
                break
        #精准最长前缀匹配 n2
        if reg=="" or reg=="^~":
            if rule == localtion[:len(rule)]:
                n2 = r
        #正则匹配 n3
        if reg=="~":
            result=re.search(re.compile(rule,re.S),localtion)
            if result:
                n3 = r
        #不区分大小写正则匹配 n4
        if reg=="~*":
            result = re.search(re.compile(rule, re.S), localtion.lower())
            if result:
                n4 = r
        #匹配所有请求 n5
        if reg=='/':
            n5=r

    #优先度排序为   非正则严格匹配 n1 > 精准最长前缀匹配 n2 > 正则匹配 n3 > 不区分大小写正则匹配 n4 > 匹配所有请求 n5 > 未成功匹配 -1
    if n1!=-1:
        return n1
    elif n2!=-1:
        return n2
    elif n3!=-1:
        return n3
    elif n4!=-1:
        return n4
    elif n5!=-1:
        return n5
    else:
        return -1

"""测试"""
if __name__=="__main__":
    rules = [
        '= /foo',                   #0
        '/foo/bar',                 #1
        '~* \.(gif|jpg|jpeg)$',     #2
        '~ /*/abc',                 #3
        '/',                        #4
        '= /login',                 #5
        '^~ /static/',              #6
        '~ \.(gif|jpg|png|js|css)$',#7
        '~* \.png$',                #8
        '= /'                       #9
    ]

    print(match_location('/foo/bar',rules))