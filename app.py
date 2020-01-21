from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def add():
    return render_template('add.html')


@app.route("/result", methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        result = request.form
        a = int(result['a'])
        b = int(result['b'])
        s = result['op']

        res="hey"

        if s == "+":
            res = a + b
        if s == "-":
            res = a - b
        if s == "*":
            res = a * b
        if s == "/":
            res = a / b

        return render_template("result.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)