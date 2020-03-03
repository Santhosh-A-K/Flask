from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

@app.route('/')
def hello1():
    return 'Hi'

@app.route('/<name>/')
def hello_world(name):
    dict1 = {'phy':50,'che':60,'maths':70}
    return render_template('page1.html', user = name,result=dict1)
    """if name=='santhosh':
        return '<h1>hello %s </h1>' % name
    else:
        return '<h1>hello guest %s </h1>' % name"""

@app.route('/san/<user>',methods=['POST','GET'])
def san(user):
    if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('hello_world',name = user))
    else:
      user = request.args.get('nm')
      return redirect(url_for('hello_world',name = user))
    #return redirect(url_for('hello_world',name=user))
      #render_template(‘hello.html’)




if __name__=='__main__':
    app.run(port=5000,debug=True,use_reloader=False)