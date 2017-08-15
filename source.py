import requests
from bs4 import BeautifulSoup
import sqlite3 as lite

def get_gif(num):
    url = 'http://neihan1024.com/weibofun/weixin/article.php?fid={}&category=weibo_pics&source=1'.format(num)
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
                print(num+'saved')
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

def gif_page(num1,num2):
    for i in range(num1, num2):
        get_gif(i)


gif_page(163968,200000)


