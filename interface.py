
from flask import Flask,jsonify,render_template,url_for,request
from util import MumbaiPrice
import config
app=Flask(__name__)
@app.route('/')
def home():
    return jsonify({"Home":"We are at home page"})
@app.route('/predict')
def predict():
    data=request.form
    Area=data['Area']
    Bedrooms=data['Bedrooms']
    New_Resale=data['New_Resale']
    Gymnasium=data['Gymnasium']
    Lift_Available=data['Lift_Available']
    Car_Parking=data['Car_Parking']
    Maintenance_Staff=data['Maintenance_Staff']
    Security=data['Security']
    Play_Area=data['Play_Area']
    Clubhouse=data['Clubhouse']
    Intercom=data['Intercom']
    Landscaped_Gardens=data['Landscaped_Gardens']
    Indoor_Games=data['Indoor_Games']
    Gas_Connection=data['Gas_Connection']
    Jogging_Track=data['Jogging_Track']
    Swimming_Pool=data['Swimming_Pool']
    Location=data['Location']
    obj=MumbaiPrice(Area,Bedrooms,New_Resale,Gymnasium,Lift_Available,Car_Parking,Maintenance_Staff,Security,Play_Area,Clubhouse,Intercom,Landscaped_Gardens,Indoor_Games,Gas_Connection,Jogging_Track,Swimming_Pool,Location)
    predict_price=obj.prediction()
    return jsonify({"Result":f"Predicted price will be {predict_price}"})
if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT,debug=True)
