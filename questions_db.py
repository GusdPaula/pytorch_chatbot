import sqlite3


def insert_into(question):

    conn = sqlite3.connect('questions_not_known.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT count from questions WHERE question = ? ', (question,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO questions (question, count)
                    VALUES (?, 1)''', (question,))
    else:
        cur.execute(
            'UPDATE questions SET count = count + 1 WHERE question = ?', (question,))
    conn.commit()
    cur.close
