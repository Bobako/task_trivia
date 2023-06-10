from flask import request, g
from flask_expects_json import expects_json

from app import app, db
from app.models import Question
from app import schemas
from app.logic import get_new_questions


@app.route("/", methods=["post"])
@expects_json(schemas.trivia_question_request)
def trivia_question():
    questions_num = g.data.get("questions_num")
    question_to_return = db.session.query(Question).order_by(Question.inserted_at.desc()).first()  # предыдущей сохранённый вопрос для викторины
    get_new_questions(questions_num)
    if question_to_return:
        return question_to_return.to_dict()
    else:
        return {}
    