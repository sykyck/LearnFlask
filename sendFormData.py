from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
   return render_template('form.html')

@app.route('/postForm',methods = ['POST', 'GET'])
def displayFormData():
   if request.method == 'POST':
      result = request.form
      return render_template("displayFormData.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)