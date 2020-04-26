## Map Reduce

![map reduce](../Images/bigdata/map_reduce.png)



Redis是缓存，围绕着内存和缓存说
Hbase是列式数据库，存在hdfs上，围绕着数据量来说
Hive是数据仓库，是用来分析数据的，不是增删改查数据的。

hive内部表和外部表的区别
内部表：加载数据到hive所在的hdfs目录，删除时，元数据和数据文件都删除
外部表：不加载数据到hive所在的hdfs目录，删除时，只删除表结构。