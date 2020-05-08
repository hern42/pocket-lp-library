# Appli pocket-lp-library


# import the kivy stuff
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

# import other stuff which is needed: sqlite3
# the database contains one table 'vinyl'
# with fields: id, artist, title, year, format, diverse, purchase_date
# id is INTEGER PRIMARY and needs to be AUTOINCREMENT
import sqlite3
import datetime

dbname = 'hern42_vinyls.db'


# class LpLibrary managing the db // does nothing at the moment!
class LpLibrary():
    """ This class takes care of giving the good info to the app """
    global dbname

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

    introtext = 'Appli Vinyl\nin your pocket'

    def print_nbr_lp(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        for info in connection.execute('SELECT COUNT(*) FROM vinyl'):
            nbr_vinyls = info[0]
        connection.close()
        return nbr_vinyls


class DisplayScreen(Screen):
    """ Display allows to display all or sorted part of the db """
    sort_str = ObjectProperty('')
    list_lp = ObjectProperty('')

    def print_list_sorted(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        if self.sort_str == '':
            query = 'SELECT * FROM vinyl ORDER BY id ASC'
        else:
            query = 'SELECT * FROM vinyl ORDER BY ' + self.sort_str + ' ASC'

        if self.howmany_input.text.isdigit():
            query += ' LIMIT ' + self.howmany_input.text
        else:
            pass

        string = ''
        for row in connection.execute(query):
            artist = row[1]
            album = row[2]
            year = row[3]
            formatlp = row[4]
            # comment = row[5]
            string += '[b]' + artist + '[/b] - ' + album + ' (' + year + ', ' + \
                      formatlp + ')\n'

        connection.close()
        self.list_lp = string.strip()


class SearchScreen(Screen):
    """ Search allows to search the db according to criteria """
    search_str = ObjectProperty('')
    search_result = ObjectProperty('')

    def print_list_search(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        if self.search_str == '':
            query = 'SELECT * FROM vinyl ORDER BY id ASC'
        else:
            query = 'SELECT * FROM vinyl WHERE ' + self.search_str + \
                    ' LIKE \"%' + self.search_input.text + '%\" ORDER BY id ASC'

        string = ''
        for row in connection.execute(query):
            artist = row[1]
            album = row[2]
            year = row[3]
            formatlp = row[4]
            # comment = row[5]
            string += '[b]' + artist + '[/b] - ' + album + ' (' + year + ', ' + \
                      formatlp + ')\n'

        connection.close()
        self.search_result = string.strip()


class AddNewScreen(Screen):
    """ AddNew allows to add a new LP (or maybe to correct an entry) """

    def add_new_lp(self):
        connection = sqlite3.connect('hern42_vinyls.db')
        fields = []
        fields.append(self.newartist_input.text)
        fields.append(self.newalbum_input.text)
        fields.append(self.newyear_input.text)
        fields.append(self.newformat_input.text)
        fields.append(self.newcomment_input.text)
        fields.append(str(datetime.date.today()))
        print(fields)
        query = 'INSERT INTO vinyl (artist, title, year, format, diverse, purchase_date) VALUES (?,?,?,?,?,?)'
        connection.execute(query, fields)
        connection.commit()
        connection.close()


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
