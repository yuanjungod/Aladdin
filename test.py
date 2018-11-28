# coding: utf-8

from tgrocery import Grocery


grocery = Grocery('test')
train_src = [
    ('education', '名师指导托福语法技巧：名词的复数形式'),
    ('education', '中国高考成绩海外认可 是“狼来了”吗？'),
    ('sports', '图文：法网孟菲尔斯苦战进16强 孟菲尔斯怒吼'),
    ('sports', '四川丹棱举行全国长距登山挑战赛 近万人参与')

grocery.train(train_src)
print grocery.get_load_status()
predict_result = grocery.predict('都要学习托福语法')
print predict_result
print predict_result.dec_values

predict_result = grocery.predict('中国高考成绩海外认可 是“狼来了”吗？')
print predict_result
print predict_result.dec_values


grocery = Grocery('read_text')
train_src = 'train_ch.txt'
grocery.train(train_src, ':')
print grocery.get_load_status()
predict_result = grocery.predict('我从哪里来')
print predict_result
print predict_result.dec_values