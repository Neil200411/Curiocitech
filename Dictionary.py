
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog


# help manage the design, texts, placements of elements, setting screen setup, and binding actions
dictionary_helper = """
<DictionaryScreen>:
    name: 'dictionary'
    FloatLayout:
        MDTextField:
            id: search_input
            mode: "line"
            hint_text: "Enter abbreviation to search"
            helper_text: "Type What You Want to Search"
            helper_text_mode: "on_focus"
            size_hint: 0.6, None
            height: dp(40)
            pos_hint: {'center_x': 0.5, 'top': 0.88}
            on_text_validate: root.search_term(search_input)
            text_color_focus: "black"


        MagicButton:
            text: "Search"
            size_hint: None, None
            size: dp(150), dp(40)
            pos_hint: {'center_x': 0.77, 'top': 0.87}
            md_bg_color: [199 / 255, 143 / 255, 87 / 255, 1]
            on_release: 
                self.wobble()
                Clock.schedule_once(lambda dt: root.search_term(search_input), 0.1)
                app.play_click_sound()

    RelativeLayout:
    
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size   
        MDTopAppBar:
            title: 'Dictionaries'
            left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
            md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
            pos_hint: {'top': 1}
            
        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            padding: 20
    
            pos_hint: {'center_x': 0.5, 'center_y': .8}       
    
            MagicButton:
                text: "View Abbreviation Table"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: [199 / 255, 143 / 255, 87 / 255, 1]
                on_release:
                    self.wobble()
                    Clock.schedule_once(lambda dt: app.show_table_screen('table'), 0.5)
                    app.play_click_sound()
    
            MagicButton:
                text: "View Terms Table"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}       
                md_bg_color: [199 / 255, 143 / 255, 87 / 255, 1]     
                on_release:
                    self.wobble()
                    Clock.schedule_once(lambda dt: app.show_table_screen('table1'), 0.5)
                    app.play_click_sound()

<TableScreen>:
    name: 'table'
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: .2
            pos: self.pos
            size: self.size
        BoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: 'Abbreviation Table'
                left_action_items: [["arrow-left", lambda x: app.show_dictionary()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
            
            MDBoxLayout:
                id: table_container
                padding: 1

<Table1Screen>:
    name: 'table1'
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: .2
            pos: self.pos
            size: self.size
        BoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: 'Terms Table'
                left_action_items: [["arrow-left", lambda x: app.show_dictionary()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
            MDBoxLayout:
                id: table1_container
                padding: 5

"""

class DictionaryScreen(Screen):
    def __init__(self, **kwargs):
        super(DictionaryScreen, self).__init__(**kwargs)
        self.original_data = dictionary = [
    ("BRB","Be Right Back. Used to indicate a temporary absence."),
    ("Idk", "I don't know"),
    ("Lol", "laugh out loud"),
    ("Python", "a high-level programming language"),
    ("Data", "facts and statistics collected together"),
    ("Data", "facts and statistics collected together"),
    ("Yeet", "to throw something with force"),
    ("Sus", "suspicious or suspect"),
    ("Account", "a personal profile or login on a website or social media platform"),
    ("App",
     "a software application designed for mobile devices, tablets, or desktops that performs specific tasks"),
    ("Avatar",
     "a digital representation of a user, often in the form of a profile picture or a cartoonish character"),
    ("Cloud",
     "online storage that allows you to store files and access them from any device connected to the internet"),
    ("Follower", "a user who subscribes to see another user’s posts on social media platforms"),
    ("Fomo", "the anxiety or feeling of missing out on something exciting happening online or socially"),
    ("Influencer",
     "a person on social media who has a large following and can influence the opinions or behaviors of others"),
    ("DM", "Direct message. A private message sent between users"),
    ("YOLO", "You Only Live Once; Used to express taking risks or living life to the fullest"),
    ("SMH", "Shaking My Head; Used to express disbelief or disappointment"),
    ("BAE", "Before Anyone Else; A term of affection for a romantic partner"),
    ("YEET", "to throw something with force"),
    ("SUS", "Suspicious or Suspect"),
    ]


    def on_enter(self):
        pass

    def search_term(self, search_input):
        """Search for the abbreviation and show a dialog with the meaning."""
        search_value = search_input.text.lower().strip()

        # Search for the term in the dictionary
        for abbr, meaning in self.original_data:
            if search_value == abbr.lower():
                # Show a dialog with the meaning of the term
                self.show_dialog(abbr, meaning)
                search_input.text = ""  # Clear search field after search
                return

        # If no match found, show a not found dialog
        self.show_dialog("Not Found", f"No meaning found for '{search_value}'. Please try again.")
        search_input.text = ""  # Clear search field after showing dialog

    def show_dialog(self, title, text):
        """Show a dialog with the result."""
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, None),
            height=dp(200)
        )
        dialog.open()

class TableScreen(Screen):
    pass
class Table1Screen(Screen):
    pass
