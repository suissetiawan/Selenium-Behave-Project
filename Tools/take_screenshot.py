import time
def page_screenshot(driver,name):
    driver.save_screenshot('Documentation/Screenshot/'+name+'.png')
    time.sleep(1)