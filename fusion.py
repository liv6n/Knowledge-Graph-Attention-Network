import numpy as np
import jieba
#读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 加载停用词
stopwords = stopwordslist("cn_stopwords.txt")


def cosine_similarity(sentence1: str, sentence2: str) -> float:
    """
    :param sentence1: s
    :param sentence2:
    :return: 两句文本的相识度
    """
    seg1 = [word for word in jieba.cut(sentence1) if word not in stopwords]
    seg2 = [word for word in jieba.cut(sentence2) if word not in stopwords]
    word_list = list(set([word for word in seg1 + seg2]))#建立词库
    word_count_vec_1 = []
    word_count_vec_2 = []
    for word in word_list:
        word_count_vec_1.append(seg1.count(word))#文本1统计在词典里出现词的次数
        word_count_vec_2.append(seg2.count(word))#文本2统计在词典里出现词的次数


    vec_1 = np.array(word_count_vec_1)
    vec_2 = np.array(word_count_vec_2)
    #余弦公式


    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos


    return sim
'''
str1="刘德华1961年9月27日出生于中国香港，籍贯广东新会，华语影视男演员、歌手、制片人、作词人。"
str2="华仔参加了安徽国剧盛典颁奖晚会"
str3= "华仔1961年9月27日出生于中国香港，籍贯广东新会，华语影视男演员、歌手、制片人、作词人。1981年出演电影处女作《彩云曲》"
'''
sim1=cosine_similarity(str1,str2)
sim2=cosine_similarity(str1,str3)
print("sim1 ：",sim1)
print("sim2:",sim2)
