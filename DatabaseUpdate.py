#-------------------------------------------------------------------------------
# Name:        module1
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

# tabloda update islemi
c.execute("UPDATE rehber SET ad='Niyazi' WHERE ad='Ahmet'")

# commit
conn.commit()

# bağlantıyı kapatma
conn.close()