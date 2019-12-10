import pymysql


class SqlUtil:
    __conn = None
    __cursor = None

    # 获取连接对象
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         port=3306,
                                         database='books',
                                         charset='utf8')
        return cls.__conn

    # 获取游标方法
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = SqlUtil.__get_conn().cursor()
        return cls.__cursor

    # 执行sql语句
    @classmethod
    def excute_sql(cls,sql):
        # 判断sql语句是否为查询语句
        if sql.split()[0] == 'select':
            # 是查询语句  游标对象.excute(sql)
            cursor = SqlUtil.__get_cursor()
            cursor.execute(sql)
            # 返回数据
            all = cursor.fetchall()
            # 关闭游标
            SqlUtil.quit_cursor()
            # 关闭连接
            SqlUtil.quit_conn()
            return all
        else:
            try:
                row = SqlUtil.__get_cursor().execute(sql)
                # 如果是查询语句  提交事务
                SqlUtil.__get_conn().commit()
                return row
            except:
                # 回滚
                # SqlUtil.__get_conn().rollback()
                # 关闭游标
                SqlUtil.quit_cursor()
                # 关闭连接
                SqlUtil.quit_conn()



    # 关闭游标对象
    @classmethod
    def quit_cursor(cls):
        if cls.cursor is not None:
            SqlUtil.__get_cursor().close()
            cls.cursor = None

    # 关闭连接对象
    @classmethod
    def quit_conn(cls):
        if cls.conn is not None:
            SqlUtil.__get_conn().close()
            cls.conn = None
