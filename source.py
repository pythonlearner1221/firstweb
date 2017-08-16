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
                title = soup.select('p')[0].text.strip()
                created_time = soup.select('div.info_text')[0].text[:10]
                gif_index = num
                # print(title,img_url,created_time,gif_index)
                save_to_sqlite(title,img_url,created_time,gif_index)
                print(str(num)+'saved')
            else:
                pass
        else:
            pass
    except:
        pass

def save_to_sqlite(title,url,created_time,gif_index):
    with lite.connect('db.sqlite3') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO merlin_gifpics (title,url,created_time,gif_index) Values (?,?,?,?)",(title,url,created_time,gif_index))

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_gif,range(174901,200000))




