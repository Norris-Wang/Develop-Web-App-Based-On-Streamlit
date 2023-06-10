# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:00:21 2023

@author: Yamato
"""

import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('长三角PM2.5监测数据')
#读入数据
url = 'https://ecnugischaser.github.io/gis_development/data/csj_pm25.csv'
data = pd.read_csv(url)
data.to_csv(r'data.csv')
st.dataframe(data)

st.title('基于属性表达式查询记录')
#设置查询条件
fields = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
field = st.selectbox('选择一个字段', fields)
operators = ['>', '<']
operator = st.selectbox('选择一个关系', operators)
value = st.number_input('输入一个值', value=0)

if operator == '>':
    results = data[data.loc[:, field] > value]
else:
    results = data[data.loc[:, field] < value]

#显示查询结果
num = len(results)
st.title(f'共有{num}条记录')
st.dataframe(results)

#显示结果的空间位置
location = results.loc[:, ['经度', '纬度']]
location.columns = ['lon', 'lat']
st.map(location)