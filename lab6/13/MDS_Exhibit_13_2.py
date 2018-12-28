import numpy as np  # arrays and math functions
import pandas as pd  # data frame operations
import statsmodels.formula.api as smf  # statistical models (including regression)

# 读取饭店数据 csv 文件，创建 pandas data frame
restdata = pd.read_csv('studenmunds_restaurants.csv')

# print the first five rows of the data frame
# print(pd.DataFrame.head(restdata))

# 回归模型
my_model = str('sales ~ competition + population + income')

# 在饭店数据上使用线性回归
my_model_fit = smf.ols(my_model, data=restdata).fit()

print(my_model_fit.summary())

# 获取预测结果
restdata['predict_sales'] = my_model_fit.fittedvalues

# 计算两列值的相关系数，默认用的是pearson相关系数
print()
print('Proportion of Test Set Variance Accounted for: ',
      round(np.power(restdata['sales'].corr(restdata['predict_sales']), 2), 3))

# 定义三家新饭店的数据
sites_data = {'sales': [0, 0, 0],
              'competition': [2, 3, 5],
              'population': [50000, 200000, 220000],
              'income': [25000, 22000, 19000]}

sites = pd.DataFrame(sites_data)

# obtain predicted sales for the new restaurants
# rounding to the nearest dollar
sites['sales_pred'] = my_model_fit.predict(sites)
print('\nNew sites with predicted sales')
print(sites)
