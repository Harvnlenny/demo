from behave import given, when, then
from hamcrest import assert_that, equal_to, contains_string
from pages.home.home_page import HomePage

@when('a name is typed into the search field')
def player(context):
    player_name = "Bernie Kosar"
    hp = HomePage(context.driver)
    hp.player_search(player_name)

@then('the User will be on the page of the Player')
def player(context):
    player_name = "Bernie Kosar"
    full_name = context.driver.find_element_by_xpath("//*[@id='meta']/div[2]/h1")
    full_name_text = full_name.text
    assert_that(full_name_text, contains_string(player_name))