from flask import Flask,render_template,url_for,request 
from tweepy_run import tweepy_run

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')#, methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
         url=request.args.get('tweet_url')
         return tweepy_run(url)
    else:
        #return 'nothing'
        return render_template('dashboard.html')

if __name__=='__main__':
    app.run(debug=True)
