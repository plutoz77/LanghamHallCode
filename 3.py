import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('./Graphical output exercise v1.0.xlsx', sheet_name='Data Set 2', header=6, nrows=10)

Industry_list = {}
for index, row in df.iterrows():
    industry = row['Industry']
    value = row['Fair value (in USD)']
    if industry not in Industry_list:
        Industry_list[industry] = value
    else:
        Industry_list[industry] += value

labels = list(Industry_list.keys())
sizes = list(Industry_list.values())

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('1. Investment by Industry')
plt.axis('equal')

# 添加完整数值标签
total = sum(sizes)
previous_angle = 0
label_distance = 0.8  # 调整文字到饼图中心的距离
for label, size in zip(labels, sizes):
    angle = previous_angle + size / total * 360 / 2  # 计算标签的角度位置
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    dx = x * label_distance
    dy = y * label_distance
    plt.text(dx, dy, f'{size:,}', ha='center', va='center')
    previous_angle += size / total * 360

plt.show()