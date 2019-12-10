# 导包
import pymysql
# 获取连接对象
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       port=3306,
                       database='books',
                       charset='utf8')
# 获取游标对象
cursor = conn.cursor()
# 执行sql
try:

    sql = 'insert into t_book (`title`,`pub_date`,`read`,`comment`,`is_delete`) values ("东游记","1980-08-12",20,30,0)'
    cursor.execute(sql)
    sql = 'select * from t_book'
    cursor.execute(sql)
    all = cursor.fetchall()
    print(all)
    sql_update = 'UPDATE t_book set `read`=`read`+1 WHERE `title`="东游记"'
    cursor.execute(sql_update)
    # conn.commit()
    conn.autocommit(True)
except:
    conn.rollback()
    print('出现异常我被执行啦')
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()
