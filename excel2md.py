# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 9:30
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : excel2md.py
# @Software: PyCharm


# excel自动转成md文档格式
import pandas as pd

def excelToMd(path, sheetName="Sheet1"):
    df = pd.read_excel(path, sheetName)
    title = "|"
    splitLine = "|"
    for i in df.columns.values:
        title = title + i + "|"
        splitLine = splitLine + "--" + "|"
    print(title)
    print(splitLine)
    for i in df.iterrows():
        row = "|"
        for j in df.columns.values:
            row = row + str(i[1][j]) + "|"
        print(row.replace("nan", "-"))

excelToMd(r"E:\Ipython\PythonOfficeAuto\excel2md\字符类.xls")

