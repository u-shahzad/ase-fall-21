from myservice import app
from myservice.views.home import home
from myservice.views.calc import calculator

# Declare all blueprints here :)
blueprints = [home, calculator]