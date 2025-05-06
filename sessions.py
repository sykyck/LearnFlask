from flask import Flask, render_template, request, make_response, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management


@app.route('/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('home'))
   return render_template('login.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('home'))

if __name__ == '__main__':
   app.run(debug = True)


