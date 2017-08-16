import requests
from bs4 import BeautifulSoup
import sqlite3 as lite
from multiprocessing import Pool

def get_gif(num):
    url = 'http://neihan1024.com/weibofun/weixin/article.php?fid={}&category=weibo_pics&source=1'.format(num)
    print(num)
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')
        if soup.select('p > img') != [] :
            img_url = soup.select('p > img')[0].get('src')
            if 'gif' in img_url:
                res2 = requests.get(img_url)
                if res2.history:
                    pass
                else:
                    title = soup.select('p')[0].text.strip()
                    created_time = soup.select('div.info_text')[0].text[:10]
                    gif_index = num
                    likes = int(soup.select('body > div:nth-of-type(2)')[0].text.split('\xa0')[0].strip('赞'))
                    save_to_sqlite(title,img_url,created_time,gif_index,likes)
                    print(str(num),'saved')
            else:
                pass
        else:
            pass
    except Exception as e:
        print(e)

def save_to_sqlite(title,url,created_time,gif_index,likes):
    with lite.connect('db.sqlite3') as con:
        cur = con.cursor()
        select = "SELECT * FROM merlin_gifpics WHERE gif_index={}".format(gif_index)
        cur.execute(select)
        res = cur.fetchall()
        if len(res) >0:
            update = "UPDATE merlin_gifpics set likes={} WHERE gif_index={}".format(likes,gif_index)
            cur.execute(update)
        else:
            insert = "INSERT INTO merlin_gifpics (title, url, created_time, gif_index,likes) VALUES (?,?,?,?,?)"
            cur.execute(insert,(title,url,created_time,gif_index,likes))

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_gif,range(1,180000))






