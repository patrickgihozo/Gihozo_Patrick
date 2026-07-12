from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username =="patrick" and password == "1234":
            return render_template("welcome.html",username=username)
        
        return "Wrong Username or Password"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
