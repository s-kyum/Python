#자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn  = getconn()
    cur = conn.cursor()
    #자료추가 - SQL
    cur.execute("insert into member values ('꺼억',18)")   #수정되는게 아니라 추가됨
    cur.execute("insert into member values ('즐라탄',55)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()