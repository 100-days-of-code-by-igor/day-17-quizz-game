class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Checks if there are more questions to ask; returns a bool"""
        return self.question_number < len(self.question_list)

    def manage_score(self, is_correct, correct_answer):
        """Manages scoring and prints score information"""
        if is_correct:
            self.score += 1
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        """Checks user answer for correctness"""
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.manage_score(True, correct_answer)
        else:
            print("Wrong")
            self.manage_score(False, correct_answer)

    def next_question(self):
        """Retrieve current question and ask user for an answer."""
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} True or False? \n").lower()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)
