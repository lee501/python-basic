import mysql.connector
conn = mysql.connector.connect(user='', password='', database='')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入数据
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'lee'])

cursor.rowcount 
# =>1

# 提交事物

conn.commit()
cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute('select * from users where id = %s', ('1', ))
values = cursor.fetchall()
cursor.close()

conn.close
