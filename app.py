from flask import Flask, render_template
import requests # import Flask class from flask module and render_template to render html files
from dotenv import load_dotenv
load_dotenv()                         # load environment variables from .env file
import os
apikey = os.getenv("APIKEY")               
app = Flask(__name__)
url="https://api.api-ninjas.com/v1/quotes"
headers={'X-Api-Key':apikey}

def get_quote():
    response=requests.get(url,headers=headers)
    data = response.json()
    if isinstance(data, list) and len(data)>0:
        quote_val =  data[0]['quote']
        author_val = data[0]['author']
        category_val = data[0]['category']
        return quote_val , author_val, category_val
    else:
        return "No quote found", "Unknown", "Unknown"
app=Flask(__name__)
@app.route('/')             #app.route is decorator
def home():
    quote, author, category = get_quote()
    return render_template('ai_quote.html', quote1=quote, author1=author, category1=category) 



@app.route('/register')
def registerpage():
    return render_template('register.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)

#app.run(use_reloader=True)                                      #fastapi and flask are web frameworks leart it 
''' 22/12/2025 
@app.route('/hello')             #app.route is decorator
def hello_world():
    return 'Hello, World!' # functions which are mapped to api then urls called
                  
@app.route('/greet')        # another api endpoint
def greet():
    return 'Greetings from Flask'

@app.route('/index')   # another api endpoint
def portfolio():
    return render_template('index.html')  # render_template is used to render html files from templates folder

#app.run(use_reloader=True)  # run the app on local server
# use_reloader=True means auto restart the server on code changes'''