# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
import mission_to_mars
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId



# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)


# Connect to a database. Will create one if not already available.
db =client.app

db.mission_to_mars.drop()



@app.route('/')
def index():
    
    entries = mongo.db.mission_to_mars.find_one()
      
    print(entries)
            
    for doc in entries:
        
            print(doc)
    
    
    
    
    return render_template("index.html", entries=entries)




   

@app.route("/scrape")
def scrape():
    
    entries = mongo.db.mission_to_mars
    mission_info = mission_to_mars.scrape_mars()
    
    
     # Run scraped functions
    
    
    
    
     # Redirect back to home page 
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)




