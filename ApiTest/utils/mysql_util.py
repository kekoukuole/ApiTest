import pymysql
from utils.log_util import logger

from utils.read import base_data

data = base_data.read_ini()["mysql"]
DB_CONF = {
    "host":data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]

}
class MysqlDb:
    def __init__(self):
        #连接
        self.conn = pymysql.connect(**DB_CONF,autocommit=True)
        #创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        #释放资源
        self.cur.close()
        self.conn.close()

    #查询一条数据
    def select_db_one(self,sql):
        logger.info(f"执行sql:{sql}")
        self.cur.execute(sql)
        #获取数据
        return self.cur.fetchone()

    #查询多条数据
    def select_db(self,sql):
        logger.info(f"执行sql:{sql}")
        self.cur.execute(sql)
        #获取数据
        return self.cur.fetchall()

    #执行sql
    def execute_db(self,sql):
        try:
            logger.info(f"执行sql:{sql}")
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))

db = MysqlDb()

if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db("SELECT code from users_verifycode WHERE  mobile = 15000000000 order by id desc limit 1")
    print(result[0]["code"])