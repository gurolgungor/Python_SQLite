#-------------------------------------------------------------------------------
# Name:        DatabaseSelect
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

# cursor oluşturma
c = conn.cursor()

# tablodan sorgulama islemi
c.execute("SELECT * FROM rehber")
print(c.fetchall())

# bağlantıyı kapatma
conn.close()