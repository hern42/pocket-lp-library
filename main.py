# Appli pocket-lp-library

# import the kivy stuff
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# import other stuff which is needed: sqlite3
import sqlite3

# the app has 4 screens

class MenuScreen(Screen):
    """ Menu has 4 items: print/sort info, search, add new, exit
        On top Menu shows the total amount of LPs in the db """
    pass


class DisplayScreen(Screen):
    """ Display allows to display all or sorted part of the db """
    pass


class SearchScreen(Screen):
    """ Search allows to search the db according to criteria """
    pass


class AddNewScreen(Screen):
    """ AddNew allows to add a new LP (or maybe to correct an entry) """
    pass


class ScreenManagement(ScreenManager):
    pass

kv = Builder.load_file('vinylpocket.kv')

class VinylPocketApp(App):
    def build(self):
        return kv

# main app
if __name__ == '__main__':
    VinylPocketApp().run()
