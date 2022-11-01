from flask import Flask, render_template, request, redirect, url_for
import pyodbc
app = Flask(__name__,template_folder='templates')

def connection():
    s = 'DESKTOP-EGO85AB\SQLEXPRESS' #Your server name
    d = 'website' # database
    u = 'Jason' #Your login
    p = '123' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    print('CONNECTED!')
    cursor = conn.cursor()

    return conn



@app.route("/", methods=['POST','GET'])
def hello_world():

    conn = connection()
    cursor = conn.cursor()
    # cursor.execute("insert into dbo.customer values ('zero', 'zero_', 23, 'onee@gmail.com', 'M')")
    cursor.execute("SELECT * FROM dbo.customer")
    for i in cursor.fetchall():
        print(i)
    conn.commit() 
    conn.close()
    return render_template('test.html')

@app.route("/result")
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install pyodbc
# C:\Program Files\Microsoft SQL Server (path of sql servers)

