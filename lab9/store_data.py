import json
import os
from lab9 import db_en, db_jp


def store_key(file_name, is_en):
    fp = open(file_name, encoding='utf-8')
    try:
        temp = json.loads(fp.read())
    except :
        print(file_name)
        return
    res_list = temp['response']['list']
    ans = []
    for res in res_list:
        nick = res['trackback_author_nick']
        name = res['trackback_author_name']
        date = res['trackback_date']
        content = res['content']
        n_data = {
            'nick': nick,
            'name': name,
            'date': date,
            'content': content
        }
        ans.append(n_data)
    if len(ans) == 0:
        return

    if is_en:
        db_en.insert_many(ans)
    else:
        db_jp.insert_many(ans)


if __name__ == '__main__':
    db_en.delete_many({})
    db_jp.delete_many({})

    path_en = 'E:/study_resources/大三上学习/4_数据科学导论/labs/lab9-图数据建模和可视化/附件/附件1-ENalljson'
    files_en = os.listdir(path_en)
    for file in files_en:
        if not os.path.isdir(file):
            f_name = path_en + '/' + file
            store_key(f_name, True)

    print('英文数据已处理！')

    path_jp = 'E:/study_resources/大三上学习/4_数据科学导论/labs/lab9-图数据建模和可视化/附件/附件2-JPalljson'
    files_jp = os.listdir(path_jp)
    for file in files_jp:
        if not os.path.isdir(file):
            f_name = path_jp + '/' + file
            store_key(f_name, False)

    print('关键信息提取完毕！')
