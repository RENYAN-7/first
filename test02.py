# 导包
import pymysql

# 获取连接对象
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       autocommit=False,
                       charset="utf8")
# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
sql = "select * from t_book"
cursor.execute(sql)

# 获取第一条数据
# one = cursor.fetchone()
# print(one)

# 获取剩余数据
# all = cursor.fetchall()
# print(all)

# 获取指定前两行的数据
many = cursor.fetchmany(2)
print(many)

count = cursor.rowcount
print("受影响的行数为:", count)
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()
