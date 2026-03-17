import os

def load_template(template_name):
    path = os.path.join("templates", template_name)
    
    with open(path, "r") as f:
        return f.read()