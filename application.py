from abc import ABC, abstractmethod
from flask import *


class CustomerInfo:
    name = ""
    address = ""
    pizza_type = []
    pizza_topping = []
    price = 0
    number_of_pizza = 0
    total = 0
    calorie = 0


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", info=CustomerInfo)


@app.route('/order_placed')
def order():
    render_template("orderfinish.html")


if __name__ == "__main__":
    app.run(debug=True)
