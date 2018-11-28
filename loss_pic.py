# coding:utf-8
import sys
import re
import matplotlib.pyplot as plt
import numpy as np

in_log_path = './train.log'  # 输入日志文件的位置
out_fig_path = './log.jpg'  # 输出图片的位置
f = open(in_log_path, 'r')
accuracy = []
train_loss = []
test_loss = []

max_iter = 0
test_iter = 0
test_interval = 0
display = 0
small_loss_count = 0
target_str = ['accuracy = ', 'Test net output #0: tripletloss = ', 'Train net output #0: tripletloss = ',
              'max_iter: ', 'test_iter: ', 'test_interval: ', 'display: ']
while True:
    line = f.readline()
    # print len(line),line
    if len(line) < 1:
        break
    for i in range(len(target_str)):
        str = target_str[i]
        idx = line.find(str)
        if idx != -1:
            # print(line[idx + len(str):idx + len(str) + 5])
            try:
                num = float(line[idx + len(str):idx + len(str) + 5])
            except:
                num = 0
            if num < 0.1:
                small_loss_count += 1
            if (i == 0):
                accuracy.append(num)
            elif (i == 1):
                test_loss.append(num)
            elif (i == 2):
                train_loss.append(num)
            elif (i == 3):
                max_iter = float(line[idx + len(str):])
            elif (i == 4):
                test_iter = float(line[idx + len(str):])
            elif (i == 5):
                test_interval = float(line[idx + len(str):])
            elif (i == 6):
                display = float(line[idx + len(str):])
            else:
                pass
f.close()
# print test_iter
# print max_iter
# print test_interval
print(len(accuracy), len(test_loss), len(train_loss))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[:1000]])) / 1000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[:2000]])) / 2000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[:3000]])) / 3000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[-1000:]])) / 1000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[-2000:]])) / 2000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss[-3000:]])) / 3000))
print("small loss count: %s" % ((1.0 * sum([0 if i > 0.1 else 1 for i in train_loss])) / len(train_loss)))

_, ax1 = plt.subplots()
ax2 = ax1.twinx()
# 绘制train_loss曲线图像，颜色为绿色'g'
ax1.plot(display * np.arange(len(train_loss)), train_loss, color='g', label='train loss', linestyle='-')

# 绘制test_loss曲线图像，颜色为黄色'y'
ax1.plot(test_interval * np.arange(len(test_loss)), test_loss, color='y', label='test loss', linestyle='-')

# 绘制accuracy曲线图像，颜色为红色'r'
ax2.plot(test_interval * np.arange(len(accuracy)), accuracy, color='r', label='accuracy', linestyle='-')

ax1.legend(loc=(0.7, 0.8))  # 使用二元组(0.7,0.8)定义标签位置
ax2.legend(loc=(0.7, 0.72))
ax1.set_xlabel('iteration')  # 设置X轴标签
ax1.set_ylabel('loss')  # 设置Y1轴标签
ax2.set_ylabel('accuracy')  # 设置Y2轴标签
plt.savefig(out_fig_path, dpi=100)  # 将图像保存到out_fig_path路径中，分辨率为100
plt.show()  # 显示图片
