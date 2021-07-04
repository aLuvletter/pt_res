# -*- coding:utf-8 -*-
# Time:2021/04/29 20:29
# Author:Chiser

import requests
import json
import datetime
import time

def get_page(item):
    now = datetime.datetime.now()
    time = '[' + now.strftime("%Y-%m-%d %H:%M:%S") + ']'
    f = open('run.log', 'a+')
    try:
        if 'action' in item.keys():
            data = {
                'action': 'sign_in'
            }
            response = requests.post(item['url'], headers=headers, data=data)
        else:
            response = requests.get(item['url'], headers=headers)
        now = datetime.datetime.now()
        time = '[' + now.strftime("%Y-%m-%d %H:%M:%S") + ']'
        if response.status_code == 200:
            response = response.text
            if '签到成功' in response or '恭喜您' in response:
                f.write(time + item['site'] + '签到成功~\n')
            elif '重复刷新' in response or '重复' in response or '簽到過' in response or '已经打卡' in response:
                f.write(time + item['site'] + '你已签到过了~\n')
            elif '开小差' in response and '已经打卡' not in response:
                f.write(time + item['site'] + '签到失败~\n')
            elif '首页' or '首頁' in response:
                f.write(time + item['site'] + '今日已访问~\n')
        else:
            f.write(time + item['site'] + '网站无法访问~\n')
        f.close()
    except:
        f.write(time + item['site'] + '网站无法访问~\n')
        f.close()

if __name__ == '__main__':
    while True:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        json_data = open('site.json', encoding='utf-8')
        json_data = json.load(json_data)
        for item in json_data:
            try:
                if item['referer']:
                    headers = {
                        'user-agent': user_agent,
                        'referer': item['referer'],
                        'cookie': item['cookie']
                    }
            except:
                headers = {
                    'user-agent': user_agent,
                    'cookie': item['cookie']
                }
            get_page(item)
        time.sleep(43200)
