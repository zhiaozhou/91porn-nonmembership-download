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

def dl_multiple_videos(dl_id,path,hot_videos):
    if 0 <= int(dl_id) <= 59:
        url = hot_videos[list(hot_videos.keys())[int(dl_id)]]
        download_video(url,path)
    else:
        print('没有这个视频id！')

def run_hot_videos():
    Type = input('请问您要下载的是？\n最近热门（输入hot）\n收藏最多（输入mf）\n本月收藏（输入tf）\n最近得分（输入rp）\n本月最热（输入top）\n最近加精（输入rf）\n输入：')
    hot_videos = get_hot_videos(Type)
    for i,j in enumerate(hot_videos.keys()):
        print(i,j)
    one_or_multiple = input('请问您要下载列表中的单个视频或部分（输入0）还是批量全部下载（输入1）？')
    if one_or_multiple:
        if one_or_multiple in ['1','0']:
            if one_or_multiple == '0':
                # --- 单个
                dl_id = input("请选择您要下载的视频id（如果是多个请用英文逗号','隔开）：")
                path = input('请输入文件保存位置: ')
                if dl_id:
                    if not ',' in dl_id:
                        dl_multiple_videos(dl_id,path,hot_videos)
                    else:
                        for i in dl_id.split(','):
                            dl_multiple_videos(i,path,hot_videos)
                else:
                    raise ValueError('必须要输入至少一个id！')
                # ---
            else:
                # --- 批量
                path = input('请输入文件保存位置: ')
                for i in hot_videos.values():
                    download_video(i,path)
                # ---
        else:
            raise ValueError('没有这个选项！')
    else:
        raise ValueError('必须要输入一个选择！')
        
if __name__ == '__main__':
    run_hot_videos()
    continue_ = input("请问您是否要继续下载？（继续请输入1，否则请输入0）")
    while int(continue_):
        run_hot_videos()
        continue_ = input("请问您是否要继续下载？（继续请输入1，否则请输入0）")
        