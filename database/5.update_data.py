#자료 내용 변경
from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "update member set age='22' where name = '둘리'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__" :
    update_data()