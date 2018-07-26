#coding: utf-8
#Author: Zhiao Zhou
#Date: 2018/7/18

import re
import sys
from robobrowser import RoboBrowser
import urllib
from support_functions import *

#url = sys.argv[1]
#path = sys.argv[2]

def get_video_url(url):
    
    br = RoboBrowser(history=True,parser='lxml')
    br.open(url)

    cn = input('请问是否要转换为中文？(y/n)')
    if not cn:
        cn = 'y'
    if cn == 'y':
        # shift to simplified chinese 
        lang = br.get_forms()[0]
        lang['session_language'].options = ['cn_CN']
        lang['session_language'].value = 'cn_CN'
        br.submit_form(lang)

    # get video title
    vid_title = br.find('div',{'id':'viewvideo-title'}).text.strip()
    print('the video you want to download is: {0}'.format(vid_title))
    print('-----------------------------------------------------------')

    # get video id
    vid_id = re.findall(r'\d{6}',br.find('a',{'href':'#featureVideo'}).attrs['onclick'])[0]

    # get real video link
    vid_real_url = 'http://192.240.120.34//mp43/{}.mp4'.format(vid_id)
    return vid_real_url, re.sub("""[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。|？、~@#￥%……&*（）：]+""", " ",vid_title).strip()

# download 
#urllib.request.urlretrieve(vid_real_url,'{}.mp4'.format(vid_title))

def download_video(url,path):
    vid_real_url, vid_title = get_video_url(url)
    if download_video_by_url(vid_real_url, path, vid_title):    
        print('---------------------------')
        print('下载成功！珍惜生命，远离黄赌毒！')
    else:
        print('下载失败')

def run_single_video():
    url = input('请输入您要下载的（内涵）视频地址：')
    path = input('请输入文件下载位置：')
    download_video(url,path)
    
if __name__ == '__main__':
    run_single_video()