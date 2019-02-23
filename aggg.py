#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author: bkdp
# github项目地址：https://github.com/bkdp/aggg
# aggg项目，使用python爬取巨潮资讯网站里面沪深股市中某个指定股票的最新公告数据，然后将得到的公告数据以json格式保存到本地，交付后续的逻辑处理数据。

import requests
import re
import json

#根据需要修改，指定所爬取的公司
ggid = "600028" #这里指定股票代码
ggse = "sse" #指定市场：上海为:sse，深圳为:szse
#根据需要修改，指定保存文件和路径
ggjsonpath = "" #指定json文件的保存路径，不指定则保存在当前目录
ggjsonfile = ggjsonpath + ggid + ".json"


#爬取参数，默认无需修改
pppageSize = "31" #每页爬取的公告数量
ppshowTitle = ggid
ppurl = "http://www.cninfo.com.cn/new/hisAnnouncement/query" 

#以下为执行代码，默认无需修改
def mmparsejson(q):
    fname = ggjsonfile
    fx = open(fname,"w")
    p = re.compile('{.*?"announcementId":"(.*?)","announcementTitle":"(.*?)","announcementTime":(.*?),"adjunctUrl":"(.*?)","adjunctSize":(.*?),"adjunctType":"(.*?)","storageTime".*?null},',re.S)
    items = re.findall(p, q)
    for item in items:
        mmitem = {'ggid':item[0],'ggtitle':item[1],'ggdate':item[2],'ggurl':item[3],'ggtype':item[5],'ggsize':item[4]}
        jsonstr = json.dumps(mmitem,ensure_ascii=False)
        fx.write(jsonstr + ",")

def mmgetlist(mmpage):
    mmurl = ppurl
    mmformdata = {"stock":ggid,"searchkey":"","plate":"","category":"","trade":"","sortName":"","sortType":"","limit":"","showTitle":ppshowTitle,"seDate":"请选择日期","column":ggse,"tabName":"fulltext","pageNum":mmpage,"pageSize":pppageSize}
    mmheaders = {'content-type': "application/x-www-form-urlencoded; charset=UTF-8","Host":"www.cninfo.com.cn","Origin":"http://www.cninfo.com.cn","Referer":"http://www.cninfo.com.cn/cninfo-new/announcement/show", "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36","X-Requested-With":"XMLHttpRequest"}
    ggjson = requests.post(url = mmurl, data = mmformdata, headers = mmheaders).text
    print(ggjson)
    mmparsejson(ggjson)

mmgetlist(1)
#如果需要爬取多页数据，可指定页数循环爬取
#for mmpage in rang(1,5):
#    mmgetlist(mmpage)

# The end