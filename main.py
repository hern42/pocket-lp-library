# Appli pocket-lp-library


# import the kivy stuff
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# import other stuff which is needed: sqlite3
import sqlite3


# class LpLibrary managing the db // does nothing at the moment!
class LpLibrary():
    """ This class takes care of giving the good info to the app """

    def __init__(self, dbname):
        self.connection = sqlite3.connect('dbname')
        print('db opened...')
        for info in self.connection.execute('SELECT COUNT(*) FROM vinyl'):
            self.nbr_vinyls = info[0]

    def __del__(self):
        self.connection.close()
        print('db closed.')


# the app has 4 screens
class MenuScreen(Screen):
    """ Menu has 4 items: print/sort info, search, add new, exit
        On top Menu shows the total amount of LPs in the db """
    def affiche_nbr_lp(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        for info in connection.execute('SELECT COUNT(*) FROM vinyl'):
            nbr_vinyls = info[0]
        return nbr_vinyls


class DisplayScreen(Screen):
    """ Display allows to display all or sorted part of the db """

    def affiche_liste_lp(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        query = 'SELECT * FROM vinyl ORDER BY artist ASC'
        string = ''
        for row in connection.execute(query):
            artist = row[1]
            album = row[2]
            year = row[3]
            formatlp = row[4]
            comment = row[5]
            string += artist + ' - ' + album + ' (' + year + ')\n'
        return string


class SearchScreen(Screen):
    """ Search allows to search the db according to criteria """
    pass


class AddNewScreen(Screen):
    """ AddNew allows to add a new LP (or maybe to correct an entry) """
    pass


# we use a screenmanager
class ScreenManagement(ScreenManager):
    pass


# we build the app using the builder to load the .kv file (name not important)
kv = Builder.load_file('vinylpocket.kv')


# the app proper
class VinylPocketApp(App):
    def build(self):
        return kv


# main app
if __name__ == '__main__':
    VinylPocketApp().run()
    print('bye')
