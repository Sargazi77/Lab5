import sqlite3
 
conn = sqlite3.connect('database.sqlite')
conn.execute('CREATE TABLE IF NOT EXISTS users (name text, country text, catches int)')
conn.execute('INSERT INTO users values (? , ?, ?)', ("Janne Mustonen","Finland","98"))
conn.execute('INSERT INTO users values (? , ?, ?)', ("Ian Stewart","Canada","94"))
 
 
def add_user_to_db(name,country,catches):
    with sqlite3.connect("database.sqlite") as conn:
        conn.execute('INSERT INTO users values (? , ?, ?)', (name,country,catches))  
    conn.close()
def show_All():
    with sqlite3.connect("database.sqlite") as conn:
        display = conn.execute('SELECT * FROM users')
    return display    
    conn.close()
 
def search(name):
    with sqlite3.connect("database.sqlite") as conn:
        try:
            find = conn.execute(f'SELECT * FROM users where name = {name}')
        except:
            return False   
    return find
    conn.close()    
 
 
 
 
 
 
conn.commit()