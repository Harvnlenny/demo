from selenium import webdriver



def before_all(context):
    context.driver = webdriver.Chrome()
    context.URL = "https://www.pro-football-reference.com/"


def after_all(context):
    context.driver.quit()
