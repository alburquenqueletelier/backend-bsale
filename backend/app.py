import os
from flask import Flask,render_template, request, jsonify, json
from flask_mysqldb import MySQL
from flask_cors import CORS
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'bsale_test'
app.config['MYSQL_PASSWORD'] = 'bsale_test'
app.config['MYSQL_DB'] = 'bsale_test'
 
mysql = MySQL(app)

@app.route("/")
def hello_world():
    
    return "<p>Hello, World!</p>"

@app.route("/category")
def get_categories():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * from category''')
        rv = cursor.fetchall()
        response = []
        for row in rv:
            response.append({"id": row[0], "name": row[1]})
        cursor.close()
        return jsonify(response), 200
    except:
        return jsonify({"error": "No fue posible conseguir la data"}), 500

@app.route("/product")
def get_products():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * from product''')
        rv = cursor.fetchall()
        response = []
        for row in rv:
            response.append({"id": row[0], "name": row[1], "url_image": row[2], "price": row[3], "discount": row[4], "category": row[5]})
        cursor.close()
        return jsonify(response), 200
    except:
        return jsonify({"error": "No fue posible conseguir la data"}), 500


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)