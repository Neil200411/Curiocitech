from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import random

# help manage the design, texts, placements of elements, setting screen setup, and binding actions
quiz_helper = """
<StartQuizScreen>:
    name: "start"
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
                title: 'Quiz      '
                anchor_title: "center" 
                left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
            Widget:
            
            BoxLayout:
                orientation: 'vertical'
                
                MDLabel:
                    text: root.star_message
                    halign: 'center'
                    pos_hint: {'center_x': 0.5, 'top': 1}
                    size_hint_y: None
                    height: "410dp"
                    markup : True
        
            BoxLayout:
                orientation: 'vertical'
                pos_hint: {'center_x': 0.5, 'top': 1}
                MDRaisedButton:
                    text: "Start Quiz"
                    pos_hint: {'center_x': 0.5,'top': 1}
                    halign: 'center'
                    size_hint_y: None
                    height: "10dp"
                    md_bg_color: [199 / 255, 143 / 255, 87 / 255, 1]
                    on_release: app.show_main_screen_quiz()
                Widget:


<QuizScreen>:
    name: "quiz"
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
                title: "Quiz"
                md_bg_color: app.theme_cls.primary_color
                specific_text_color: 1, 1, 1, 1
                left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
                md_bg_color: [30 / 255, 30 / 255, 102 / 255, 1]
    
            BoxLayout:
                pos_hint: {'center_x': .5,'center_x': .5}
                id: question_area
                orientation: 'vertical'
                padding: 20
                spacing: 10
    
            GridLayout:
                id: button_area
                padding: 20
                spacing: 10
                cols: 2  # Define 2 columns for the buttons  

"""

class StartQuizScreen(Screen):
    star_message = """
    
    [size=25][b]QUIZ ME![/b][/size]
    
You will be given a set of situational questions that you need 
to answer based on your own understanding. 
This will serve as a test for your digital literacy. 
At the end of the quiz, you will be shown your score.

[size=25][b]How?[/b][/size]

1. Press "Start Quiz".

2. Once a question is displayed, tap your answer from the choices. Green means correct while red means incorrect.

3. Keep on answering until the quiz finishes and your score is displayed.
"""
    pass


class QuizScreen(Screen):
    def on_enter(self):
        self.questions = [
            {
                "question": "Identifying Reliable Information Online\nYou are reading a news article online, but you’re unsure if the website is trustworthy. What should you do?",
                "choices": [
                    "Share the article \non social media \nwithout verifying it.",
                    "Check the website’s \n'About Us' page and look for \ninformation about the authors.",
                    "Search for similar \narticles on reputable \nnews platforms.",
                    "Rely on the number of \nlikes and comments to \njudge its credibility.",
                ],
                "answer": 1,
            },
            {
                "question": "Using New Software Tools\nYour workplace has introduced new project management software, but you are unfamiliar with it. How should you approach learning it?",
                "choices": [
                    "Experiment with \nrandom buttons \nuntil you figure it out.",
                    "Watch tutorials \nand review the \nsoftware's user guide.",
                    "Wait for someone \nelse to teach \nyou how to use it.",
                    "Avoid using the \nsoftware and stick \nto old methods.",
                ],
                "answer": 1,
            },
            {
                "question": "Strengthening Password Security\nYou need to create a new password for your online bank account. What is the most secure approach?",
                "choices": [
                    "Use your name \nand birthdate so \nit’s easy \nto remember.",
                    "Choose a long, \nrandom combination of \nletters, numbers\n, and special characters.",
                    "Use the same \npassword y\nou’ve used \non other websites.",
                    "Write the password \non a sticky note and \nattach it to your \ncomputer monitor.",
                ],
                "answer": 1,
            },
            {
                "question": "Avoiding Online Scams\nYou receive an email claiming you’ve won a cash prize but need to provide personal information to claim it. What should you do?",
                "choices": [
                    "Immediately provide \nthe requested information.",
                    "Delete the email and \nblock the sender.",
                    "Click on the link to \ninvestigate further.",
                    "Reply asking for more \ndetails about the prize.",
                ],
                "answer": 1,
            },
            {
                "question": "Managing Digital Well-being\nYou notice you are spending too much time on social media, affecting your productivity. What would be the best course of action?",
                "choices": [
                    "Turn off your  \nphone completely during  \nwork hours.",
                    "Set specific \ntime limits for using\n social media apps.",
                    "Uninstall all \nsocial media apps \npermanently.",
                    "Ignore the \nproblem and hope \nit resolves itself.",
                ],
                "answer": 1,
            },
            {
                "question": "Understanding Digital Collaboration\nYou’re working on a group project, and a teammate shares a document for collaboration on a platform you’ve never used before. How do you handle this?",
                "choices": [
                    "Request the teammate \nto use a platform \nyou’re comfortable with.",
                    "Explore the platform, \nuse its help feature, \nand ask teammates for tips.",
                    "Avoid participating until \nsomeone else uploads the \nfinal version.",
                    "Print the document and \nprovide feedback in \nperson instead.",
                ],
                "answer": 1,
            },
            {
                "question": "Protecting Personal Data\nYou are signing up for a free online service, and it asks for extensive personal information, including your address and phone number. What is the best response?",
                "choices": [
                    "Provide all the \ninformation to \naccess the service.",
                    "Skip signing \nup and look for\n alternative platforms.",
                    "Read the privacy policy \nto understand how \nyour data will be used.",
                    "Use false\n information to \ncreate the account.",
                ],
                "answer": 2,
            },
            {
                "question": "Evaluating Media Content\nA video on social media is going viral, claiming a groundbreaking scientific discovery. How do you verify its authenticity?",
                "choices": [
                    "Believe it \nbecause it has many\n views and shares.",
                    "Check the credentials of \nthe source and look for \npeer-reviewed articles.",
                    "Assume it's fake because \nmost viral content is \nunreliable.",
                    "Share it \nwith friends to \nget their opinions.",
                ],
                "answer": 1,
            },
        ]

        random.shuffle(self.questions)  # Shuffle the order of the questions
        self.question_index = 0
        self.correct_answers = 0

        # Ensure widgets are ready before trying to access ids
        Clock.schedule_once(self.load_question, .5)

    def load_question(self, *args):
        # Access ids only after the screen has been loaded

        self.right_answ = SoundLoader.load('Sounds/rightanswer-95219.mp3')
        self.wrong_answ = SoundLoader.load('Sounds/wronganswer-37702.mp3')

        question_area = self.ids.question_area
        button_area = self.ids.button_area

        # Clear previous content
        question_area.clear_widgets()
        button_area.clear_widgets()

        # Load the current question
        question = self.questions[self.question_index]

        # Shuffle the choices and update the correct answer index
        choices = question["choices"]
        correct_answer_index = question["answer"]
        shuffled_choices = choices[:]
        random.shuffle(shuffled_choices)
        new_correct_answer_index = shuffled_choices.index(choices[correct_answer_index])

        # Update the question with the new shuffled answer index
        question["choices"] = shuffled_choices
        question["answer"] = new_correct_answer_index

        question_label = MDLabel(
            text=question["question"],
            halign="center",
            font_style="H5",
        )
        question_area.add_widget(question_label)

        # Load answer buttons
        for index, choice in enumerate(shuffled_choices):
            btn = MDRaisedButton(
                text=choice,
                md_bg_color=[199 / 255, 143 / 255, 87 / 255, 1],
                pos_hint={'center_x': .5, 'top': 1},
                size_hint=(.5, None),
                height=50,
                on_release=lambda btn, idx=index: self.check_answer(idx),
            )
            button_area.add_widget(btn)

    def play_right(self):
        if self.right_answ:
            self.right_answ.play()

    def play_wrong(self):
        if self.wrong_answ:
            self.wrong_answ.play()

    def check_answer(self, selected_index):
        question = self.questions[self.question_index]
        button_area = self.ids.button_area

        # Highlight answers
        for idx, button in enumerate(reversed(button_area.children)):
            if idx == question["answer"]:
                button.md_bg_color = (0, 1, 0, 1)  # Green for correct
                button.on_release = self.play_right
            elif idx == selected_index:
                button.md_bg_color = (1, 0, 0, 1)
                button.on_release = self.play_wrong# Red for incorrect

        if selected_index == question["answer"]:
            self.correct_answers += 1

        # Move to the next question after a short delay
        self.question_index += 1
        if self.question_index < len(self.questions):
            Clock.schedule_once(lambda dt: self.load_question(), 1)
        else:
            Clock.schedule_once(lambda dt: self.show_summary(), 1)

    def show_summary(self):
        screen = self
        question_area = screen.ids.question_area
        button_area = screen.ids.button_area

        # Clear widgets
        question_area.clear_widgets()
        button_area.clear_widgets()

        # Display summary
        summary_label = MDLabel(
            text=f"You answered {self.correct_answers} out of {len(self.questions)} correctly!"
                 f"\n"
                 f"\n Do You Want To Try Again?",
            halign="center",
            valign= "top",
            font_style="H4",
            size_hint_y=None,
            height=300,
        )

        yes = MDRaisedButton(
            text="YES",
            size_hint=(.5, None),
            height=50,
            md_bg_color=[199 / 255, 143 / 255, 87 / 255, 1],
            on_release=self.restart_quiz)

        no = MDRaisedButton(
            text="NO",
            size_hint=(.5, None),
            height=50,
            md_bg_color=[199 / 255, 143 / 255, 87 / 255, 1],
            on_release= self.back_start_menu)


        button_area.add_widget(yes)
        button_area.add_widget(no)
        question_area.add_widget(summary_label)

    def back_start_menu(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "start"


    def restart_quiz(self, instance):
        # Reset quiz state
        self.correct_answers = 0
        self.question_index = 0

        # Shuffle the questions again for a fresh quiz
        random.shuffle(self.questions)

        # Go back to the quiz screen
        self.manager.current = "quiz"

        # Ensure the next question is loaded after navigating back to the quiz screen
        Clock.schedule_once(self.load_question, .2)

