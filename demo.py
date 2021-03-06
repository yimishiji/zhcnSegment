#encoding=utf-8

from zhcnSegment import *

if __name__ == '__main__':
    wds = Seg()

    # 精确分词， 不去出停用词
    seg_list = wds.cut("他来到了网易杭研大厦",False)
    # 他, 来到, 了, 网易, 杭研, 大厦
    print(", ".join(seg_list))

    # 加入用户词典,用户词典中有 ‘网易杭研大厦’
    wds.load_userdict("userdict//userdict.txt")
    seg_list = wds.cut("他来到了网易杭研大厦",False)
    # 他, 来到, 了, 网易杭研大厦
    print(", ".join(seg_list))

    # 精确分词， 去出停用词
    seg_list = wds.cut("他来到了网易杭研大厦")
    # 来到, 网易, 杭研, 大厦
    print(", ".join(seg_list))

    # 全模式
    seg_list = wds.cut("我来到北京清华大学", stopword= False, cut_all=True)
    # 我, 来到, 北京, 清华, 清华大学, 华大, 大学
    print(", ".join(seg_list))

    # 搜索引擎分词
    seg_list = wds.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造",False)
    # 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
    print(", ".join(seg_list))
