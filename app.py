from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
      return render_template("home.html")
    else:
      context =  request.form['context']
      question =  request.form['question']

      answer = "Hệ thống đang chờ cập nhật"
      return render_template("home.html", context=context, question=question, answer=answer)


if __name__ == '__main__':
    app.run()



