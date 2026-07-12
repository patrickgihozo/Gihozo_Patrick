from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return '<h1>Welcome to Flask Framework </h2>'
@app.route('/about')

def about():
    return '<h1> Flask is ma favorite</h1>'

@app.route('/Contact')
#Route to contact
def Contact():
    return '<h1> Welcome to Contact page </h1>'
 
#Dynamic Routing 
@app.route('/contact')
def contact():
    page_title = "Contact Us"
    name = "Patrick"
    email = "support@example.com"
    phone = "+250 700 000 000"
    services = ["Web Development", "Graphic designs", "Training", "Support"]
    return render_template(
        'Contact.html',
        page_title=page_title,
        name=name,
        email=email,
        phone=phone,
        services=services
    )

@app.route("/myStory/<name>")
def myStory(name):
    return f"Welcome to {name}Page"

@app.route("/student/<name>")
def student(name):
    return f"Welcome {name}"

if __name__ =='__main__':
    app.run(debug=True)