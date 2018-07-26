import re
from robobrowser import RoboBrowser
import urllib
import os
from get_vid import *
from support_functions import *
import sys

def get_hot_videos(Type):
    hot_videos = {}
    br = RoboBrowser(history=True,parser='lxml')
    for i in range(1,4):
        url = 'http://91porn.com/v.php?category={}&viewtype=basic&page={}'.format(Type,i)
        br.open(url)

        # get every video's information
        videos = br.find_all('div',{'class':'listchannel'})
        # get their titles and urls
        videos_dict = dict([(i.find('a').find('img')['title'],i.find('a')['href']) for i in videos])
        hot_videos.update(videos_dict)
    return hot_videos

def run_hot_videos():
    Type = input('请问您要下载的是？\n最近热门（输入hot）\n收藏最多（输入mf）\n本月收藏（输入tf）\n最近得分（输入rp）\n本月最热（输入top）\n最近加精（输入rf）\n输入：')
    hot_videos = get_hot_videos(Type)
    for i,j in enumerate(hot_videos.keys()):
        print(i,j)
    dl_id = input('请选择您要下载的视频id：')
    path = input('请输入文件保存位置: ')
    if dl_id:
        if 0 <= int(dl_id) <= 59:
            url = hot_videos[list(hot_videos.keys())[int(dl_id)]]
            download_video(url,path)
        else:
            print('没有这个视频id！')
            
    else:
        raise ValueError('必须要输入一个id！')

if __name__ == '__main__':
    run_hot_videos()