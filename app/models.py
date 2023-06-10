import json
from datetime import datetime

from app import db

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text)
    answer_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    inserted_at = db.Column(db.DateTime)  # дата вставки в бд
    
    def __init__(self, id:int, question_text:str, answer_text:str, created_at:datetime):
        self.id = id
        self.question_text = question_text
        self.answer_text = answer_text
        self.created_at = created_at
        self.inserted_at = datetime.now()
        
    def to_dict(self):
        return {
            "id":self.id,
            "question_text":self.question_text,
            "answer_text": self.answer_text,
            "created_at": self.created_at.isoformat()
        }