import sqlite3

DB_NAME = "f7bot.db"


def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guild_settings (
            guild_id INTEGER PRIMARY KEY,
            enabled INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def enable_guild(guild_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO guild_settings
        (guild_id, enabled)
        VALUES (?, 1)
    """, (guild_id,))

    conn.commit()
    conn.close()


def disable_guild(guild_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO guild_settings
        (guild_id, enabled)
        VALUES (?, 0)
    """, (guild_id,))

    conn.commit()
    conn.close()


def is_enabled(guild_id: int):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT enabled
        FROM guild_settings
        WHERE guild_id = ?
    """, (guild_id,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return False

    return row[0] == 1
