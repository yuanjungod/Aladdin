# _*_coding:utf-8 _*_
import jieba

jieba.load_userdict("dict_dict.txt")
seg_list = jieba.cut("日式三色串团子")
print(", ".join(seg_list))

