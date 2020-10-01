from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def add():
    return render_template('add.html')

# this is for nothing
@app.route("/result", methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        result = request.form
        a = int(result['a'])
        b = int(result['b'])
        s = result['op']
        # this is for nothing
        res="hey"
        # this is for nothing
        if s == "+":
            res = a + b
        if s == "-":
            res = a - b
        if s == "*":
            res = a * b
        if s == "/":
            res = a / b
        # this is for nothing
        return render_template("result.html", res=res)

# this is for nothing
if __name__ == '__main__':
    app.run(debug=True)
