# _*_coding:utf-8 _*_
import logging
import fasttext
# jieba.load_userdict("dict_dict.txt")
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# 训练模型
classifier = fasttext.supervised(
    "fast_test_train.txt", "news_fasttext1.model", label_prefix="__label__", lr=0.1, epoch=100, dim=200, bucket=5000000)


classifier = fasttext.load_model('news_fasttext1.model.bin', label_prefix='__label__')
result = classifier.predict_proba(["不要 BBQ松蘑鸡胸"])
print result[0][0][0], result[0][0][1]

# load训练好的模型
# classifier = fasttext.load_model('news_fasttext.model.bin', label_prefix='__label__')
# labels_right = []
# texts = []
# with open("news_fasttext_test.txt") as fr:
#     for line in fr:
#         line = line.decode("utf-8").rstrip()
#         labels_right.append(line.split("\t")[1].replace("__label__", ""))
#         texts.append(line.split("\t")[0])
        # break
    #     print labels
    #     print texts
#     break
# print(texts)
# labels_predict = [e[0] for e in classifier.predict(texts)]  # 预测输出结果为二维形式
# print(len(labels_predict))
# # print labels_predict
#
# text_labels = list(set(labels_right))
# text_predict_labels = list(set(labels_predict))
# print(text_predict_labels)
# print(text_labels)

