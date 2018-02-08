# 数据库支持入门
import sqlite3
# 创建一个数据库的连接，如果文件不存在就会自动生成，通过一个文件名，如下面的：somedatabase.db
conn = sqlite3.complete_statement('somedatabase.db')
# 之后能获得连接的游标,这是一种操作数据库的对象
curs = conn.cursor()
# 将数据操作提交到数据库
conn.commit()
# 关闭数据库
conn.close()