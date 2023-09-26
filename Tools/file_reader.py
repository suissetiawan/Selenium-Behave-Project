import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read("Config/setup.cfg")
    return config.get(section, key)


def get_element(section, key):
    config = configparser.ConfigParser()
    config.read("Config\locator_element.cfg")
    return config.get(section, key)