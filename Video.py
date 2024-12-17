from kivy.uix.screenmanager import Screen

# help manage the design, texts, placements of elements, setting screen setup, and binding actions
video_helper = """
<VideoScreen>:
    name: 'video'
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
                title: 'Videos'
                left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
            Widget:
    
        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            padding: 20
            
            MDLabel:
                text: 
                    "Here are some helpful videos"
                font_size: "20sp"
                halign: "center"
                pos_hint: {'center_x': 0.5, 'bottom': 1}
                size_hint_y: None
                height: "200dp"
                
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "[u]Being Safe on the Internet[u]"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        markup: True  # Enables the use of markup
                        halign: "center"
                        on_release: app.open_link("https://youtu.be/HxySrSbSY7o?feature=shared")
                        ImageLeftWidget:
                            source: 'Images/img.png'
            
                    OneLineIconListItem:
                        text: "[u]11 Internet Safety Tips for Your Online Security[u]"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        markup: True  
                        halign: "center"
                        on_release: app.open_link("https://www.youtube.com/watch?v=aO858HyFbKI")
                        ImageLeftWidget:
                            source: 'Images/img_1.png'
            
                    OneLineIconListItem:
                        text: "[u]Online safety for grown ups[u]"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        markup: True 
                        halign: "center"
                        on_release: app.open_link("https://www.youtube.com/watch?v=iCs3aJYXLwo")
                        ImageLeftWidget:
                            source: 'Images/img_2.png'
            
                    OneLineIconListItem:
                        text: "[u]Digital Literacy – Staying safe online[u]"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        markup: True 
                        halign: "center"
                        on_release: app.open_link("https://www.youtube.com/watch?v=EyQeUwqCDWg")
                        ImageLeftWidget:
                            source: 'Images/img_3.png'
            
                    OneLineIconListItem:
                        text: "[u]60 Internet Slang Terms You NEED to Know![u]"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        markup: True  # Enables the use of markup
                        halign: "center"
                        on_release: app.open_link("https://www.youtube.com/watch?v=PVnrDHHJwHM")
                        ImageLeftWidget:
                            source: 'Images/img_4.png'  

"""
class VideoScreen(Screen):
    pass