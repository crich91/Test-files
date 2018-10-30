import win32
import win32file
import win32con
import pywintypes
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):

    Test = "This is only a Test"
    
    effects = [
        Cycle(
            screen,
            FigletText(Test, font='big'), int(screen.height / 2 - 8 )),
        Cycle(
            screen,
            FigletText("Julie!", font='big'), int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])




Screen.wrapper(demo)
