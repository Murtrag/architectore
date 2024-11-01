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
