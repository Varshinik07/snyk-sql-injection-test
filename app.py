import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # 🔥 VULNERABLE: SQL injection via unescaped user input
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
