from flask import Flask,request,render_template,url_for
import math
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("base.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/help',methods=['POST'])
def help():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    a=(int(str(a)))
    b = (int(str(b)))
    c = (int(str(b)))
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'У этого уравнения нет корней'
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return f'Уравнение имеет один корень {x}'
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print
        return f'Уравнение имеет два корня: {x1}, " и", {x2}'
