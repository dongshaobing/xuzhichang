from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "这是首页"

@app.route("/aaa")
def aaa():
    return "这是ip:port/aaa的内容"

@app.route("/name")
def c():
    return "这是ip:port/name路由下的内容：我是森淼"

if __name__=="__main__":
    app.run(debug=True,host='192.168.0.100',port=9999)