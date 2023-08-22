from flask import Flask

app = Flask(__name__)


@app.get('/helloworld')
def helloword():
    return {'message':'hello world'}


app.run()