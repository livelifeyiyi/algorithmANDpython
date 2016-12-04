#-*- coding:utf-8 -*-
import pandas as pd

filePath = u'./input/测试用固定资产清单-input.xls'
name = [u'资产编号', u'资产描述', u'入账日期', u'折旧年限', u'原值', u'累计折旧', u'残值', u'本期折旧']
data = pd.read_excel(filePath)
newData = pd.DataFrame()

#获取列名称
row_name = data.colums

#按照name，截取部分列到new dataframe
for i in name:
	datai = data.ix[:, i]
	newData[i] = datai

newData.insert(4, u'折旧方法', u'直线法')
newData.index = newData.index + 1
print newData
newData.to_excel('./output/output.xls', 'Sheet1')
newData.to_csv('test_data1.dat', index=False, sep=' ')
#删除行
newData.drop([i for i in range(0,399)])
#从txt文件读取数据，以空格为间隔符，按照names对列命名
multi_phenos = pd.read_table('filename.txt', sep='\s+', names=['pheno1','pheno2','pheno3','pheno4','pheno5','pheno6','pheno7','pheno8','pheno9','pheno10'])


print newData.ix[0,['year']].values#选择行和列
print newData.ix[2]#选择单行
print newData.ix[:,'year']#选择单列
frame2 = newData.ix[:,['year','pop']]
print frame2