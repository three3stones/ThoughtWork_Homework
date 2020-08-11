"""
对数据集中的3个csv文件进行聚合，生成一个csv，包含电影的信息，其中每部电影一行，信息包括电影名称、主演、平均分、所有tag
"""
import pandas as pd
pd.set_option('display.max_colwidth', 50000)
# 1. 读入csv文件   文件存放路径 C:\Users\10920\Desktop\ml-latest-small
movies = pd.read_csv("C:\\Users\\10920\\Desktop\\ml-latest-small\\movies.csv", header=0)
ratings = pd.read_csv("C:\\Users\\10920\\Desktop\\ml-latest-small\\ratings.csv", header=0)
tags = pd.read_csv("C:\\Users\\10920\\Desktop\\ml-latest-small\\tags.csv", header=0)

# 2. 单个csv文件进行聚合汇总  确保电影ID的唯一性
# 2.1 求出电影的平均分
ratings['avg_rating'] = ratings.groupby('movieId')['rating'].transform('mean')   # 每条记录都会配置平均分
ratings1 = ratings[['movieId', 'avg_rating']].drop_duplicates(keep='first')      # 删除重复值，保证电影ID只对应一条记录

# 2.2 求出电影的所有tag
def agg_tag(x):
    tag_list = []
    for i in x:
        if i not in tag_list:
            tag_list.append(i)
        else:
            continue
    return '|'.join(tag_list)

tags1 = tags.groupby('movieId').agg({'tag': agg_tag})
tags1['movieId'] = tags1.index                  # 将movieId索引改为列

# 3. 对三个csv文件进行连接
join_mid = pd.merge(movies, ratings1, how='left', on='movieId')
join_res = pd.merge(join_mid, tags1, how='left', on='movieId')
result = join_res[['movieId', 'title', 'avg_rating', 'tag']]
print(result)
