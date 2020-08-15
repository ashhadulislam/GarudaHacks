from flask import Flask, render_template, request,send_from_directory
from flask import jsonify, url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import os



# from models import Result
# initialize a flask object


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# manager = Manager(app)
db = SQLAlchemy(app)




# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)




@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")

@app.route("/addrule",methods=["POST"])
def add_rule():
    from models import Rule


    # return the rendered template
    print("Going to add rule")
    device_name=str(request.form['device_name'])
    parameter=str(request.form['parameter'])
    condition=str(request.form['condition'])
    threshold_value=str(request.form['threshold_value'])
    result=str(request.form['result'])

    print(device_name,parameter,condition,threshold_value)
    new_rule = Rule(device_name, parameter, condition, threshold_value,result)
    db.session.add(new_rule)
    db.session.commit()
    return render_template("index.html")    

if __name__ == "__main__":    
    app.run(debug=True,host="0.0.0.0",port=5001)

