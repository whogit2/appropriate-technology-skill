from mycroft import MycroftSkill, intent_file_handler


class AppropriateTechnology(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('technology.appropriate.intent')
    def handle_technology_appropriate(self, message):
        self.speak_dialog('technology.appropriate')


def create_skill():
    return AppropriateTechnology()

