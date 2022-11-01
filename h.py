from flask import Flask, render_template, request, redirect, url_for
import pyodbc
app = Flask(__name__,template_folder='templates')

def connection(query,getResult = True):
    s = 'DESKTOP-EGO85AB\SQLEXPRESS' #Your server name
    d = 'website' # database
    u = 'Jason' #Your login
    p = '123' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    print('CONNECTED!')
    cursor = conn.cursor()
    cursor.execute(query)
    if getResult:
        result = cursor.fetchall()
    else:
        result = None
    conn.commit()
    conn.close()
    return result



@app.route("/", methods=['POST','GET'])
def hello_world():
    # result = connection("insert into customer values ('jason', 'leong', 23, '123000@gmail.com', 'M')",getResult=False)
    result = connection("select * from customer ", getResult=True)
    return render_template('test.html')

@app.route("/result")
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install pyodbc
# C:\Program Files\Microsoft SQL Server (path of sql servers)

