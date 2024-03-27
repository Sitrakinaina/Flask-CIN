
import sqlite3

connection = sqlite3.connect('applitest.db')


with open('schema.sql') as f:
        connection.executescript(f.read())
cur = connection.cursor()
cur.execute("INSERT INTO user (nom, prenom,date_de_naissance,lieu_de_naissance,signe,numero,lieu,arrondissement,profession,pere,mere,fait,le) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ('Jean', 'Doe','20 janvier 1995','Besarety ANTANANARIVO III','neant','10126517539522','II M 56 Ambohipo','ANTANANARIVO III','MPianatra','RAZAKA BE','RASOA KELY','ANTANANARIVO III','10 OKTOBRA 2005')
            )



connection.commit()
connection.close()
# import sqlite3

# connection = sqlite3.connect('database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

# connection.commit()
# connection.close()