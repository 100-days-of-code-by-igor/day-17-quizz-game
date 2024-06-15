from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import json
import requests
import html

def decode_html_entities_in_json(json_data):
    """
    Recursively decode HTML entities in JSON data.
    """
    if isinstance(json_data, dict):
        return {k: decode_html_entities_in_json(v) for k, v in json_data.items()}
    elif isinstance(json_data, list):
        return [decode_html_entities_in_json(item) for item in json_data]
    elif isinstance(json_data, str):
        return html.unescape(json_data)
    else:
        return json_data

number_of_questions = 10
api_url = f"https://opentdb.com/api.php?amount={number_of_questions}&difficulty=easy&type=boolean"
response = requests.get(api_url)
data = json.loads(response.text)
data_decoded = decode_html_entities_in_json(data)
questions = data_decoded['results']

question_bank = [Question(q['question'], q['correct_answer']) for q in questions]
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quizz")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
