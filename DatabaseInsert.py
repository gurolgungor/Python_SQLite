#-------------------------------------------------------------------------------
# Name:        DatabaseInsert
# Purpose:
#
# Author:      Gürol Güngör
#
# Created:     18.09.2022
# Copyright:   (c) Gürol Güngör 2022
# Licence:     GNU - General Public Licence
#-------------------------------------------------------------------------------

# sqlite kitaplığını kullanma
import sqlite3

# Databse nereye ve hangi isimle olusturulacağı tabnımlanır
database = r"C:\Database\rehber.db"

# bağlantı oluşturma
conn = sqlite3.connect(database)

# cursor olusturma
c = conn.cursor()

# cursor olusturma
c.execute("INSERT INTO rehber VALUES ('Gürol','Güngör', 30, 1.78)")

tum_kayitlar = [
    ('Ahmet','Güngör', 40, 1.79),
    ('Mehmet','Güngör', 50, 1.80),
    ('Nihat','Güngör', 60, 1.85),
]
c.executemany("INSERT INTO rehber VALUES (?,?, ?, ?)", tum_kayitlar)

# commit
conn.commit()

# close the connection
conn.close()