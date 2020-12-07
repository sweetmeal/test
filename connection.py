import pymysql
import json
import datetime

# 접속
# 비밀번호가 포함되어 있기 때문에 보통 config파일에서 key값으로 부른다.
db = pymysql.connect(
                    host='127.0.0.1', 
                    port=3306, 
                    user='root', 
                    passwd='winwin1234', 
                    db='winwin', 
                    charset='utf8'
                    )

# Cursor Object 가져오기
cursor = db.cursor()

# SQL 문 만들기
# sql = '''
#             CREATE TABLE gytable (
#                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
#                    name VARCHAR(20) NOT NULL,
#                    model_num VARCHAR(10) NOT NULL,
#                    model_type VARCHAR(10) NOT NULL,
#                    PRIMARY KEY(id)
#             );
#         '''



# cursor.execute("INSERT INTO winwin.Member VALUES ('coffee', '1234', 'coffee')")

# resultMember = cursor.execute("SELECT * FROM Member")
# print(resultMember)

# resultMemberAll = cursor.fetchall()
# print(resultMemberAll)




# try:
#     with db.cursor() as cursor:
#         sql = "SELECT * FROM Member WHERE name = 'kgy'"
#         cursor.execute(sql)

#         result = cursor.fetchone()
#         print(result)
#         print("값 불러오기")
# finally:
#     db.close()



# SQL 실행하기
#cursor.execute(sql)

# 실행 mysql 서버에 확정 반영하기
db.commit()

# DB 연결 닫기
db.close()





def handler(event, context):
    data = {
        'userId': 'jiny',
        'password': '1234',
        'name': 'jiny'

    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}