import random
from flask import *
import sqlite3

app = Flask(__name__)
order_num = 0


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == "POST":
        with sqlite3.connect("checkout") as conn:
            command = "INSERT INTO stuff VALUES(?, ?, ?, ?, ?, ?)"
            data_list = []
            additions = ""
            data_list.append(request.form["name"])
            data_list.append(request.form["address"])
            data_list.append(request.form["pizza"])

            additions += "Green Pepper, " if request.form.get("green_pepper", None) is not None else ""
            additions += "Mushroom, " if request.form.get("mushroom", None) is not None else ""
            additions += "Tomato, " if request.form.get("tomato", None) is not None else ""
            additions += "Pickle, " if request.form.get("pickle", None) is not None else ""
            additions += "Pineapple, " if request.form.get("pineapple", None) is not None else ""
            additions += "Olive, " if request.form.get("olive", None) is not None else ""
            data_list.append(additions)

            data_list.append(request.form["total"])
            data_list.append(request.form["calorie"])
            conn.execute(command, data_list)
            conn.commit()
        return render_template("order.html")
    else:
        return render_template("order.html")


@app.route('/checkout')
def checkout():
    with sqlite3.connect("checkout") as conn:
        command1 = "SELECT * FROM stuff"
        cursor1 = conn.execute(command1)
        table_assignments = cursor1.fetchall()
    return render_template("checkout.html", table_assignments=table_assignments)


@app.route('/finished')
def getmeout():
    global order_num
    order_num += 1
    return render_template("finished.html", order_num=order_num)


@app.route('/delete_order')
def delete():
    with sqlite3.connect("checkout") as conn:
        command2 = "DELETE FROM stuff"
        cursor2 = conn.execute(command2)
        table_assignments = cursor2.fetchall()
        return render_template("delete.html", table_assignments=table_assignments)


@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
