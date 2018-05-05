from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class ShoppingListSkill(MycroftSkill):
    def __init__(self):
        super(ShoppingListSkill, self).__init__(name="ShoppingListSkill")

    @intent_handler(IntentBuilder("").require('ShoppingList'))
    def handle_shopping_list(self, message):
        self.speak_dialog('shopping.list')

    @intent_handler(IntentBuilder("").require('AddItem'))
    def add_item_to_list(self, message):
        self.speak_dialog("shopping.list.add")


def create_skill():
    return ShoppingListSkill()

