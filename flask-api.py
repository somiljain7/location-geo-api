from flask import Flask
from api_bp import api_bp

app=Flask(__name__)
app.register_blueprint(api_bp,url_prefix='/api/v1')

@app.route('/')
def hello_world():
	return 'hello world'

if __name__=='__main__':
	app.run(debug=True)