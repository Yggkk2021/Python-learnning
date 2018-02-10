# 数据库支持入门
import sqlite3
# # 创建一个数据库的连接，如果文件不存在就会自动生成，通过一个文件名，如下面的：somedatabase.db
# conn = sqlite3.complete_statement('somedatabase.db')
# # 之后能获得连接的游标,这是一种操作数据库的对象
# curs = conn.cursor()
# # 将数据操作提交到数据库
# conn.commit()
# # 关闭数据库
# conn.close()

# 将数据导入数据库
# 转换方法
def convert(value):
    if value.startwith('='):
        # strip()移除字段指定的字符，默认为空
        return value.strip('-')
    # 如果value为空
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.close()

# 执行下面的数据库语句
curs.execute('''
CREATE TABLE food (
id  TEXT    PRIMARY KEY,
desc    TEXT,
water   FLOAT,
kcal    FLOAT,
protein FLOAT
)
''')

query = 'INSERT INTO food VALUE (?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.strip('^')
    vals = [convert(f) for f in fields[:fields.__len__()]]
    curs.execute(query,vals)

conn.commit()
conn.close()