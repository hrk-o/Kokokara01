#!/usr/bin/env python
# coding: utf-8

# In[1]:


#会社情報の抽出


# In[2]:


import requests
import json
import time
import csv


# In[3]:


def getData(location, offset, services):
    print(location, offset, services, end='')
    url = "https://u10sme-api.smrj.go.jp/v1/corporations.json?location="+location+"&offset="+offset+"&services="+services+"&limit=100"
    response = requests.get(url)
    jsonData = response.json()
    return jsonData


# In[4]:


def compList(dData):
    dlist = []
    try:
        dlist.append(dData['id'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['corporateNumber'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['uqOperatorCode'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['name'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['nameKana'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['location']['postalCode'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['location']['prefectureCode'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['location']['cityCode'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['location']['address'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['contact']['phoneNumber'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['contact']['faxNumber'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['contact']['email'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['affiliatedGroup'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['qualification'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['businessResults'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['profile'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['url'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['foundationDate'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['capital'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['numberOfEmployees'])
    except :
        dlist.append(None)
    try:
        dlist.append(dData['lastUpdateTime'])
    except :
        dlist.append(None)

    plist = [0]*47
    for bd in dData['businessAreas']:
        for pd in bd['prefectures']:
            plist[int(pd['code'])-1] = 1
    slist = [0]*237
    for bd in dData['serviceCategories']:
        for pd in bd['serviceKinds']:
            for sd in pd['services']:
                slist[int(sd['id'])-1] = 1
    dlist = dlist + plist + slist
    #print(dlist)
    return dlist


# In[5]:


url = "https://u10sme-api.smrj.go.jp/v1/areas.json"
response = requests.get(url)
jsonData = response.json()
areas = []#エリアコード、都道府県コード、都道府県名
for jsonObj in jsonData["areas"]:
    #print(jsonObj['id'])#areaコード
    for jsonObp in jsonObj['prefectures']:#都道府県コード
        #print(jsonObp['code'] , jsonObp['name'])
        areas.append([jsonObj['id'], jsonObp['code'], jsonObp['name']])
print(areas)


# In[6]:


f = open('./Kokokara_all.csv', 'w', encoding="utf_8_sig")
writer = csv.writer(f, lineterminator='\n')

corporations = []#エリアコード、都道府県コード、都道府県名
corlist = ['id', 'corporateNumber', 'uqOperatorCode', 'name', 'nameKana', 'location_postalCode','location_prefectureCode','location_cityCode', 'location_address','contact_phoneNumber', 'contact_faxNumber','contact_email','affiliatedGroup','qualification','businessResults','profile','url','foundationDate','capital','numberOfEmployees','lastUpdateTime','prefectures01','prefectures02','prefectures03','prefectures04','prefectures05','prefectures06','prefectures07','prefectures08','prefectures09','prefectures10','prefectures11','prefectures12','prefectures13','prefectures14','prefectures15','prefectures16','prefectures17','prefectures18','prefectures19','prefectures20','prefectures21','prefectures22','prefectures23','prefectures24','prefectures25','prefectures26','prefectures27','prefectures28','prefectures29','prefectures30','prefectures31','prefectures32','prefectures33','prefectures34','prefectures35','prefectures36','prefectures37','prefectures38','prefectures39','prefectures40','prefectures41','prefectures42','prefectures43','prefectures44','prefectures45','prefectures46','prefectures47','services01','services02','services03','services04','services05','services06','services07','services08','services09','services10','services11','services12','services13','services14','services15','services16','services17','services18','services19','services20','services21','services22','services23','services24','services25','services26','services27','services28','services29','services30','services31','services32','services33','services34','services35','services36','services37','services38','services39','services40','services41','services42','services43','services44','services45','services46','services47','services48','services49','services50','services51','services52','services53','services54','services55','services56','services57','services58','services59','services60','services61','services62','services63','services64','services65','services66','services67','services68','services69','services70','services71','services72','services73','services74','services75','services76','services77','services78','services79','services80','services81','services82','services83','services84','services85','services86','services87','services88','services89','services90','services91','services92','services93','services94','services95','services96','services97','services98','services99','services100','services101','services102','services103','services104','services105','services106','services107','services108','services109','services110','services111','services112','services113','services114','services115','services116','services117','services118','services119','services120','services121','services122','services123','services124','services125','services126','services127','services128','services129','services130','services131','services132','services133','services134','services135','services136','services137','services138','services139','services140','services141','services142','services143','services144','services145','services146','services147','services148','services149','services150','services151','services152','services153','services154','services155','services156','services157','services158','services159','services160','services161','services162','services163','services164','services165','services166','services167','services168','services169','services170','services171','services172','services173','services174','services175','services176','services177','services178','services179','services180','services181','services182','services183','services184','services185','services186','services187','services188','services189','services190','services191','services192','services193','services194','services195','services196','services197','services198','services199','services200','services201','services202','services203','services204','services205','services206','services207','services208','services209','services210','services211','services212','services213','services214','services215','services216','services217','services218','services219','services220','services221','services222','services223','services224','services225','services226','services227','services228','services229','services230','services231','services232','services233','services234','services235','services236','services237']

writer.writerow(corlist)


# In[7]:


for area in areas:
    for services in range(1,238):
        location = area[2]
        offset = 0
        jsonData = getData(location, str(offset), str(services))

        print('count', jsonData['count'])
        for jData in jsonData['corporations']:
            writer.writerow(compList(jData))
        if jsonData['count'] >= 100:
            for idex in range(100,jsonData['count'],100):
                offset = 0
                offset = idex
                json2Data = getData(location, str(offset), str(services))
                for jData in json2Data['corporations']:
                    writer.writerow(compList(jData)) 
    for i in range(30):
        print('*')
        time.sleep(60)
f.close()


# In[ ]:




