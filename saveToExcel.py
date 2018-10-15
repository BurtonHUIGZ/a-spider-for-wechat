# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:44:36 2018

@author: Administrator
"""

import xlwt
from datetime import datetime
import json


#写一个读取爬取文件的类
class readCSV(object):
    def __init__(self,filename):
        self.name = filename
    def readfile(self):
        with open(self.name,'r',encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    def saveToExcel(self):
        lines = self.readfile()
        for i in range(60000):
            items = {}
            items['title'] = eval(lines[i])['文章标题']
            items['belongsTo'] = eval(lines[i])['所属公众号']
            items['author'] = eval(lines[i])['文章作者']
            items['typeOfTitle'] = eval(lines[i])['文章所属类型']
            items['url'] = eval(lines[i])['文章链接地址']
            yield items
    def writeToCsv(self):
        #创建一个工作薄
        xlst = xlwt.Workbook()
        #设置一个时间格式
        xfobj = xlwt.XFStyle()
        xfobj.num_format_str = 'yyyy-mm-dd'
        #设置字体
        fonts = xlwt.Font()
        fonts.bold = 'True'
        fonts.height = 12 * 20
        fonts.name = 'SimSun'
        xfobj.font = fonts
        
        #在工作薄中创建一个表
        sheet = xlst.add_sheet('微信文章信息', cell_overwrite_ok=False)
        sheet.col(0).width = 256 * 50
        sheet.col(1).width = 256 * 20
        sheet.col(2).width = 256 * 20
        sheet.col(3).width = 256 * 20
        sheet.col(4).width = 256 * 100
        sheet.col(5).width = 256 * 20
        #创建标题
        sheet.write(0,0,'文章标题',xfobj)
        sheet.write(0,1,'所属公众号',xfobj)
        sheet.write(0,2,'文章作者',xfobj)
        sheet.write(0,3,'文章所属类型',xfobj)
        sheet.write(0,4,'文章链接地址',xfobj)
        #引用一个时间格式xfobj
        sheet.write(0,5,'插入时间',xfobj)
        
        items = self.saveToExcel()
        row = 1
        for item in items:
            
            sheet.write(row,0,item['title'])
            sheet.write(row,1,item['belongsTo'])
            sheet.write(row,2,item['author'])
            sheet.write(row,3,item['typeOfTitle'])
            sheet.write(row,4,item['url'])
            #引用一个时间格式xfobj
            sheet.write(row,5,datetime.now(),xfobj)
            row += 1
        xlst.save('example.csv')
    
if __name__ == '__main__':
    file = 'json.txt'
    s = readCSV(file)
    s.writeToCsv()
    