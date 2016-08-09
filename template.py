#!/usr/local/python/bin/python
#
# -*- coding: utf-8 -*-
#
#   本文件包含 Extractor 系列中通用超类的定义, 包含:
#       Extractor
#           WebExtractor
#           FileExtractor
#
""" Docstring for module """

#
# SECTION: MODULE IMPORTS
#
import logging


#
# SECTION: DEFINE EXTERNAL INTERFACE
#
__all__ = ['',]

#
# SECTION: GLOBAL VARIABLES DECLARATION
#


#
# SECTION: GLOBAL FUNCTION DEF
#


#
# SECTION: CLASS DEFINATION
#
#   所有数据抓取器的基类.
#       属性:
#       方法:
#
class Extractor:
    """ Sample Class Definaton """

    def __init__(self):
        super().__init__()
        # 类属性定义部分


# SECTION: SELFTESTING
#
#   syntax: python <filename>
#
if __name__ == "__main__":
    # 自我测试用的 logging 机制, 仅输出错误到标出错误输出。
    log = logging.getLogger("MAIN")
    log.setLevel(logging.DEBUG)  # 在此处设置生成日志的级别
    ch1 = logging.StreamHandler()
    ch1.setLevel(logging.DEBUG)  # 在此处设置输出日志的级别
    fmt = logging.Formatter(
        fmt='%(asctime)s %(levelname)8s %(name)s : %(message)s',
        datefmt='%y-%m-%d %H:%M:%S |')
    ch1.setFormatter(fmt)
    log.addHandler(ch1)

    # 构造变量, 或调用函数以对本模块进行自我测试
