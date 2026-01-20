from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Needed for flashing messages

# Mock database
users = {"admin": "password123"}

@app.route('/')
def index():
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return f"<h1>Welcome, {username}!</h1>"
        return "Invalid credentials!"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users:
            return "User already exists!"
        
        # Save the new user
        users[username] = password
        return redirect(url_for('login_page'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)