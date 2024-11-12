from abc import ABC, abstractmethod

class Text:
    def __init__(self, text: str):
        self.text = text
    
    def present_text(self):
        return self.text

class BoldText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    
    def present_text(self):
        return f'<b>{self.text_obj.present_text()}</b>'

class ItalicText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    
    def present_text(self):
        return f'<i>{self.text_obj.present_text()}</i>'

class UnderlineText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    
    def present_text(self):
        return f'<u>{self.text_obj.present_text()}</u>'

t = Text("Ala ma kota")
t.present_text()
b = BoldText(t)
i = ItalicText(t)
u = UnderlineText(t)

print(
    b.present_text(),
    i.present_text(),
    u.present_text()
)