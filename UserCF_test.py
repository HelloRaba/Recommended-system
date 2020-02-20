"""
@author: guanpingan
@contact: 16608166124@163.com
@software: PyCharm
@file: UserCF_test.py
@time: 2020/2/20 18:39
"""
import pandas as pd
import numpy as np
from pprint import pprint
#pprint  打印出的内容带有完整的数据结构，每行一个数据结构，方便阅读。当数据较长较多时适用。
users = ["User1", "User2", "User3", "User4", "User5"]
items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
# 用户购买记录数据集
datasets = [
    [1,0,1,1,0],
    [1,0,0,1,1],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,1,1,0,1],
]
df = pd.DataFrame(datasets,
                  columns=items,
                  index=users)

# 计算所有的数据两两的杰卡德相似系数
from sklearn.metrics.pairwise import pairwise_distances
# # 计算用户间相似度  1-杰卡德距离=杰卡德相似度
user_similar = 1 - pairwise_distances(df.values, metric="jaccard")
user_similar = pd.DataFrame(user_similar, columns=users, index=users)
print("用户之间的两两相似度：")
print(user_similar)

topN_users = {}
# 遍历每一行数据
for i in user_similar.index:
    # 取出每一列数据，并删除自身，然后排序数据
    _df = user_similar.loc[i].drop([i])
    #sort_values 排序 按照相似度降序排列
    _df_sorted = _df.sort_values(ascending=False)
    # 从排序之后的结果中切片 取出前两条（相似度最高的两个）
    top2 = list(_df_sorted.index[:2])
    topN_users[i] = top2

print("Top2相似用户：")
pprint(topN_users)

# 准备空白dict用来保存推荐结果
rs_results = {}
#遍历所有的最相似用户
for user, sim_users in topN_users.items():
    rs_result = set()    # 存储推荐结果
    for sim_user in sim_users:
        # 构建初始的推荐结果
        rs_result = rs_result.union(set(df.loc[sim_user].replace(0,np.nan).dropna().index))
        #把0过滤掉，只留下1，因为1代表喜欢过。
    # 过滤掉已经购买过的物品
    rs_result -= set(df.loc[user].replace(0,np.nan).dropna().index)
    rs_results[user] = rs_result
print("最终推荐结果：")
pprint(rs_results)

"""
技术栈总结：
1、pprint格式化输出；
2、多维数组可以指定行列的名称转为DataFrame表格，关键字分别是index和columns；
3、在sklearn.metrics包里封装了杰卡德距离计算功能，其相似度系数=1-杰卡德距离；
4、pandas.DataFrame中loc根据行名或列名取表格中的内容，iloc用具体位置获取；
5、DataFrame中删除0的方法：df.replace(0,np.nan).dropna();先替换为np.nan后用dropna()过滤np.nan；
6、sort_values排序函数，默认升序，降序修改ascending参数；
7、集合set的union取两个集合的并集并去重；集合可以用减号删除元素。
"""