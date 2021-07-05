from libs.db.dbconn import getconn

def drop_table():
    conn = getconn()  #db 연결 객체
    cur = conn.cursor()
    #테이블 삭제 - SQL(DDL) drop,create,add,
    sql = "drop table member"
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()