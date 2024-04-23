from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    birthdate = request.form['birthdate']
    color = request.form['color']
    vacation = request.form['vacation']
    
    # Do something with the form data, like printing it
    print("Birthdate:", birthdate)
    print("Favorite Color:", color)
    print("Dream Vacation:", vacation)
    
    # You can also process the data further, like storing it in a database
    
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
