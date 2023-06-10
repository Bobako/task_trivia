import datetime
from dateutil import parser

import requests

from app import db, config
from app.models import Question

def get_new_questions(questions_num: int) -> None:
    url = config["SITE"]["questions_url"]
    while questions_num:
        questions = requests.get(f"{url}?count={questions_num}").json()
        questions_num = 0
        for question in questions:
            if db.session.query(Question).filter(Question.id == question["id"]).first():
                questions_num += 1  # уже есть в бд
            else:
                db.session.add(Question(question["id"],
                                        question["question"],
                                        question["answer"],
                                        parser.parse(question["created_at"])))
        
        
    db.session.commit()
    
