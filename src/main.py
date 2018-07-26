import re
from robobrowser import RoboBrowser
import urllib
import os
from get_vid import *
from support_functions import *
from dl_hot_videos import *
import sys

if __name__ == '__main__':
    print('----------------')
    print('91porn视频下载破解')
    print('----------------')
    print('作者：zhiaozhou')
    print('-----------------------------------------------------------------')
    print('源代码：https://github.com/zhiaozhou/91porn-nonmembership-download')
    print('-----------------------------------------------------------------')
    choice = input('请问您要下载单个视频（输入1），或是下载热门列表视频（输入2）？')
    if choice:
        if choice in ['1','2']:
            if choice == '1':
                run_single_video()
            else:
                run_hot_videos()     

        else:
            raise ValueError('没有这个选项！')

    else:
        raise ValueError('必须要输入一个选择！')