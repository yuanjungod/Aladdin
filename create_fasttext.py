import jieba
import os
jieba.load_userdict("dict_dict.txt")
ftrain = open("news_fasttext_train.txt", "w")

fh = open('train.txt')
for text in fh.readlines():
    text = text.decode("utf-8").encode("utf-8")
    try:
        label, text = text.split("--------")
    except:
        print("fuck")
        continue
    seg_text = jieba.cut(text.replace("\t", " ").replace("\n", " "))
    outline = " ".join(seg_text)
    outline = outline.encode("utf-8") + "\t__label__" + label + "\n"
    ftrain.write(outline)
    ftrain.flush()
fh.close()
ftrain.close()

