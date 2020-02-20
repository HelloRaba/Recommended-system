# Recommended-system
第一个推荐系统项目  
首先两个例子：UserCF & ItemCF  
###UserCF
实现协同过滤推荐有以下几个步骤：  
&nbsp;&nbsp;&nbsp;&nbsp;1、找出最相似的人或物品：TOP-N相似的人或物品  
&nbsp;&nbsp;&nbsp;&nbsp;2、通过计算两两的相似度来进行排序，即可找出TOP-N相似的人或物品  
&nbsp;&nbsp;&nbsp;&nbsp;3、根据相似的人或物品产生推荐结果  
&nbsp;&nbsp;&nbsp;&nbsp;4、利用TOP-N结果生成初始推荐结果，然后过滤掉用户已经有过记录的物品或明确表示不感兴趣的物品  