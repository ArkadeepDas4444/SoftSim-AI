import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_template(template_name):
    path = os.path.join(BASE_DIR, "templates", template_name)
    with open(path, "r") as f:
        return f.read()