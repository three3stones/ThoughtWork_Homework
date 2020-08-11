"""
读取ratings.csv文件，完成：
1. 将每1分做为一档，电影的评分共分为5档，(0:1], (1,2], (2, 3], (3, 4], (4, 5], 通过pandas包求出每个评分档共有多少部电影
2. 添加一个comment列，对平均分4分以上的电影标‘推荐’，其他标‘不推荐’，输出到一个comment.csv中
"""
import pandas as pd
ratings = pd.read_csv("C:/Users/10920/Desktop/ml-latest-small/ratings.csv", header=0)

# 求出每部电影的平均分
ratings['avg_rating'] = ratings.groupby('movieId')['rating'].transform('mean')      # 每条记录都会配置平均分
ratings_avg = ratings[['movieId', 'avg_rating']].drop_duplicates(keep='first')      # 删除重复值，保证电影ID只对应一条记录

# 1. 求出每个评分档共有多少部电影
## 电影分档函数
def rank(rating):
    if 0 < rating <= 1:
        return "(0:1]"
    elif 1 < rating <= 2:
        return "(1,2]"
    elif 2 < rating <= 3:
        return "(2,3]"
    elif 3 < rating <= 4:
        return "(3,4]"
    else:
        return "(4,5]"
ratings_avg['rank'] = ratings_avg['avg_rating'].apply(rank)
result1 = ratings_avg.groupby('rank').agg({'movieId':'count'})
print(result1)

# 2. 添加一个comment列，打标签，输出csv文件
ratings_avg['comment'] = ratings_avg['avg_rating'].apply(lambda x: "推荐" if x > 4 else " 不推荐")
## 不包含行索引
ratings_avg.to_csv("C:/Users/10920/Desktop/ml-latest-small/comment.csv", index=0, encoding='utf_8_sig')
