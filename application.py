from abc import ABC, abstractmethod
from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        with sqlite3.connect("checkout") as conn:
            command = "INSERT INTO stuff VALUES(?, ?, ?)"
            data_list = []
            data_list.append('')
            data_list.append(1)
            data_list.append('')
            conn.execute(command, data_list)
            conn.commit()
        return render_template("home.html")
    else:
        return render_template("home.html")


@app.route('/filler_arc', methods=['POST'])
def filler():
    pizza_in = request.args.get('group1')
    if pizza_in == 'input1':
        pizza = "Sicilian"
        price = "$7"
    elif pizza_in == 'input2':
        pizza = "Marine"
        price = "$7"
    elif pizza_in == 'input3':
        pizza = "Neapolitan"
        price = "$7"
    elif pizza_in == 'input4':
        pizza = "Mixed"
        price = "$8"
    with sqlite3.connect("checkout") as conn:
        command = "INSERT INTO stuff VALUES(?, ?, ?)"
        data_list = []
        data_list.append(pizza)
        data_list.append(1)
        data_list.append(price)
        conn.execute(command, data_list)
        conn.commit()
    return render_template("filler.html")


@app.route('/checkout', methods=['POST'])
def order():
    with sqlite3.connect("checkout") as conn:
        command1 = "SELECT * FROM stuff"
        cursor1 = conn.execute(command1)
        table_assignments = cursor1.fetchall()
    render_template("checkout.html", table_assignments=table_assignments)


if __name__ == "__main__":
    app.run(debug=True)
