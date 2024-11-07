class Text:
    def __init__(self, content: str):
        self.content = content
    
    def render(self):
        return self.content


class BoldDecorator:
    def __init__(self, text: Text):
        self.text = text
    
    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicDecorator:
    def __init__(self, text: Text):
        self.text = text
    
    def render(self):
        return f"<i>{self.text.render()}</i>"

text = Text("testowy text")
print(
    text.render()
)

btext = BoldDecorator(text)
itext = ItalicDecorator(text)
print(
    btext.render()
)
print(
    itext.render()
)