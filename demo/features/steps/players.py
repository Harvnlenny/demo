from behave import given, when
from pages.home.home_page import HomePage

@when('a name is typed into the search field')
def player(context):
    player_name = "Bernie Kosar"
    hp = HomePage(context.driver)
    hp.player_search(player_name)