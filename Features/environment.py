from Tools import file_reader
from selenium.webdriver import Firefox, Chrome


def before_scenario (context, scenario):
    browser = file_reader.read_config("precondition","browser")
    if (browser.upper() == 'CHROME'):
        context.driver = Chrome()
    elif (browser.upper() == 'FIREFOX'):
        context.driver = Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    context.driver.close()