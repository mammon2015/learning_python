#!/usr/local/python/bin/python
#
#   本文件包含 Extractor 系列中通用超类的定义, 包含:
#       Extractor
#           WebExtractor
#           FileExtractor
#
# -*- coding: utf-8 -*-
""" Module contains the superclasses of 'Extractor'. """

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
#
#   所有数据抓取器的基类.
#       属性:
#           state(str)  用于记录抓取器的状态, 例如 "抓取成功", "转换结束"。
#       方法:
#           fetch()     用于抓取数据
#           upload()    用于上传数据到数据库
#
class Extractor:
    """ Root class of all data extractors """

    def __init__(self):
        super().__init__()
        # 类属性定义部分
        self._state = "已初始化"
        # 初始化本地日志
        self.log = logging.getLogger("Extrator")

    def fetch(self):
        """ Fetches data from source, returns None. """
        pass


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
