from pymongo import MongoClient
from flask import(Flask, render_template, jsonify)

#------------------------------------------------------------------------------------#
# Flask Setup #
#------------------------------------------------------------------------------------#
## app = Flask(__name__)  ## For Local 

app = Flask(__name__, template_folder='templates') # For Heroku

#------------------------------------------------------------------------------------#
# Local MongoDB connection #
#------------------------------------------------------------------------------------#
conn = "mongodb://localhost:27017"
client = MongoClient(conn)
# create / Use database
db = client.healthi_db
#------------------------------------------------------------------------------------#
# MLab MongoDB connection #
#------------------------------------------------------------------------------------#
#### Connection for remote host
####conn = 'mongodb://<dbuser>:<dbpassword>@ds255332.mlab.com:55332/healthi_db'

# client = MongoClient(conn,ConnectTimeoutMS=30000)
# db = client.get_default_database()
#------------------------------------------------------------------------------------#
#### Initialise and populate the Collection / Database
#------------------------------------------------------------------------------------#
# def InitializeDataBase():
#     CreateMongoDataBase()
#     mongodbset()

#------------------------------------------------------------------------------------#
# Home Page
@app.route("/")
def home():
    return(render_template("index.html"))

# Route to 
@app.route("/routes")
def routes():
    
    
    sample_list.append(Routes_dict)
    return jsonify(sample_list)

# Route to 
@app.route("<>")
def XXXXXXXX(): 



    return jsonify(sample_list)

# Route to display 
@app.YYYYYY("<>")
def rankszscores( ):
    


    return jsonify(sample_list)    

#Route to display all the states present in the database
@app.route("-----")
def state():
    



    return jsonify(sample_list)  


#------------------------------------------------------------------------------------#
# Initiate Flask app
#------------------------------------------------------------------------------------#
if __name__=="__main__":
    connect_args={'check_same_thread':False} 
    InitializeDataBase() 
    app.run(debug=True)
    

