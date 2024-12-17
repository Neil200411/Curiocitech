# help manage the design, texts, placements of elements, setting screen setup, and binding actions
screen_helper = """
<MagicButton@MagicBehavior+MDRaisedButton>
#:import Clock kivy.clock.Clock

ScreenManager:
    
    SplashScreen:
    MainScreen:
    DictionaryScreen:
    TableScreen:
    Table1Screen:
    VideoScreen:
    StartQuizScreen:
    ArticleScreen:
    QuizScreen:
    AboutUsScreen:

<MainScreen>:
    name: 'main'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                RelativeLayout:
                    Image:
                        source: 'Images/blue.jpg'
                        allow_stretch: True
                        keep_ratio: False
                        opacity: .2
                        pos: self.pos
                        size: self.size
                    MDTopAppBar:
                        title: 'Final App'
                        anchor_title: "center"
                        left_action_items: [["menu", lambda x: app.play_click_sound3()]]
                        md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
                        pos_hint: {'top': 1} # Position the top app bar at the top
                    BoxLayout:
                        orientation: 'vertical'
                        
                        MDLabel:
                            text: ''
                            halign: 'center'
                            pos_hint: {'center_x': 0.5, 'top': 1}
                    
                        MDLabel:
                            text: 'GUIDES:'
                            font_size: '30sp'
                            halign: 'center'
                            valign: 'top'
                            pos_hint: {'center_x': 0.5}
                            size_hint_y: None
                            height: "75dp"
                            
                        MDLabel:
                            text: root.text1
                         
                            halign: 'center'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: '30sp'
                            markup: True
                        MDLabel:
                            text: root.text2
                            halign: 'center'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: '30sp'
                            markup: True
                        MDLabel:
                            text: root.text3
                            halign: 'center'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: '30sp'
                            markup: True
                            
                        MDBoxLayout:
                            orientation: 'horizontal'
                            padding: dp(20)
                            spacing: dp(20)
                            
                            Widget: 

        MDNavigationDrawer:
            id: nav_drawer
            radius: [20, 20, 20, 20]
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
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Dictionary'
                                on_release: 
                                    app.show_dictionary()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    icon: 'book-open-variant'
                                    
                            OneLineIconListItem:
                                text: 'Videos'
                                on_release: 
                                    app.show_video()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    icon: 'video-outline'
                            OneLineIconListItem:
                                text: 'Quizzes'
                                on_release:
                                    app.show_quiz()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    icon: 'form-select'
                            OneLineIconListItem:
                                text: 'Resource Library'
                                on_release: 
                                    app.show_article()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    icon: 'newspaper'
                            OneLineIconListItem:
                                text: 'About'
                                on_release: 
                                    app.show_about()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    icon: 'information'
                            OneLineIconListItem:
                                id: tap
                                text: "Dark Mode"
                                on_release:
                                    app.dl()
                                    app.play_click_sound2()
                                IconLeftWidget:
                                    id: icons
                                    icon: 'weather-night' 
    
    """

