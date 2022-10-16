#-------------------------------------------------------------------------------
# Name:        DatabaseCreate
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

# tablo oluşturma
c.execute("""CREATE TABLE rehber (
            ad TEXT,
            soyad Text,
            yas INTEGER,
            boy REAL
            )""")

# yapılan islemi kaydetme
conn.commit()

# bağlantıyı kapatma
conn.close()