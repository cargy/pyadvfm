"""
AdvFM statements editor
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, BOLD, JUSTIFY
from .core import Game
from .statements import generator


class AdvFMEditor(toga.App):
    def startup(self):
        self.game = Game(10, 10, 10, 10)
        self.statement_generator = generator('statements_001.json')
        self.current_statement = next(self.statement_generator)
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        # Top Box
        top_box = toga.Box()

        self.players_level = toga.NumberInput(value=self.game.factors.players, step=1)
        players_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        players_box.add(toga.Label("Players"))
        players_box.add(self.players_level)

        self.fans_level = toga.NumberInput(value=self.game.factors.fans, step=1)
        fans_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        fans_box.add(toga.Label("Fans"))
        fans_box.add(self.fans_level)

        self.management_level = toga.NumberInput(value=self.game.factors.management, step=1)
        management_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        management_box.add(toga.Label("Management"))
        management_box.add(self.management_level)

        self.finances_level = toga.NumberInput(value=self.game.factors.finances, step=1)
        finances_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        finances_box.add(toga.Label("Finances"))
        finances_box.add(self.finances_level)

        top_box.add(players_box)
        top_box.add(fans_box)
        top_box.add(management_box)
        top_box.add(finances_box)

        # Middle Box (for long label)
        middle_box = toga.Box(style=Pack(direction=ROW))
        self.statement_label = toga.MultilineTextInput(
            style = Pack(alignment=CENTER, font_weight=BOLD, flex=0.8, padding=20),
            readonly=True
        )
        self.update_statement()
        middle_box.add(self.statement_label)

        # Bottom Box
        bottom_box = toga.Box()
        agree_button = toga.Button('Agree', style=Pack(flex=1, height=100, padding_left=50), on_press=self.agree)
        disagree_button = toga.Button('Disagree', style=Pack(flex=1, height=100, padding_right=50), on_press=self.disagree)
        bottom_box.add(agree_button)
        bottom_box.add(disagree_button)

        # Main Box to hold all three areas
        main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
        main_box.add(top_box)
        main_box.add(middle_box)
        main_box.add(bottom_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # Function to handle agreement
    def agree(self, widget):
        # Update factors based on agreement
        self.game.apply(self.current_statement.agree)
        self.current_statement = next(self.statement_generator)
        self.update_numbers()
        self.update_statement()

    # Function to handle disagreement
    def disagree(self, widget):
        # Update factors based on disagreement
        self.game.apply(self.current_statement.disagree)
        self.current_statement = next(self.statement_generator)
        self.update_numbers()
        self.update_statement()

    # Update the numbers on the screen
    def update_numbers(self):
        self.players_level.value = self.game.factors.players
        self.fans_level.value = self.game.factors.fans
        self.management_level.value = self.game.factors.management
        self.finances_level.value = self.game.factors.finances

    def update_statement(self):
        self.statement_label.value = self.current_statement.statement#.replace('. ', '.\n')


def main():
    return AdvFMEditor()
