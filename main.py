import random,json,time,os
from nlp import check,nlp_api,loadfile

if __name__ == '__main__':
    start = (2023,1,1,0,0,0,0,0,0)
    end = (2023,12,31,23,59,59,0,0,0)
    start_date = time.mktime(start)
    end_date = time.mktime(end)
    for i in range(1,46+1):
        t=random.randint(start_date,end_date)
        date = time.localtime(t)
        date = time.strftime('%Y-%m-%d',date)
        print(date)
        #输出至output文件夹
        path = os.path.join('raw',date+'.json')
        data = json.dumps(check(path),ensure_ascii=False)
        path_name = path.split('\\')[1]
        with open('output/'+path_name,'a+',encoding='utf8') as f:
            f.write(data)
    print('end')