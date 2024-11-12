class Text:
    def __init__(self, text: str):
        self.text = text
    def output_text(self):
        return self.text

class BoldText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    
    def output_text(self):
        return f"<b>{self.text_obj.output_text()}</b>"

class ItalicText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    # 
    def output_text(self):
        return f"<i>{self.text_obj.output_text()}</i>"

class UnderlineText:
    def __init__(self, text_obj: Text):
        self.text_obj = text_obj
    
    def output_text(self):
        return f"<u>{self.text_obj.output_text()}</u>"

t = Text("ala ma kota")
print( t.output_text() )
b = BoldText(t)
print( b.output_text() )
u = UnderlineText(t)
print( u.output_text() )
i = ItalicText(t)
print( i.output_text() )

