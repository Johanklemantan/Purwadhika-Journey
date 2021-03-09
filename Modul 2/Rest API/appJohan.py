from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

# conda install -c anaconda flask
# conda install -c anaconda flask_mysqldb
# pip install flask_mysqldb

# membuat objek app, sebagai object utama untuk menjalankan API
app = Flask(__name__)

# config untuk terhubung dengan mySQL
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Funicula8'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='flask_mysql'

# config optional. cursor = list / dict
# json_sort = nge sort json berdasarkan alphabeth (kalo default true). kalo false, sesuai urutan file kita
app.config['MYSQL_CURSORCLASS']='DictCursor'
app.config['JSON_SORT_KEYS']=False

#object untuk membuat koneksi terhadap mysql
mysql = MySQL(app)

#start routing
@app.route('/',methods=['GET'])
def home():
    return jsonify({'message':'API is Running'})

@app.route('/employee',methods=['GET','POST'])
def employee():

    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM employee''')
        results = cur.fetchall()
        return jsonify(results)

    elif request.method=='POST':
        #POST UNTUK INSERT DATA
        
        #data yang dikirim saat request akan terdaapt pada request.form
        # data pada request.form diubah jadi dict biar mudah ngelolanya
        form = dict(request.form)

        #menyimpan saetiap satu data yang dikirim ke dalam variable
        username = form['username']
        name = form['name']
        gender = form['gender']
        #data dikirim dalam bentuk string, maka dari itu harus diubah ke bool secara manual
        married = bool(form['married'])

        sql = f'''INSERT INTO employee (username,name,gender,married) VALUES('{username}','{name}','{gender}',{married})'''
        
        cur = mysql.connection.cursor()

        cur.execute(sql)

        mysql.connection.commit()
        cur.close()

        return jsonify({'message':'Insert Success'})

@app.route('/employee/<id>',methods=['GET','PATCH','DELETE'])
def employeeid(id):

    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute(f'''SELECT * FROM employee WHERE id={id}''')
        results = cur.fetchall()
        return jsonify(results)

    elif request.method=='PATCH':
        form = dict(request.form)
        username = form['username']
        name = form['name']
        gender = form['gender']
        married = bool(form['married'])

        sql = f'''UPDATE employee SET username = '{username}', name = '{name}', gender = '{gender}', married = {married} WHERE id = {id}'''
        
        cur = mysql.connection.cursor()

        cur.execute(sql)

        mysql.connection.commit()
        cur.close()

        return jsonify({'message':'Update Success','user id':id})

    elif request.method == 'DELETE':
        sql = f'''DELETE FROM employee WHERE id={id}'''
        cur = mysql.connection.cursor()

        cur.execute(sql)

        mysql.connection.commit()
        cur.close()

        return jsonify({'message' : 'Delete Success', 'user id' : id})
#end routing

#running api
if __name__=='__main__':
    app.run(debug=True, port=1234)