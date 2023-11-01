import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./Graphical output exercise v1.0.xlsx', sheet_name='Data Set 1', header=4, nrows=10)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 按季度结束日期进行重采样
df_resampled = df.resample('Q').sum()

x_axis_data = df_resampled.index
y_axis_data1 = df_resampled['Cash flow'].cumsum()
y_axis_data2 = df_resampled['Cash flow'].apply(lambda x: -x if x < 0 else 0).cumsum()
y_axis_data3 = (y_axis_data1 + y_axis_data2)

# 画图
plt.plot(x_axis_data, y_axis_data3, 'b*--', label='Cumulative Distributions')
plt.plot(x_axis_data, y_axis_data2, 'rs--', label='Cumulative Contributions')
plt.plot(x_axis_data, y_axis_data1, 'go--', label='Cumulative combined net basis')
plt.axhline(0, color='gray', linestyle='-', linewidth=1)  # 添加水平线
plt.legend()  # 显示上面的label
plt.ylabel('Cash flow')
plt.title('Quarterly Cash Flow Trends')
plt.xlabel('Date')
plt.show()