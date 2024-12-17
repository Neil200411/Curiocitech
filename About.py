
# help manage the design, texts, placements of elements, setting screen setup, and binding actions
about_helper = """
<AboutUsScreen>:
    name: "about_us"
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
                title: 'About Us'
                left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
    
            MDScrollView:
                id: scroll
                bar_width: 5
                fast_scroll: True
                bar_color: [0, 0.5, 0.7, 1]
                radius: [30, 30, 30, 30]
                smooth_scroll_end: 10


                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: 60
                    padding: 60
                    
                    MDLabel:
                        text: "Thank you for using [size=25]CURIOCITECH![/size]"
                        font_name: 'FONTS/LufgaBold.ttf'
                        halign: "center"
                   
                        font_size: '20sp'
                        bold: True
                        markup: True
                    Widget:
                    
                    MDLabel:
                        text: "CURIOCITECH is a digital literacy improvement platform designed to help the older generations adapt with today’s technology, allowing them to be digitally literate, understand modern slangs, and be technologically aware."
                        font_name: 'FONTS/Lexend-Regular.ttf'
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Body1"
                    Widget:
    
                    MDLabel:
                        text: "Mission"
                        halign: "center"
                        font_name: 'FONTS/LufgaBold.ttf'
                        font_size: '20sp'
                      
                        
                    MDLabel:
                        id: mission
                        text: "CURIOCITECH connecting generations with a simple touch."
                        font_name: 'FONTS/Lexend-Regular.ttf'
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: (0,0,0,.8)
                        markup: True
                        
    
                    MDLabel:
                        text: "Team Overview"
                        halign: "center"
                        font_name: 'FONTS/LufgaBold.ttf'
                        font_size: '20sp'
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 350  # Adjust to fit both the image and the label
    
                        Image:
                            source: "Images/ACAR.jpg"
                            size_hint: None, None
                            size: 300, 300
                            pos_hint: {'center_x': 0.5}
    
                        MDLabel:
                            id: two
                            text: "[b][color=#000000]Acar, Annessa[/color][/b] - Project Manager, Researcher, Programmer"
                            halign: "center"
                            theme_text_color: "Secondary"
                            font_name: "FONTS/Lexend-Regular.ttf"
                            
                            markup: True
                  
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 300  # Adjust to fit both the image and the label
    
                        Image:
                            source: "Images/Neil.jpg"
                            size_hint: None, None
                            size: 250, 300
                            pos_hint: {'center_x': 0.5}
    
                        MDLabel:
                            
                            id: three
                            text: "[b][color=#000000]Catilo, Neil[/color][/b] - Project Lead, UI/UX Developer, Programmer"
                            font_name: "FONTS/Lexend-Regular.ttf"
                            halign: "center"
                            theme_text_color: "Secondary"
                            markup: True
                        
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 350  # Adjust to fit both the image and the label
    
                        Image:
                            source: "Images/Delen.jpg"
                            size_hint: None, None
                            size: 300, 300
                            pos_hint: {'center_x': 0.5}
    
                        MDLabel:
                            
                            id: four
                            text: "[b][color=#000000]Delen, John[/color][/b] - Data Analyst, Researcher, Programmer"
                            font_name: "FONTS/Lexend-Regular.ttf"
                            halign: "center"
                            theme_text_color: "Secondary"
                            markup: True
                            
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 300  # Adjust to fit both the image and the label
    
                        Image:
                            source: "Images/Gonzalez.jpg"
                            size_hint: None, None
                            size: 250, 300
                            pos_hint: {'center_x': 0.5}
    
                        MDLabel:
                            
                            id: five
                            text: "[b][color=#000000]Gonzales, Kelly[/color][/b] - Researcher, Programmer, Documentation in charge"
                            font_name: "FONTS/Lexend-Regular.ttf"
                            halign: "center"
                            theme_text_color: "Secondary"
                            markup: True
                                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 350  # Adjust to fit both the image and the label
    
                        Image:
                            source: "Images/Jared.jpg"
                            size_hint: None, None
                            size: 300, 300
                            pos_hint: {'center_x': 0.5}
    
                        MDLabel:
                            id: one
                            text: "[b][color=#000000]Larios, Djohn Jared[/color][/b] - Data Analyst, Project Manager, Programmer"
                            halign: "center"
                            theme_text_color: "Secondary"
                            font_name: "FONTS/Lexend-Regular.ttf"
                            markup: True
                    
                    
    
                    MDLabel:
                        text: "User-Centric Focus"
                        halign: "center"
                        font_style: "H6"
                        bold: True
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 200
                        spacing: 20
                        
                        
                        MDLabel:
                            text: "Provides [b][i]Dictionaries[/i][/b] containing daily [i][b]Technical Words[/b][/i], [i][b]Slangs[/b][/i], and [i][b]Abbreviations[/b][/i] commonly used today"
                            halign: "center"
                            font_style: "Body1"
                            markup: True
                            font_size: "15sp"
                           
                        
                        MDLabel:
                            text: "Helps users develop Critical Thinking skills with [i][b]Quizzes[/b][/i] on responsible netizenship"
                            halign: "center"
                            font_style: "Body1"
                            font_size: "15sp"
                            markup: True
                            
                        MDLabel:
                            text: "Has a [i][b]Resource Library[/b][/i] that provides easy-to-access sites and allows self-paced learning"
                            halign: "center"
                            font_style: "Body1"
                            font_size: "15sp"
                            markup: True
                  
                        MDLabel:
                            text: "Displays [i][b]Videos[/b][/i] on electronic processes to help navigate the digital world"
                            halign: "center"
                            font_style: "Body1"
                            font_size: "15sp"
                            markup: True
       
    
                    MDLabel:
                        text: "Contact Information"
                        halign: "center"
                        font_style: "H6"
        
                    MDLabel:
                        text: "acarannessa@gmail.com - Acar, Annessa"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"
                        
                    MDLabel:
                        text: "neiltalaincatilo@gmail.com - Catilo, Neil"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"
                    
                    MDLabel:
                        text: "delenjohnm@gmail.com - Delen, John"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"
                        
                    MDLabel:
                        text: "kellybalitaangelo@gmail.com - Gonzales, Kelly"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"
                        
                    MDLabel:
                        text: "djohnjaredlarios78@gmail.com - Larios, Djohn Jared"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"

"""
from kivy.uix.screenmanager import Screen, ScreenManager

class AboutUsScreen(Screen):
    pass
