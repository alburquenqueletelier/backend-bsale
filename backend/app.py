import os
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = ' mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = ' bsale_test'
app.config['MYSQL_PASSWORD'] = ' bsale_test'
app.config['MYSQL_DB'] = ' bsale_test'
 
mysql = MySQL(app)
 
 
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)