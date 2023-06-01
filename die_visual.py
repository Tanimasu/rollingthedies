import plotly.graph_objs as go
import plotly.offline as pyo
from collections import Counter

from die import Die

# 获取用户输入的骰子面数
while True:
    try:
        num_1 = int(input("请输入骰子的面数："))
        num_2 = int(input("请输入骰子的面数："))
        if num_1 <= 0 or num_2 <= 0:
            raise ValueError("请输入一个大于0的整数")
        break
    except ValueError as e:
        print(f"无效的输入：{e}")

# 创建骰子
die_1 = Die(num_1)
die_2 = Die(num_2)

# 获取用户输入的投掷次数
while True:
    try:
        num_rolls = int(input("请输入要投掷骰子的次数："))
        if num_rolls <= 0:
            raise ValueError("请输入一个大于0的整数")
        break
    except ValueError as e:
        print(f"无效的输入：{e}")

# 投掷几次骰子并将结果储存在一个列表中
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

# 分析结果
frequencies = Counter(results)

# 对结果进行可视化
result_values = sorted(frequencies.keys())
frequencies_values = [frequencies[val] for val in result_values]

data = [go.Bar(x=result_values, y=frequencies_values)]

my_layout = go.Layout(title=f'投掷一个D{num_1}和一个D{num_2} {num_rolls}次的结果',
                      xaxis={'title': '结果'},
                      yaxis={'title': '结果的频率'},
                      )

fig = go.Figure(data=data, layout=my_layout)
pyo.plot({'data': data, 'layout': my_layout}, filename='dice_roll.html')
