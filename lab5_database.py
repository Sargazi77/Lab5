import sqlite3
 
conn = sqlite3.connect('database.sqlite')
conn.execute('DROP TABLE users')
 
conn.execute('CREATE TABLE IF NOT EXISTS users (name text, country text, catches int)')
 
def add_user_to_db(name,country,catches):
    with sqlite3.connect("database.sqlite") as conn:
        conn.execute('INSERT INTO users values (? , ?, ?)', (name,country,catches))  
    conn.close()
def show_All():
    with sqlite3.connect("database.sqlite") as conn:
        display = conn.execute('SELECT * FROM users')
    return display    
    conn.close()
 
 
 
 
conn.commit()
 
 
 