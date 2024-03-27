# from app import app
# import pymysql
# from flask import jsonify
# db = pymysql.connect(
#     host=app.config['MYSQL_HOST'],
#     user=app.config['MYSQL_USER'],
#     password=app.config['MYSQL_PASSWORD'],
#     db=app.config['MYSQL_DB']
# )
# @app.route('/')
# def get_users():
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM user")
#     users = cursor.fetchall()
#     cursor.close()
#     return jsonify(users)