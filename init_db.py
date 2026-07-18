import sqlite3

def init_database():
    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id   TEXT NOT NULL,
            lesson_id    TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0,
            updated_at   TEXT DEFAULT (datetime('now'))
        )
    """)
    
    conn.commit()
    conn.close()
    print("OK! Baza dannyh sozdana!")

init_database()