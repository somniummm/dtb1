import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute ("""CREATE TABLE IF NOT EXISTS fio (
    frstnm TEXT,
    scdnm TEXT,
    trdnm TEXT
)""")

db.commit()
def reg():
    user_frstnm = input('frstnm: ')
    user_scndnm = input('scdnm: ')
    user_trdnm = input('trdnm: ')

    sql.execute("SELECT frstnm FROM fio WHERE frstnm = '{frstnm}'")
    if sql.fetchone() is None: 
        sql.execute("INSERT INTO fio VALUES (?, ?, ?)", (fio_frstnm, fio_scdnm, fio_trdnm))
        db.commit()
        print('Зарегестрировано')
    
