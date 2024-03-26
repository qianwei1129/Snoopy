import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据，假设已经进行了卡方检验并得到了结果
# 这里假设results_df是一个包含特征名称和对应卡方检验P值的数据框
results_df = pd.DataFrame({'特征': ['Feature1', 'Feature2', 'Feature3'],
                           '卡方检验P值': [0.001, 0.005, 0.01]})

# 将P值转换为颜色编码，这里简单示范，可以根据具体需求自定义颜色映射
results_df['Color'] = results_df['卡方检验P值'].apply(lambda p: 'lightblue' if p < 0.05 else 'darkblue')

# 绘制热图
plt.figure(figsize=(8, 6))
sns.heatmap(data=results_df[['卡方检验P值']], cmap=sns.color_palette(['darkblue', 'lightblue']), annot=True, fmt=".4f")
plt.title('卡方检验P值热图')
plt.xlabel('特征')
plt.ylabel('')

plt.show()
