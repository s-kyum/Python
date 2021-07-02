#특정 회원 검색
from libs.db.dbconn import getconn

def select_one():
    conn = getconn()
    cur = conn.cursor()
    #1명 검색 sql
    sql = "select * from member where name = '투레'"
    cur.execute(sql)
    print("투레 검색")
    #rs = cur.fetchmany(num)
    rs = cur.fetchone()
    '''
    for i in rs:   #1명 조회이니 안씀
        print(i)
    '''
    print(rs)
    conn.close()

if __name__ == "__main__" :
   select_one()