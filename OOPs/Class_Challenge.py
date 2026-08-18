
class question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        #return {f"{self.text}-->{self.answer}"}
    def display(self):
        print(f"{self.text}--> {self.answer}")

