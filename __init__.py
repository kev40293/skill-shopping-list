from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import LOG


class ShoppingListSkill(MycroftSkill):
    def __init__(self):
        super(ShoppingListSkill, self).__init__(name="ShoppingListSkill")

    @intent_handler(IntentBuilder("").require('ShoppingList'))
    def handle_shopping_list(self, message):
        self.speak_dialog('shopping.list')

    @intent_handler(IntentBuilder("").require("Add").require('Item').require("List"))
    def add_item_to_list(self, message):
        item = message.data.get('Item')
        listName = message.data.get('List')
        self.speak_dialog("list.add.item", data={"item": item, "List": listName})
        # Now to add backend code for add

    @intent_handler(IntentBuilder("").require('Remove').require('Item').require('List'))
    def remove_item_from_list(self, message):
        item = message.data.get('Item')
        listName = message.data.get('List')
        self.speak_dialog("list.remove.item", data={"item": item, "List": listName})

    def clear_list(self,message):
        pass

    def send_list(self, message):
        pass

    def create_list(self, message):
        pass

    def delete_list(self, message):
        pass

def create_skill():
    return ShoppingListSkill()

