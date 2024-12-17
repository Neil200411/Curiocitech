
import webbrowser
from Video import *
from About import *
from Article import *
from Quizzes import *
from Dictionary import *
from Loading_Screen import *
from Manager import screen_helper
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import Screen, SlideTransition, FallOutTransition, RiseInTransition
from kivy.core.window import Window
from Video import video_helper

Window.set_icon('Images/logo.jpg') #Logo of the app

#combinations of kv strings
full = screen_helper + loading_screen_helper + dictionary_helper + quiz_helper + helper_article + video_helper + about_helper

#main
class FinalApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style= "Light"
        self.screen_manager = Builder.load_string(full)
        self.load_tables()
        self.click_sound = SoundLoader.load('Sounds/mouse-click-153941.mp3')
        self.click_sound2 = SoundLoader.load('Sounds/click.mp3')
        Window.bind(on_keyboard=self.handle_back_button)  # bind the back button of cellphones
        self.screen_stack = []  # Stack to keep track of screen for back function
        self.main_screen = "main"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        self.exit_dialog = None

        return self.screen_manager

    # to switch screen , and to track its history
    def switch_to_screen(self, screen_name):
        # Add the current screen to the stack only if it's not already in the stack
        if self.root.current != screen_name:
            self.screen_stack.append(self.root.current)  # Add the current screen to the stack
        self.root.current = screen_name  # Navigate to the new screen

    def handle_back_button(self, window, key, *args):
        if key == 27:  # code for android Back button
            if self.screen_stack:  # If there are screens in the stack
                previous_screen = self.screen_stack.pop()  # Get the last screen
                self.root.current = previous_screen  # Navigate to the previous screen
                article_screen = self.screen_manager.get_screen('Article')
                article_screen.clear_tabs()
                return True  # Prevent default back button behavior
            elif self.root.current != self.main_screen:  # If not on the main screen
                self.root.current = self.main_screen  # Navigate to the main screen
                self.screen_stack.clear()
                return True
            elif self.root.current == self.main_screen:  # If on the main screen
                current_screen = self.root.get_screen('main')
                if current_screen.ids.nav_drawer.state == "open":
                    current_screen.ids.nav_drawer.set_state("stop")
                    return True
                else:  # If on the main screen, show exit confirmation
                    self.show_exit_confirmation()
                    return True
        return False  # Allow default behavior for other keys

    def show_exit_confirmation(self):
        # Create the exit confirmation
        if not self.exit_dialog:
            self.exit_dialog = MDDialog(
                text="Are you sure you want to exit the app?",
                buttons=[
                    MDRaisedButton(
                        text="CANCEL",
                        on_release=lambda _: self.exit_dialog.dismiss()  # Dismiss dialog
                    ),
                    MDRaisedButton(
                        text="EXIT",
                        on_release=lambda _: self.stop()  # Exit the app
                    ),
                ],
            )
        self.exit_dialog.open()  # Show the dialog


    def dl(self): # code and condition in switching dark and light mode
        current_screen = self.root.get_screen('main')
        if 'tap' in current_screen.ids:
            current_theme = current_screen.ids.tap.text
            if current_theme == "Dark Mode":
                self.theme_cls.theme_style = "Dark"
                self.clearcolor = (0, 0, 0, 1)
                current_screen.ids.tap.text = "Light Mode"
                current_screen.ids.icons.icon = "weather-sunny"
                self.screen_manager.get_screen('dictionary').ids.search_input.text_color_focus = "white"
                self.screen_manager.get_screen('about_us').ids.one.text = "[b][color=#FFFFFF]Larios, Djohn Jared[/color][/b] - Data Analyst, Project Manager, Programmer"
                self.screen_manager.get_screen('about_us').ids.two.text = "[b][color=#FFFFFF]Acar, Annessa[/color][/b] - Project Manager, Researcher, Programmer"
                self.screen_manager.get_screen('about_us').ids.three.text = "[b][color=#FFFFFF]Catilo, Neil[/color][/b] - Project Lead, UI/UX Developer, Programmer"
                self.screen_manager.get_screen('about_us').ids.four.text = "[b][color=#FFFFFF]Delen, John[/color][/b] - Data Analyst, Researcher, Programmer"
                self.screen_manager.get_screen('about_us').ids.five.text = "[b][color=#FFFFFF]Gonzalez, Kelly[/color][/b] - Researcher, Programmer, Documentation in charge"
                self.screen_manager.get_screen('about_us').ids.mission.text_color = (1, 1, 1, .8)


            else:
                self.theme_cls.theme_style = "Light"
                self.clearcolor = (1, 1, 1, 1)
                current_screen.ids.tap.text = "Dark Mode"
                current_screen.ids.icons.icon = "weather-night"
                self.screen_manager.get_screen('dictionary').ids.search_input.text_color_focus = "black"
                self.screen_manager.get_screen('about_us').ids.one.text = "[b][color=#000000]Larios, Djohn Jared[/color][/b] - Data Analyst, Project Manager, Programmer"
                self.screen_manager.get_screen('about_us').ids.two.text = "[b][color=#000000]Acar, Annessa[/color][/b] - Project Manager, Researcher, Programmer"
                self.screen_manager.get_screen('about_us').ids.three.text = "[b][color=#000000]Catilo, Neil[/color][/b] - Project Lead, UI/UX Developer, Programmer"
                self.screen_manager.get_screen('about_us').ids.four.text = "[b][color=#000000]Delen, John[/color][/b] - Data Analyst, Researcher, Programmer"
                self.screen_manager.get_screen('about_us').ids.five.text = "[b][color=#000000]Gonzalez, Kelly[/color][/b] - Researcher, Programmer, Documentation in charge"
                self.screen_manager.get_screen('about_us').ids.mission.text_color = (0,0,0,.8)

    def play_click_sound(self):

        if self.click_sound:
            self.click_sound.play()

    def play_click_sound2(self):

        if self.click_sound2:
            self.click_sound2.play()

    def play_click_sound3(self):
        current_screen = self.root.get_screen('main')
        self.play_click_sound2()  # Play the in touch sound
        current_screen.ids.nav_drawer.set_state("toggle")

    def show_dictionary(self): #switch in dictionary screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('dictionary')
        self.play_click_sound2()


    def show_article(self): #switch in article screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('Article')
        self.play_click_sound2()

    def go_back_to_main(self): #switch to main screen
        self.root.transition = SlideTransition(duration=0.5, direction='right')
        self.switch_to_screen('main')
        self.play_click_sound2()
        article_screen = self.screen_manager.get_screen('Article')
        article_screen.clear_tabs()

    def show_table_screen(self, table_screen_name): #to show table
        if self.theme_cls.theme_style == "Dark":
            clearcolor = (0, 0, 0, 1)
        else:
            clearcolor = (1, 1, 1, 1)

        if table_screen_name == 'table':
            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)
        elif table_screen_name == 'table1':
            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)
        elif table_screen_name == 'table2':

            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)

        self.switch_to_screen(table_screen_name)


    def open_link(self, url): #to open links
        webbrowser.open(url)

    def load_tables(self):
        if self.screen_manager:
            table = MDDataTable(
                column_data=[("Slang", dp(30)), ("Meanings", dp(60))],
                rows_num = 20,
                row_data=[("BRB","Be Right Back. Used to indicate a temporary absence."),
                          ("IDK", "I Don't Know"),
                          ("LOL", "Laugh Out Loud"),
                          ("DM", "Direct message. A private message sent between users"),
                          ("YOLO", "You Only Live Once; Used to express taking risks or living life to the fullest"),
                          ("SMH", "Shaking My Head; Used to express disbelief or disappointment"),
                          ("BAE", "Before Anyone Else; A term of affection for a romantic partner"),
                          ("YEET", "to throw something with force"),
                          ("SUS", "Suspicious or Suspect"),
                          ],
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(0.9, 0.8),
                height=200,
                padding = 1
            )
            table1 = MDDataTable(
                column_data=[("Terms", dp(20)), ("Meanings", dp(65)), ],
                rows_num=20,
                row_data=[("Python", "a high-level programming language"),
                ("Data", "facts and statistics collected together"),
                ("Yeet", "to throw something with force"),
                ("Sus", "suspicious or suspect"),
                ("Account", "a personal profile or login on a website or social media platform"),
                ("App", "a software application designed for mobile devices, tablets, or desktops that performs specific tasks\n"),
                ("Avatar", "a digital representation of a user, often in the form of a profile picture or a cartoonish character"),
                ("Cloud", "online storage that allows you to store files and access them from any device connected to the internet"),
                ("Follower", "a user who subscribes to see another user’s posts on social media platforms"),
                ("Fomo", "the anxiety or feeling of missing out on something exciting happening online or socially"),
                ("Influencer", "a person on social media who has a large following and can influence the opinions or behaviors of others"),
                          ],
                size_hint=(0.9, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                padding = 1,



            )

            self.screen_manager.get_screen('table').ids.table_container.add_widget(table)
            self.screen_manager.get_screen('table1').ids.table1_container.add_widget(table1)



    def show_video(self): #switch to video screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('video')

    def show_main_screen_quiz(self): #switch to main quiz screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('quiz')

    def show_quiz(self): #switch to quiz screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('start')

    def show_about(self): #switch to abot screen

        self.root.transition = SlideTransition(direction="left")
        self.switch_to_screen('about_us')




DictionaryScreen()
SplashScreen()
CircularProgressBar()
QuizScreen()
StartQuizScreen()
AboutUsScreen()
TableScreen()
Table1Screen()
VideoScreen()



class MainScreen(Screen):
    text1 = '[font=FONTS/Lexend-Black.ttf]Step 1:[/font]\n [size=25][i]Tap the menu button found in upper right corner[/i][/size]'
    text2 = '[font=FONTS/Lexend-Black.ttf]Step 2:[/font]\n [size=25] [i]Choose and click what you want to do or view. [/i][/size]'
    text3 = '[font=FONTS/Lexend-Black.ttf]Step 3:[/font]\n [size=25][i]Explore, learn, and enjoy![/i][/size]'
    pass



if __name__ == "__main__":
    FinalApp().run()