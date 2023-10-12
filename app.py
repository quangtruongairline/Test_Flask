from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    # return render_template('index.html', content="Thanh dep trai!",
    #                        cars=["Vinfast", "BMW", "Mer"])
    return render_template("index.html")

@app.route('/admin')
def hello_admin():
    return "<h1> Hello Admin</h1>"

@app.route('/user/<name>')
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_admin"))
    return f"<h1> Hello {name} </h1>"

if __name__ == "__main__":
    app.run(debug=True)