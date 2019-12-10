from postting.script import SqlUtil
# sql = 'select * from t_book'
# sql = 'delete from t_book where `title`="东游记"'
sql = 'insert into t_book (`title`,`pub_date`,`read`,`comment`,`is_delete`) values ("东游记","1980-08-12",20,30,0)'
SqlUtil.excute_sql(sql)

