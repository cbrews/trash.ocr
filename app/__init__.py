import pkgutil
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.authentication import Auth

web = Flask(__name__, template_folder="../templates")
web.config.from_object('config')
db = SQLAlchemy(web)
auth = Auth()

# Load all application controllers
web_entrypoint = "routes"
for importer, module, ispkg in pkgutil.iter_modules(__path__):
    if ispkg:
        package = "%s.%s.%s" % (__name__, module, web_entrypoint)
        if pkgutil.find_loader(package) is not None:
            __import__(package)

db.create_all()