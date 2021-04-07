
from flask import Flask
app = Flask(_name_)

@app.route('/')
def Home():
return "มนัสชนก เพ็งมีศรี 6006021612069"


if _name_ == '_main_':
app.debug = True
app.run(host='0.0.0.0', port=80)
