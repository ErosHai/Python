from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello Flask!'

# 渲染html文件并传参数
@app.route('/home',methods=['GET'])
def home_page():
    return render_template('home.html',text='MY NAME IS SEAN ZHANG123')


# 传给页面字典 后端给前端渲染时传递内容
@app.route('/data/app')
def data_page():

    data={
        '01':'aaa',
        '02':'bbb',
        '03':'ccc'
    }

    return render_template('data.html', data=data)

# 获取路径的动态参数  前端通过路径给后端传内容
@app.route('/data/appInfo/<name>',methods=['GET'])
def query_data_by_name(name):
    print(type(name))
    return 'string: => {}'.format(name)

@app.route('/data/appInfo/<int:uid>',methods=['GET'])
def query_data_by_id(uid):
    print(type(uid))
    return 'int: => {}'.format(uid)

# 运行js文件
@app.route('/data/static')
def static_page():
    return render_template('static.html')

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)