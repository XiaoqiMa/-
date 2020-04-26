# SQL基础
模式定义了数据如何存储、存储什么样的数据以及数据如何分解等信息，数据库和表都有模式。
主键的值不允许修改，也不允许复用（不能将已经删除的主键值赋给新数据行的主键）。

 从SQL的角度来看，视图和表是相同的，两者的区别在于表中保存的是实 际的数据，而视图中保存的是 SELECT 语句(视图本身并不存储数据)
创建视图的CREATE VIEW语句 
CREATE VIEW 视图名称(<视图列名1>, <视图列名2>, ......) AS

`<select 语句>`


![image-20200426114336807](/Users/xiaoqi/Library/Application Support/typora-user-images/image-20200426114336807.png)

函数大致可以分为以下几种。 
● 算术函数(用来进行数值计算的函数)
● 字符串函数(用来进行字符串操作的函数)
 ● 日期函数(用来进行日期操作的函数)
	获得当前日期+时间（date + time）函数：now()
	获得当前时间戳函数：`current_timestamp, current_timestamp()`
	Str to Date （字符串转换为日期）函数：`str_to_date(str, format)`
	日期、时间相减函数：`datediff(date1,date2), timediff(time1,time2)`
	为日期增加一个时间间隔：`date_add()`
	为日期减去一个时间间隔：`date_sub()`

● 转换函数(用来转换数据类型和值的函数) 
● 聚合函数(用来进行数据聚合的函数) 

通俗来讲谓词就是 6-1 节中介绍的函数中的一种，是需要满足特定条 件的函数，该条件就是返回值是真值。对通常的函数来说，返回值有可能 是数字、字符串或者日期等，但是谓词的返回值全都是真值(TRUE/ FALSE/UNKNOWN)。这也是谓词和函数的最大区别。 
本节将会介绍以下谓词。 
● LIKE
● BETWEEN
● IS NULL、IS NOT NULL 
● IN
● EXISTS 

Case 表达式
●  CASE表达式分为简单CASE表达式和搜索CASE表达式两种。搜索 CASE 表达式包含简单 CASE 表达式的全部功能。
搜索 CASE 表达式 
CASE    WHEN <求值表达式> THEN <表达式> 
	WHEN <求值表达式> THEN <表达式> 
	WHEN <求值表达式> THEN <表达式> 
	. . . 
	ELSE <表达式> 
END 
<img src="/Users/xiaoqi/Library/Application Support/typora-user-images/image-20200426114416434.png" alt="image-20200426114416434" style="zoom: 25%;" />

联结(JOIN)就是将其他表中的列添加过来，进行“添加列”的集合运算。 UNION 是以行(纵向)为单位进行操作，而联结则是以列(横向)为单位 进行的。 
内联结(INNER JOIN) 
SELECT SP.shop_id, SP.shop_name, SP.product_id, P.product_name, P.sale_price _
FROM ShopProduct AS SP 
INNER JOIN Product AS P  
ON SP.product_id = P.product_id; 
进行内联结时必须使用 ON 子句，并且要书写在 FROM 和 WHERE 之间。 

对于外联结来说，只要数据存在于某一张表当中，就能够读取 出来。在实际的业务中，例如想要生成固定行数的单据时，就需要使用外 联结

对满足相同规则的表进行交叉联结的集合运算符是CROSS JOIN(笛卡 儿积)。进行交叉联结时无法使用内联结和外联结中所使用的 ON 子句， 这是因为交叉联结是对两张表中的全部记录进行交叉组合，因此结果中 的记录数通常是两张表中行数的乘积。

● 1 行注释 书写在“--”之后，只能写在同一行。
● 多行注释书写在“/*”和“*/”之间，可以跨多行。

子句的书写顺序 
1.SELECT子句→2.FROM子句→3.WHERE子句→4.GROUP BY子句→ 5. HAVING 子句 → 6. ORDER BY 子句 

使用 HAVING 子句时 SELECT 语句的顺序 FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY  一定要记住 SELECT 子 句的执行顺序在 GROUP BY 子句之后，ORDER BY 子句之前

drop, delete与truncate的区别
参考答案：
drop直接删掉表 truncate删除表中数据，再插入时自增长id又从1开始 delete删除表中数据，可以加where字句。
（1） DELETE语句执行删除的过程是每次从表中删除一行，并且同时将该行的删除操作作为事务记录在日志中保存以便进行进行回滚操作。TRUNCATE TABLE 则一次性地从表中删除所有的数据并不把单独的删除操作记录记入日志保存，删除行是不能恢复的。并且在删除的过程中不会激活与表有关的删除触发器。执行速度快。
（2） 表和索引所占空间。当表被TRUNCATE 后，这个表和索引所占用的空间会恢复到初始大小，而DELETE操作不会减少表或索引所占用的空间。drop语句将表所占用的空间全释放掉。
（3） 一般而言，drop > truncate > delete
（4） 应用范围。TRUNCATE 只能对TABLE；DELETE可以是table和view
（5） TRUNCATE 和DELETE只删除数据，而DROP则删除整个表（结构和数据）。
（6） truncate与不带where的delete ：只删除数据，而不删除表的结构（定义）drop语句将删除表的结构被依赖的约束（constrain),触发器（trigger)索引（index);依赖于该表的存储过程/函数将被保留，但其状态会变为：invalid。
（7） delete语句为DML（data maintain Language),这个操作会被放到 rollback segment中,事务提交后才生效。如果有相应的 trigger,执行的时候将被触发。
（8） truncate、drop是DLL（data define language),操作立即生效，原数据不放到 rollback segment中，不能回滚
（9） 在没有备份情况下，谨慎使用 drop 与 truncate。要删除部分数据行采用delete且注意结合where来约束影响范围。回滚段要足够大。要删除表用drop;若想保留表而将表中数据删除，如果于事务无关，用truncate即可实现。如果和事务有关，或想触发trigger,还是用delete。
（10） Truncate table 表名 速度快,而且效率高,因为: truncate table 在功能上与不带 WHERE 子句的 DELETE 语句相同：二者均删除表中的全部行。但 TRUNCATE TABLE 比 DELETE 速度快，且使用的系统和事务日志资源少。DELETE 语句每次删除一行，并在事务日志中为所删除的每行记录一项。TRUNCATE TABLE 通过释放存储表数据所用的数据页来删除数据，并且只在事务日志中记录页的释放。
（11） TRUNCATE TABLE 删除表中的所有行，但表结构及其列、约束、索引等保持不变。新行标识所用的计数值重置为该列的种子。如果想保留标识计数值，请改用 DELETE。如果要删除表定义及其数据，请使用 DROP TABLE 语句。
（12） 对于由 FOREIGN KEY 约束引用的表，不能使用 TRUNCATE TABLE，而应使用不带 WHERE 子句的 DELETE 语句。由于 TRUNCATE TABLE 不记录在日志中，所以它不能激活触发器

• limit y 分句表示: 读取 y 条数据
• limit x, y 分句表示: 跳过 x 条数据，读取 y 条数据
• limit y offset x 分句表示: 跳过 x 条数据，读取 y 条数据



### 参考资料

SQL必知必会