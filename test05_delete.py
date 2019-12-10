# 导包
import pymysql
# 获取连接对象
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       port=3306,
                       database='books',
                       autocommit=True,
                       charset='utf8')
# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
# 删除title叫东游记的信息
sql = 'delete from t_book where `title`="东游记"'
cursor.execute(sql)
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()
