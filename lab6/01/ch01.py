from numpy import *

import pandas as pd  # data frame operations
import statsmodels.formula.api as smf  # R-like model specification


# 读取数据源 csv 文件
conjoint_data_frame = pd.read_csv('mobile_services_ranking.csv')

# 设置联合分析全轮托
# using C(effect, Sum) notation within main effects model specification
main_effects_model = 'ranking ~ C(brand, Sum) + C(startup, Sum) +  \
    C(monthly, Sum) + C(service, Sum) + C(retail, Sum) + C(apple, Sum) + \
    C(samsung, Sum) + C(google, Sum)'

# 线性回归，仅使用 main effects
main_effects_model_fit = smf.ols(main_effects_model, data=conjoint_data_frame).fit()
print(main_effects_model_fit.summary())
print()

conjoint_attributes = ['brand', 'startup', 'monthly', 'service', 'retail', 'apple', 'samsung', 'google']
print(conjoint_attributes)

# 构建 分值效用：用于描述消费者对每种属性的各个水平所赋予的效用，或者说它们对消费者偏好的作用大小
level_name = []
part_worth = []
part_worth_range = []
end = 1
for item in conjoint_attributes:
    nlevels = len(list(unique(conjoint_data_frame[item])))              # 有多少种水平
    level_name.append(list(unique(conjoint_data_frame[item])))          # 将水平值存在队列中
    begin = end
    end = begin + nlevels - 1
    new_part_worth = list(main_effects_model_fit.params[begin:end])     # 每种水平的效用值
    new_part_worth.append((-1) * sum(new_part_worth))
    part_worth_range.append(max(new_part_worth) - min(new_part_worth))
    part_worth.append(new_part_worth)
    # end set to begin next iteration
attribute_importance = []
for item in part_worth_range:                                           # 相对重要性 = 分值距离占比
    attribute_importance.append(round(100 * (item / sum(part_worth_range)), 2))
print(attribute_importance)

effect_name_dict = {'brand': 'Mobile Service Provider',
                    'startup': 'Start-up Cost',
                    'monthly': 'Monthly Cost',
                    'service': 'Offers 4G Service',
                    'retail': 'Has Nearby Retail Store',
                    'apple': 'Sells Apple Products',
                    'samsung': 'Sells Samsung Products',
                    'google': 'Sells Google/Nexus Products'}

# 输出联合分析结果
index = 0
for item in conjoint_attributes:

    print('\nAttribute:', effect_name_dict[item])

    print('    Importance:', attribute_importance[index])
    print('    Level Part-Worths')
    for level in range(len(level_name[index])):
        print('       ', level_name[index][level], part_worth[index][level])
    index = index + 1
