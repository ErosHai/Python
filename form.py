from flask import Flask, render_template, json, jsonify

app = Flask(__name__)

@app.route('/')

# json转换为字典
@app.route('/form')
def form_handler():
    with open('./static/form.json', 'r', encoding='utf-8') as f:
        load_result = json.load(f)
        print(type(f))

    # with open('./static/form.json', 'a', encoding='utf-8') as f:
    #     data = {
    #         'name':'zhang san',
    #         'age':32,
    #         'work':'Engineer'
    #     }
    #
    #     load_result.update(json.dumps(data))
    #     json.dump(load_result, f)
    # f.close()

    return render_template('form.html',load_result=load_result)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5001, debug=True)