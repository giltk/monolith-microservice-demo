from flask import Flask, request, render_template
 
app = Flask(__name__)

@app.route('/')
@app.route('/users/', methods=['GET', 'POST'])
def users():
    method = request.method
    if method == 'POST':
      # get users list
      user_list = ['user1', 'user2', 'user3']
    else:
       user_list = None
    return render_template('users.html', method=method, user_list=user_list)

if __name__ == '__main__':
    app.run(port=8000)