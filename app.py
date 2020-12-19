from flask import Flask,render_template,url_for,request 
from tweepy_run import tweepy_run
from model import model_run
from pred_plot import mk_piechart



app= Flask(__name__)

tweet_data={}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')#, methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        url=request.args.get('tweet_url')
        
        tweet_data= tweepy_run(url)
        if tweet_data=='There is an error in url':
            return render_template('load.html')
        #print(tweet_data)
        reply_pred = model_run(tweet_data) 
        tweet_data = mk_piechart(reply_pred,tweet_data)

        return render_template('dashboard.html',tweet_data=tweet_data)

    else:
        #return 'nothing'
        return render_template('dashboard.html')

if __name__=='__main__':
    app.run(debug=True)
