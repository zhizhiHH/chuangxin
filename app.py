
from flask import Flask, render_template, request

app = Flask(__name__)

# 存储留言
messages = []

# 主页路由，包括展示所有留言和留言表单
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 获取留言内容，并且追加到留言列表中
        message = request.form["message"]
        messages.append(message)

    # 渲染主页模板，传入留言列表 messages
    return render_template("index.html.jinja2", messages=messages)

# 程序入口
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
