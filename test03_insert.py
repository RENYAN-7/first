# 导包
import pymysql
# 获取连接对象
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       port=3306,
                       autocommit=True,
                       charset='utf8')
# 获取游标对象
cursor = conn.cursor()
# 执行sql
sql = 'insert into t_book (`title`,`pub_date`,`read`,`comment`,`is_delete`) values ("东游记","1980-08-12",20,30,0)'
cursor.execute(sql)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
