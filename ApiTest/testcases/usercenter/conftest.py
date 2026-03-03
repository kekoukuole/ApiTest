#获取短信验证码
import logging

from utils.mysql_util import db

#获取验证码
def get_code(mobile):
    sql = "SELECT code from users_verifycode WHERE  mobile = '%s' order by id desc limit 1;" % mobile
    result = db.select_db_one(sql)
    logging.info(f"sql执行结果：{result}")
    return result["code"]

#s删除用户
def delete_user(mobile):
    sql = "DELETE FROM users_userprofile WHERE mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logging.info(f"sql执行结果：{result}")

#删除用户验证码
def delete_code(mobile):
    sql = "delete from users_verifycode where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logging.info(f"sql执行结果：{result}")