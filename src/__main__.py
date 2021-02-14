#coding=utf-8

# 程序名
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021 Haujet Zhao

# 内存分析：
# @profile
# python -m memory_profiler __main__.py

import argparse
import os
import shlex
import subprocess
import sys

# 这里从相对路径导入，在被 pyinstaller 打包时，需要换成绝对路径
from .moduel import *

def main():

    parser = 得到参数解析器()

    参数列表, 命令行参数为空 = 得到参数列表()

    args = parser.parse_args(参数列表)

    处理参数(args)

    # 如果命令行参数为空，用户有可能是从 win+r 运行的
    # 程序运行完，黑窗口会立马关闭
    # 为了用户能看到日志信息，使用回车键结束程序
    if 命令行参数为空:
        input('\n所有任务处理完毕，按下回车结束程序')

def 得到参数解析器():
    parser = argparse.ArgumentParser(
        description='''功能：*****  用途示例：  *****''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('Audio', type=str, help='外置音频，只能输入一个')
    parser.add_argument('Video', nargs='+', type=str, help='可一次添加多个文件')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('--time', metavar='Minutes', type=int, default=0, help='分钟数')
    parser.add_argument('--switch', action='store_true', help='开关')

    return parser

def 得到参数列表():
    if len(sys.argv) == 1:
        命令行参数为空 = True
        参数列表 = sys.argv
        print(f'''
你没有输入任何文件，因此进入文字引导。
程序的用处主要是***，例如：
  * ~~~
  * ~~~
        ''')
        print(f'\n首先输入 *** ')
        参数列表.append(得到输入文件())
    else:
        命令行参数为空 = False
        参数列表 = sys.argv
    return 参数列表, 命令行参数为空

def 得到输入文件():
    while True:
        用户输入 = input(f'请输入文件路径 或 直接拖入：')
        if 用户输入 == '':
            continue
        if os.path.exists(用户输入.strip('\'"')):
            输入文件 = 用户输入.strip('\'"')
            break
        else:
            print('输入的文件不存在，请重新输入')
    return 输入文件

def 处理参数(参数: argparse.ArgumentParser):
    for index, file in enumerate(参数.video):
        print(f'\n总共有 {len(参数.Video)} 个文件需要处理，正在对齐第 {index + 1} 个：{file}')
        处理文件(file)

def 处理文件(file):
    ...

if __name__ == '__main__':
    main()