import pymysql


class Conn:
    conn = None
    cursor = None

    @classmethod
    def create(cls):
        # 获取连接对象
        cls.conn = pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   port=3306,
                                   database='books',
                                   charset='utf8')
        # 获取游标对象
        cls.cursor = cls.conn.cursor()

    @classmethod
    def quit(cls):
        # 关闭游标对象
        cls.cursor.close()
        # 关闭连接对象
        cls.conn.close()
