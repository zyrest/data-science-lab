from lab1 import db
from bs4 import BeautifulSoup

import requests

url_suffix = 'https://steamcn.com/suid-'


def store_user_info(limits):
    for uid in range(1, limits):
        try:
            ans = dict()
            ans['uid'] = uid
            url = url_suffix + str(uid)
            html = requests.get(url).content.decode('utf-8')
            soup = BeautifulSoup(html, 'lxml')
            table = soup.select_one('#ct > div > div.bm.bw0 > div > div.bm_c.u_profile')

            datas = table.select('div.pbm.mbm.bbda.cl')
            infos = datas[0]
            active = table.find('h2', class_='mbn', text='活跃概况').parent
            analysis = table.select_one('#psts')

            name = infos.select_one('h2').contents[0].strip()
            sex = infos.select('ul')[3].select('li')[0].contents[1].strip()
            ans['姓名'] = name
            ans['性别'] = sex

            title = active.select_one('ul > li > span > a > font').contents[0].strip()
            ans['头衔'] = title
            act_ul = active.select_one('#pbbs').select('li')
            for li in act_ul:
                key = li.select_one('em').text
                value = li.contents[1].strip()
                ans[key] = value

            ana_ul = analysis.select_one('ul').select('li')
            for li in ana_ul:
                key = li.select_one('em').text
                value = li.contents[1].strip()
                ans[key] = value

            print(ans)
            db.insert_one(ans)
        except:
            continue


if __name__ == '__main__':
    user_nums = 400000
    store_user_info(user_nums)
