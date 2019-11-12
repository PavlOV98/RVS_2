from flask import Flask, request
import pymysql.cursors
import os

app = Flask(__name__)


#curl -d "numb=2" 127.0.0.1:5000
@app.route("/", methods=['POST'])
def simple():

    conn = pymysql.connect(host=os.environ.get('DB_HOST'),user="user",passwd="password",db=os.environ.get('DB_NAME'))
    cursor = conn.cursor()

    buf = int(request.form.get('numb'))
    cursor.execute('SELECT * FROM list WHERE value=%s', (buf+1,))
    ret = cursor.fetchone()
    if ret != 0:
        return "numb +1 error"
        #return (buf + 1).__str__()
    cursor.execute('SELECT * FROM list WHERE value=%s', (buf,))
    ret = cursor.fetchone()
    if ret == 0:
        cursor.execute('INSERT INTO list (numb) VALUES %s', (buf,))
        #cursor.execute('INSERT INTO list (numb) VALUES %s', (buf-1,))
        conn.commit()
        cursor.close()
        conn.close()
        return (buf+1).__str__()
    print("Numb "+buf.__str__()+" error\n")
    cursor.close()
    conn.close()
    return "numb error"


if __name__ == "__main__":
    app.run()