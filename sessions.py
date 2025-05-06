from flask import Flask, flash, render_template, request, make_response, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management


@app.route('/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
         flash(error)
         return render_template('login.html', error = error)
      else:
         session['username'] = request.form['username']
         flash('You were successfully logged in')
         return redirect(url_for('home'))
   else:
      error = 'Invalid request. Please try again!'
      flash(error)
      return render_template('login.html', error = error)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('home'))

if __name__ == '__main__':
   app.run(debug = True)


