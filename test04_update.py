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
# 修改
sql = 'UPDATE t_book set `read`=`read`+1 WHERE `title`="东游记"'
now = cursor.execute(sql)
print('受影响的行为:', now)
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()
