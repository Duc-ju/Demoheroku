from flask import Flask
from transformers import pipeline

app = Flask(__name__)

@app.route("/")
def home():
    model_checkpoint = "nguyenvulebinh/vi-mrc-large"
    # model_checkpoint = "nguyenvulebinh/vi-mrc-base"
    nlp = pipeline('question-answering', model=model_checkpoint,
                      tokenizer=model_checkpoint)
    QA_input = {
      'question': "Bình là chuyên gia về gì ?",
      'context': "Bình Nguyễn là một người đam mê với lĩnh vực xử lý ngôn ngữ tự nhiên . Anh nhận chứng chỉ Google Developer Expert năm 2020"
    }
    res = nlp(QA_input)
    print('pipeline: {}'.format(res))

    return "Huyen"


if __name__ == '__main__':
    app.run()


