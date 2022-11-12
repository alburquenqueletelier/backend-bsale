import os
from flask import Flask,render_template, request, jsonify, json
from flask_mysqldb import MySQL
from flask_cors import CORS

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = HOST
app.config['MYSQL_USER'] = USER
app.config['MYSQL_PASSWORD'] = PASSWORD
app.config['MYSQL_DB'] = DATABASE

CORS(app)
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/category")
def get_categories():
    id = request.args.get('id', None)
    name = request.args.get('name', None)
    try:
        cursor = mysql.connection.cursor()
        if id:
            cursor.execute(f'''SELECT * FROM category WHERE id="{id}" LIMIT 1''')
        elif name:
            name=name.replace('+', ' ')
            cursor.execute(f'''SELECT * FROM category WHERE name="{name}" LIMIT 1''')
        else:
            cursor.execute('''SELECT * FROM category''')
        rv = cursor.fetchall()
        response = []
        for row in rv:
            response.append({"id": row[0], "name": row[1]})
        cursor.close()
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "No fue posible conseguir la data"}), 500

@app.route("/product")
def get_products():
    id = request.args.get('id', None)
    name = request.args.get('name', None)
    category = request.args.get('category', None) # int
    try:
        cursor = mysql.connection.cursor()
        if id:
            cursor.execute(f'''SELECT * FROM product WHERE id="{id}" LIMIT 1''')
        elif name:
            name=name.replace('+', ' ')
            cursor.execute(f'''SELECT * from product WHERE name="{name}"''')
        elif category:
            cursor.execute(f'''SELECT * from product WHERE category="{category}"''')
        else:
            cursor.execute('''SELECT * from product''')
        rv = cursor.fetchall()
        if not rv:
            return jsonify({"empty": "No se encuentra lo que buscas"})
        response = []
        for row in rv:
            response.append({"id": row[0], "name": row[1], "url_image": row[2], "price": row[3], "discount": row[4], "category": row[5]})
        cursor.close()
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "No fue posible cargar productos"}), 500


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)