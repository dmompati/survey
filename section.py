from question import question

class section(question):

    def __init__(self, question_text, answers,title,description,questions):
        super().__init__(question_text, answers):
        self.title = title
        self.description = description
        self.questions = questions

section1 = section('Learning','This section is about how you are going with the learning in shecodes', )
# section1 = section('Social','This section is about how you are going with the Socially in shecodes')
# section1 = section('Learning','This section is about how you are going with the Location and time in shecodes')

