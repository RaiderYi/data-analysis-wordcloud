#-*- coding:utf-8 -*-
import pandas as  pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']# 用于显示plt的中文标签
pd.set_option('display.max_columns', None)#显示所有列
pd.set_option('display.max_rows', None)#显示所有行
data = pd.read_csv('C:\User\dell\Desktop\大众点评\dazhong.csv',encoding='gbk')
#print(data.head())#显示数据前5行
#print(data.head().columns)#显示数据每一列属性（即列名称）
#print(data.head().shape)#显示数据形状
data_analysis = data.loc[:,['Type', 'ID', 'ReviewNum', 'Level',
       'FlavorScore', 'EnvironmentScore', 'ServiceScore',
       'ApplauseRate',  'PictureNum', 'ParkingNum']]#选取特定的列
#菜系种类
kind=data_analysis['Type'].value_counts().sort_values(ascending=False)
kind=pd.DataFrame(kind)
#print(kind)
#菜系和评分之间的关系
kind_score=data_analysis[['Type','Level']].groupby(data_analysis['Type']).mean()
print(kind_score)
#plt.figure()
#plt.bar(data_analysis['Type'],data_analysis['Level'])
#plt.show()
#评分分布情况
star_map = data_analysis['Level'].value_counts(ascending=True)
#print(star_map)
sizes=[3,85,170,445,1128,1293]
plt.figure()
plt.pie(star_map,
        autopct='%3.2f%%',  # 数值保留固定小数位
        labels=['2','5','3','4.5','4','3.5'])
plt.legend()
plt.title('店家评分分布情况')
#plt.show()

#各种评分折线图
df_pf=data_analysis.groupby('Type')['FlavorScore', 'EnvironmentScore', 'ServiceScore'].mean()
df_pf.head()
fig=plt.figure(figsize=(16,6))
ax1=fig.add_subplot(111)
ax1.plot(df_pf.index,df_pf['FlavorScore'],label='FlavorScore')
ax1.plot(df_pf.index,df_pf['EnvironmentScore'],label='EnvironmentScore')
ax1.plot(df_pf.index,df_pf['ServiceScore'],label='ServiceScore')
ax1.set_ylim(0,10)
plt.title('菜系与口味，环境，服务得分分布')
plt.legend(loc='best')
plt.grid()
#plt.show()
#分析粤菜
data_yuecai = data_analysis.loc[0:721]
plt.figure()
plt.subplot(221)
plt.scatter(data_yuecai['Level'],data_yuecai['FlavorScore'],alpha=0.5,edgecolors='red')
plt.title('店家得分与口味得分')
plt.subplot(222)
plt.scatter(data_yuecai['Level'],data_yuecai['EnvironmentScore'],edgecolors='yellow')
plt.title('店家得分与环境得分')
plt.subplot(223)
plt.scatter(data_yuecai['Level'],data_yuecai['ServiceScore'],edgecolors='blue')
plt.title('店家得分与环境得分')
plt.subplot(224)
plt.stackplot(data_yuecai['Level'], data_yuecai['FlavorScore'],
              data_yuecai['EnvironmentScore'],data_yuecai['ServiceScore'],
              colors=['m','c','r','k'])
plt.legend()
plt.title('得分折叠图')
plt.show()

plt.figure()
sns.pairplot(data_yuecai,hue="Level",palette="husl")  #hue 选择分类列#
plt.title('粤菜店家得分概况')
plt.show()
sns.heatmap(data_yuecai.corr())
plt.show()
sns.jointplot(data_yuecai['Level'], data_yuecai['FlavorScore'], kind='hex')
sns.jointplot(data_yuecai['Level'], data_yuecai['FlavorScore'], kind='kde')
sns.scatterplot(x=data_yuecai['ReviewNum'],y=data_yuecai['ApplauseRate'])
plt.show()
sns.boxplot(x = data_yuecai['Level'],y = data_yuecai['FlavorScore'])
plt.show()
sns.boxplot(x = data_yuecai['Level'],y = data_yuecai['EnvironmentScore'])
plt.show()
sns.boxplot(x = data_yuecai['Level'],y = data_yuecai['ServiceScore'])
plt.show()
