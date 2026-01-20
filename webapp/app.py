from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (In a real app, you'd use a real database)
USER_DATA = {"admin": "password123"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # 1. Get data from the HTML form
    username = request.form.get('username')
    password = request.form.get('password')

    # 2. Check if credentials match our "database"
    if username in USER_DATA and USER_DATA[username] == password:
        return f"Welcome, {username}! Login Successful."
    else:
        return "Invalid Credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)