import string
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

# 读取数据
df = pd.read_excel('./Graphical output exercise v1.0.xlsx', sheet_name='Data Set 1', header=4, nrows=10)
y_1 = 0
y_2 = 0
y_3 = 0
x_axis_data = []
y_axis_data1 = []
y_axis_data2 = []
y_axis_data3 = []

# 提取日期和现金流数据
x_axis_data = pd.to_datetime(df['Date'])  # 转换日期格式

for i in df['Cash flow']:
    y_axis_data3.append(y_3 + i)
    y_3 += i
    if i>=0:
        y_axis_data1.append(y_1 + i)
        y_axis_data2.append(y_2)
        y_1 += i
    else:
        y_axis_data1.append(y_1)
        y_axis_data2.append(y_2 - i)
        y_2 -= i

# 设置日期格式
date_fmt = mdates.DateFormatter('%Y-%m-%d')

# 绘图
fig, ax = plt.subplots()

bar_width = 0.3  # 条形宽度
index_y_axis_data1 = np.arange(len(x_axis_data))
index_y_axis_data2 = index_y_axis_data1 + bar_width
index_y_axis_data3 = index_y_axis_data2 + bar_width

ax.bar(index_y_axis_data1, y_axis_data1, width=bar_width, label='Cumulative Distributions')
ax.bar(index_y_axis_data2, y_axis_data2, width=bar_width, label='Cumulative Contributions')
ax.bar(index_y_axis_data3, y_axis_data3, width=bar_width, label='Cumulative combined net basis')

ax.axhline(0, color='gray', linestyle='-', linewidth=1)  # 添加水平线

ax.xaxis.set_major_formatter(date_fmt)  # 格式化横坐标为日期格式
plt.xticks(index_y_axis_data1 + bar_width / 2, x_axis_data.dt.strftime('%Y-%m-%d'), rotation=45)  # 设置横坐标标签

plt.legend()
plt.ylabel('Cash flow')
plt.xlabel('Date')
plt.title('Quarterly Cash Flow Trends')
plt.tight_layout()  # 调整布局，以免标签被截断
plt.show()