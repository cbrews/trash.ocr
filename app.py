# Initialize Application
from app import web
web.run(host='0.0.0.0', port=web.config["PORT"], debug=web.config["DEBUG"])