
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

# help manage the design, texts, placements of elements, setting screen setup, and binding actions
helper_article = '''

<ArticleScreen>
    name: "Article"
    
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size  
        MDBoxLayout:
            orientation: "vertical"
        
            MDTopAppBar:
                title: 'Articles'
                left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
                pos_hint: {'top': 1}
        
            MDTabs:
                id: tabs
            


<TabInternetOverview>:
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size  
        ScrollView:
            MDList:
                OneLineListItem:
                    id: l1
                    text: "[u]Digital Literacy Imperative[/u]"
                    markup: True
                    on_release: app.open_link("https://www.csis.org/analysis/digital-literacy-imperative")
                OneLineListItem:
                    text: "[u]History of the Internet[/u]"
                    markup: True
                    on_release: app.open_link("https://www.internetsociety.org/internet/history-internet/?gad_source=1")
                OneLineListItem:
                    text: "[u]What Can You Do Online?[/u]"
                    markup: True
                    on_release: app.open_link("https://edu.gcfglobal.org/en/internetbasics/what-can-you-do-online/1/")
                OneLineListItem:
                    text: "[u]How to Use the Internet[/u]"
                    markup: True
                    on_release: app.open_link("https://www.wikihow.com/Use-the-Internet")

<TabApplicationGuides>:
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size  
        ScrollView:
            MDList:
                OneLineListItem:
                    text: "[u]How to Install Apps[u]"
                    markup: True
                    on_release: app.open_link("https://support.google.com/android/answer/9457058?hl=en")
                OneLineListItem:
                    text: "[u]Facebook Guide[u]"
                    markup: True
                    on_release: app.open_link("https://blog.hubspot.com/marketing/how-to-use-facebook")
                OneLineListItem:
                    text: "[u]Messenger Guide[u]"
                    markup: True
                    on_release: app.open_link("https://www.wikihow.com/Use-Facebook-Messenger")
                OneLineListItem:
                    text: "[u]YouTube Guide[u]"
                    markup: True
                    on_release: app.open_link("https://www.lifewire.com/how-to-use-youtube-2655498")
                OneLineListItem:
                    text: "[u]TikTok Guide[u]"
                    markup: True
                    on_release: app.open_link("https://blog.hubspot.com/marketing/how-to-use-tiktok")

<TabDigitalNewspapers>:
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size  
        ScrollView:
            MDList:
                OneLineListItem:
                    text: "[u]Manila Bulletin[u]"
                    markup: True
                    on_release: app.open_link("https://manilabulletin.pressreader.com/")
                OneLineListItem:
                    text: "[u]Philippine Daily Inquirer[u]"
                    markup: True
                    on_release: app.open_link("https://philippinedailyinquirerplus.pressreader.com/")
                OneLineListItem:
                    text: "[u]The Manila Times[u]"
                    markup: True
                    on_release: app.open_link("https://www.manilatimes.net/print-edition")

<TabOnlineChannels>:
    RelativeLayout:
        Image:
            source: 'Images/blue.jpg'
            allow_stretch: True
            keep_ratio: False
            opacity: 0.2
            pos: self.pos
            size: self.size  
        ScrollView:
            MDList:
                OneLineListItem:
                    text: "[u]Radio Stations[u]"
                    markup: True
                    on_release: app.open_link("https://www.radio-philippines.com/#google_vignette")
                OneLineListItem:
                    text: "[u]Live Televisions[u]"
                    markup: True
                    on_release: app.open_link("https://www.squidtv.net/asia/philippines/")
                    
'''

# Define each tab class inheriting from MDFloatLayout and MDTabsBase
class TabInternetOverview(MDFloatLayout, MDTabsBase):
    pass

class TabApplicationGuides(MDFloatLayout, MDTabsBase):
    pass

class TabDigitalNewspapers(MDFloatLayout, MDTabsBase):
    pass

class TabOnlineChannels(MDFloatLayout, MDTabsBase):
    pass


class ArticleScreen(Screen):

    def on_enter(self):
        # Add specific tabs with content
        tabs = self.ids.tabs
        tabs.add_widget(TabInternetOverview(title="Internet Overview"))
        tabs.add_widget(TabApplicationGuides(title="Application Guides"))
        tabs.add_widget(TabDigitalNewspapers(title="Digital Newspapers"))
        tabs.add_widget(TabOnlineChannels(title="Online Channels"))

    def clear_tabs(self): #to clear tabs after exiting article screen
        """Clears all tabs from the MDTabs widget."""
        tabs = self.ids.tabs
        for tab in tabs.get_tab_list():  # Iterate through all tabs
            tabs.remove_widget(tab)




