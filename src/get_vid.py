#coding: utf-8
#Author: Zhiao Zhou
#Date: 2018/7/18

import re
import sys
from robobrowser import RoboBrowser
import urllib
from support_functions import *

url = sys.argv[1]
path = sys.argv[2]

br = RoboBrowser(history=True,parser='lxml')
br.open(url)

# shift to simplified chinese 
lang = br.get_forms()[0]
lang['session_language'].options = ['cn_CN']
lang['session_language'].value = 'cn_CN'
br.submit_form(lang)

# get video title
vid_title = br.find('div',{'id':'viewvideo-title'}).text.strip()
print('the video you want to download is: {0}'.format(vid_title))

# get video id
vid_id = re.findall(r'\d{6}',br.find('a',{'href':'#featureVideo'}).attrs['onclick'])[0]

# get real video link
vid_real_url = 'http://192.240.120.34//mp43/{}.mp4'.format(vid_id)

# download 
#urllib.request.urlretrieve(vid_real_url,'{}.mp4'.format(vid_title))
if download_video_by_url(vid_real_url, path, vid_title):    
            print('下载成功！珍惜生命，远离黄赌毒！')