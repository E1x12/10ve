from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def hello_login():
    # Get username and match ID and record data, return backend page
    #print(request.form)
    Username = request.form.get('Username')
    MatchCode = request.form.get('MatchCode')
    print(Username,MatchCode)
    #record data

    #input success return backend page 
    return render_template('admin.html')
   

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
