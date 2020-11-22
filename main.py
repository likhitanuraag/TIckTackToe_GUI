from kivy.config import Config
Config.set('graphics','resizable', False)
import kivy
import sys
import subprocess
import json
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from subprocess import call
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.core.audio import SoundLoader


class TTTGrid(Widget):
    #name = ObjectProperty(None)
    #email = ObjectProperty(None)
    sound = SoundLoader.load("Assets\\sounds\\menu_1.mp3")
    sound.play()


    def on_spinner_select_playType(self, playtype = "Local-player"):
        '''
        ptype = {}
        if playtype == "Local-player":
            ptype = {"DIM": 3,"playType": 'Local-player'}
        if playtype == "Single-player":
            ptype = {"DIM": 3,"playType": 'Single-player'}
        if playtype == "Multi-player":
            ptype = {"DIM": 3,"playType": 'Multi-player'}
        if playtype == "LAN":
            ptype = {"DIM": 3,"playType": 'LAN'}

        with open('config.json', 'w') as f:  # writing JSON object
            json.dump(ptype, f) '''
        pass
    
    def on_spinner_select_DIM(self, dimension = "3X3"):
        dim = {}
        if dimension == "3X3":
            dim = {"DIM": 3}
        if dimension == "6X6":
            dim = {"DIM": 6}
        if dimension == "9X9":
            dim = {"DIM": 9}

        with open('dim-config.json', 'w') as f:  # writing JSON object
            json.dump(dim, f)

    def btn(self):
        spawn_program_and_die(["python", "game.py"])
        print("Game Started")

class TTTApp(App):
    def build(self):
        return TTTGrid()

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

if __name__ == "__main__":
    dim = {"DIM": 3} #default setting
    with open('dim-config.json', 'w') as f:  # writing JSON object
        json.dump(dim, f)
    TTTApp().run()