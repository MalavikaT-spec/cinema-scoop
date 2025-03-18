from flask import *
from public import *
from admin import *
from normal_members import *
from feature_members import *

app=Flask(__name__)

app.secret_key="dfdgdh"
app.register_blueprint(pub)
app.register_blueprint(admin)
app.register_blueprint(normal)
app.register_blueprint(feature)
app.run(debug=True)