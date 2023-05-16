from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def health_check():
   return 'ok'
@app.route('/api/users')
def users():
    response = Flask.make_response(self=app, rv={'users': ['user1', 'user2', 'user3', 'user4']})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)