from transformers import pipeline
model_checkpoint = "nguyenvulebinh/vi-mrc-large"

def predict(question, context):
    nlp = pipeline('question-answering', model=model_checkpoint,
                    tokenizer=model_checkpoint)
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    start = res['start']
    end = res['end']
    start_idx = len(context[:start-1].split(" "))
    end_idx = len(context[:end].split(" "))
    ctx = context.split(" ")
    answer = " ".join(ctx[start_idx:end_idx])
    return answer

