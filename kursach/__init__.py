from flask import Flask
import os
import sys
project_root = os.path.dirname(__file__)
print(project_root)
static_path = os.path.join(project_root, 'templates')
print(static_path)
template_path = os.path.join(project_root, './')
app = Flask(__name__)
import kursach.views
if __name__ == "__main__":
    app.run(TEMPLATES_AUTO_RELOAD=True)