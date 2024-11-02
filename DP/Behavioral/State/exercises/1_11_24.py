# Exercise #1)
# Implement a simple media player that can play different types of media files,
# including music and video.

# The player should have a Player class that maintains the current state of the media player. The player should be able to transition between the following states:

# 1. StoppedState: The player is currently stopped.
# 2. PlayingState: The player is currently playing a media file.
# 3. PausedState: The player is currently paused.

# 4. Your task is to implement the Player class and the three state classes (StoppedState, PlayingState, and PausedState) using the State Design Pattern.
# 5. The Player class should have methods for playing, stopping, nad pausing the media, and it should delegate these operations to the appropriate
# state object based on the current state of the player.

# We have provided you with some starting code for this task.
# class Player:
#     def __init__(self):
#         pass

#     def play(self):
#         pass

#     def stop(self):
#         pass

#     def pause(self):
#         pass

# class StoppedState:
#     def __init__(self):
#         pass

# class PlayingState:
#     def __init__(self):
#         pass

# class PausedState:
#     def __init__(self):
#         pass
from abc import ABC, abstractmethod
class Player:
    def __init__(self):
        self.state = StoppedState(self)

    def play(self):
        self.state.play()

    def stop(self):
        self.state.stop()

    def pause(self):
        self.state.pause()

class PlayerState(ABC):
    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def pause(self):
        pass

class StoppedState(PlayerState):
    def play(self):
        print("Playing media from the beginning! trutututu...")
        self.player.state = PlayingState(self.player)

    def stop(self):
        print("You push the button but you don't hear any difference")
        self.player.state = self

    def pause(self):
        print("You push the button but you don't hear any difference")
        self.player.state = PausedState(self.player)

class PlayingState(PlayerState):
    def play(self):
        print("You push the button but you don't hear any difference")
        self.player.state = self

    def stop(self):
        print("You push the button and music stops!")
        self.player.state = StoppedState(self.player)

    def pause(self):
        print("You push the button and music paused!")
        self.player.state = PausedState(self.player)

class PausedState(PlayerState):
    def play(self):
        print("Resuming media! trutututu...")
        self.player.state = PlayingState(self.player)

    def stop(self):
        print("You push the button and music stops!")
        self.player.state = StoppedState(self.player)

    def pause(self):
        print("You push the button but you don't hear any difference")
        self.player.state = self


p = Player()
p.play()
p.stop()
p.play()
p.pause()
p.play()

print("\n\n\n\n\n\n\n\n")
# Exercise #2)
# Implement a text editor that can edit and format text using different styles, including bold, italic, and underline. The editor should have a TextEditor class
# that maintains the current state of the text editor. The editor should be able to transition between the following states:
# 1. DefaultState: The editor is currently in the default state, no special formatting is applied to the text.
# 2. BoldState: The editor is currently in the bold state, any new text entered will be bolded.
# 3. ItalicState: The editor is currently in the italic state, any new text entered will be italicized.
# 4. UnderlineState: The editor is currently in the underline state, any new text entered will be underlined.

# 5. Your task is to implement the TextEditor class and the four state classes(DefaultState, BoldState, ItalicState, and UnderlineState) using the State Design Pattern.
# 6. The TextEditor class should have methods for entering text, applying bold, italic, and underline formatting to the text, and
# undoing any formatting changes.
# 7. The editor should be able to maintain a history of formatting changes so that it can undo and redo changes.

# class TextEditor:
#     def __init__(self):
#         pass

#     def enter_text(self, text):
#         pass

#     def apply_bold(self):
#         pass

#     def apply_italic(self):
#         pass

#     def apply_underline(self):
#         pass

#     def undo(self):
#         pass

#     def redo(self):
#         pass

# class DefaultState:
#     def __init__(self):
#         pass

# class BoldState:
#     def __init__(self):
#         pass

# class ItalicState:
#     def __init__(self):
#         pass

# class UnderlineState:
#     def __init__(self):
#         pass

class TextEditor:
    def __init__(self):
        self.state = DefaultState(self)
        self.text = ""
        self.history = []
        self.redo_history = []

    def enter_text(self, text):
        # Clear redo, the timeline has changed
        self.redo_history.clear()

        # Get formating
        formated_text = self.state.decorate_text(text)

        # Add to history
        self.history.append(formated_text)

        # Add text
        self.text += formated_text

    def apply_bold(self):
        self.state.apply_bold()

    def apply_italic(self):
        self.state.apply_italic()

    def apply_underline(self):
        self.state.apply_underline()

    def apply_default(self):
        self.state.apply_default()

    def undo(self):
        # Check if possible
        if not self.history:
            print("nothing to undo.")
            return

        # Get last change
        text_to_undo = self.history.pop()
        
        # Append it to redo history
        self.redo_history.append(text_to_undo)

        # Cut off last change from the text
        self.text = self.text[:-len(text_to_undo)]

    def redo(self):
        # Check if possible
        if not self.redo_history:
            print("nothing to undo.")
            return

        # Get last change
        text_to_redo = self.redo_history.pop()

        # Append it to history
        self.history.append(text_to_redo)

        # Append last change to the text
        self.text += text_to_redo
    def __str__(self):
        return (
            f"Text Editor - Current State: {self.state.__class__.__name__}\n"
            f"Text Length: {len(self.text)} characters\n"
            f"Text Content:\n{self.text}"
        )
class BaseState(ABC):
    def __init__(self, text_editor: TextEditor):
        self._text_editor = text_editor
    @abstractmethod
    def apply_bold(self) -> None:
        pass
    @abstractmethod
    def apply_italic(self) -> None:
        pass
    @abstractmethod
    def apply_underline(self) -> None:
        pass
    @abstractmethod
    def apply_default(self) -> None:
        pass
    @abstractmethod
    def decorate_text(self, text: str) -> str:
        pass

class DefaultState(BaseState):
    def apply_bold(self) -> None:
        self._text_editor.state = BoldState(self._text_editor)
    def apply_italic(self) -> None:
        self._text_editor.state = ItalicState(self._text_editor)
    def apply_underline(self) -> None:
        self._text_editor.state = UnderlineState(self._text_editor)
    def apply_default(self) -> None:
        self._text_editor.state = self
    def decorate_text(self, text: str) -> str:
        return text

class BoldState(BaseState):
    def apply_bold(self) -> None:
        self._text_editor.state = self
    def apply_italic(self) -> None:
        self._text_editor.state = ItalicState(self._text_editor)
    def apply_underline(self) -> None:
        self._text_editor.state = UnderlineState(self._text_editor)
    def apply_default(self) -> None:
        self._text_editor.state = DefaultState(self._text_editor)
    def decorate_text(self, text: str) -> str:
        return f"<b>{text}</b>"

class ItalicState(BaseState):
    def apply_bold(self) -> None:
        self._text_editor.state = BoldState(self._text_editor)
    def apply_italic(self) -> None:
        self._text_editor.state = self
    def apply_underline(self) -> None:
        self._text_editor.state = UnderlineState(self._text_editor)
    def apply_default(self) -> None:
        self._text_editor.state = DefaultState(self._text_editor)
    def decorate_text(self, text: str) -> str:
        return f"<i>{text}</i>"

class UnderlineState(BaseState):
    def apply_bold(self) -> None:
        self._text_editor.state = BoldState(self._text_editor)
    def apply_italic(self) -> None:
        self._text_editor.state = ItalicState(self._text_editor)
    def apply_underline(self) -> None:
        self._text_editor.state = self
    def apply_default(self) -> None:
        self._text_editor.state = DefaultState(self._text_editor)
    def decorate_text(self, text: str) -> str:
        return f"<u>{text}</u>"


te = TextEditor()
te.enter_text("Ala ma")
te.apply_bold()
te.enter_text("kota")
te.apply_underline()
te.enter_text("a kot ma ale")
te.apply_default()
te.enter_text("\nTaka to krotka i glupia historia")
print("############")
print(te)
print("############")
te.undo()
print(te)
print("############")
te.undo()
print(te)
print("############")
te.redo()
print(te)
print("############")
te.redo()
print(te)
print("############")
te.redo()
print(te)
print("############")