from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello Flask!'

# 渲染html文件
@app.route('/home',methods=['GET'])
def home_page():
    return render_template('home.html',text='MY NAME IS SEAN')

# 获取路径的动态参数
@app.route('/data/appInfo/<name>',methods=['GET'])
def query_data_by_name(name):
    print(type(name))
    return 'string: => {}'.format(name)

@app.route('/data/appInfo/<int:uid>',methods=['GET'])
def query_data_by_id(uid):
    print(type(uid))
    return 'int: => {}'.format(uid)

if __name__ == '__main__':
    app.run()