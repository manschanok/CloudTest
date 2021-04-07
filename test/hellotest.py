
from flask import Flask
app = Flask(__name__)

@app.route("/")
def Home():
  return "มนัสชนก เพ็งมีศรี 6006021612069"


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=80)
