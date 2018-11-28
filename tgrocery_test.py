# _*_coding:utf-8 _*_
from tgrocery import Grocery
import jieba
import jieba.posseg as pseg
from flask import Flask, jsonify
import random

app = Flask(__name__)

jieba.load_userdict("dict_dict.txt")

words = pseg.cut("加个鱼丸面")
for word, flag in words:
    print('%s %s' % (word, flag))

grocery = Grocery('sample')

train_src = [
    ('点餐', '来一份凉面'),
    ('点餐', '来一份乌冬面'),
    ('点餐', '整一份牛肉面'),
    ('点餐', '我要牛肉面'),
    ('点餐', '整碗白酒'),
    ('点餐', '加碗白酒'),
    ('点餐', '鱼香肉丝'),
    ('点餐', '牛肉面'),
    ('退菜', '不要牛肉面了'),
    ('退菜', '不整牛肉面了'),
    ('退菜', '牛肉面退了'),
    ('退菜', '牛肉面退掉'),
    ('结账', '老板埋单'),
    ('结账', '服务员结账'),
    ('结账', '老板娘结账'),
    ('结账', '老板结账')
]

intention_dict = {
    "点餐": "diancan",
    "下单": "xiadan",
    "结账": "jiezhang",
    "退菜": "tuicai",
    "推荐": "tuijian"
}

fo = open("dict_dict.txt", "r")

for line in fo.readlines():
    line = line.split(" ")[0]
    train_src.append(('点餐', line))
    train_src.append(('退菜', "不要%s" % line))

file_dict = {
    "下单": "下单.txt",
    "点餐": "点餐的意图.txt",
    "结账": "结账.txt",
    "推荐": "推荐意图.txt"
}

# for i in range(10000):
for key, value in file_dict.items():
    f = open(value, "r")
    for line in f.readlines():
        line = line.split(".")
        if len(line) == 0:
            print(key, line)
        else:
            train_src.append((key, line[1]))
#
# random.shuffle(train_src)
#
# print(len(train_src))
# w = open("train.txt", "w")
# for i in train_src:
#     w.write("%s--------%s\n" % (i[0], i[1]))
#     w.flush()
# w.close()

grocery.train(train_src)
grocery.save()
print(dir(grocery))
print(grocery.predict("给钱"))


@app.route('/<words>')
def intention(words):
    a = grocery.predict(words)
    print(str(a))
    print(a.dec_values[str(a)])
    # for key in a.dec_values:
    #     print(key)
    #     print(a.dec_values[key])
    # print(a.dec_values)
    result = {
            "code": 0,
            "message": "",
            "content": {
                "intent": intention_dict[str(a)],
                "score": a.dec_values[str(a)],
                "intentInfos": []
            }
        }
    words = pseg.cut(words)
    for word, flag in words:
        if flag == "dish":
            print(word)
            result["content"]["intentInfos"].append({"name": word, "des": flag, "extra": ""})

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
