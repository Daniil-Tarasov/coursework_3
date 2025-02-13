import os
from configparser import ConfigParser


current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "../config/database.ini")


def config(
    filename=path,
    section="postgresql",
):
    # create a parser
    parser = ConfigParser(interpolation=None)
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} is not found in the {1} file.".format(section, filename))
    return db
