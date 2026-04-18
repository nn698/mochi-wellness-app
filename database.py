import sqlite3

def create_connection():
    conn = sqlite3.connect("fitness_app.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS period_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        last_period_date TEXT,
        cycle_length INTEGER
    )
    """)



    # New table for BMI/Calories
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        bmi REAL,
        daily_calories INTEGER,
        log_date TEXT
    )""")

    conn.commit()
    conn.close()


def add_period_entry(user_name, last_period_date, cycle_length):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO period_history (user_name, last_period_date, cycle_length)
    VALUES (?, ?, ?)
    """, (user_name, last_period_date, cycle_length))
    
    conn.commit()
    conn.close()


def get_user_history(user_name):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM period_history WHERE user_name = ?", (user_name,))
    rows = cursor.fetchall()
    
    conn.close()
    return rows
    


    


