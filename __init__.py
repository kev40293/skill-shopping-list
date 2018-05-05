from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class ShoppingListSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('ShoppingList'))
    def handle_shopping_list(self, message):
        self.speak_dialog('shopping.list')


def create_skill():
    return ShoppingListSkill()

