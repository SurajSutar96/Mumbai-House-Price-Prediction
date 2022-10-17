import numpy as np
import pickle
import json
class MumbaiPrice():
    def __init__(self,Area,Bedrooms,New_Resale,Gymnasium,Lift_Available,Car_Parking,Maintenance_Staff,Security,Play_Area,Clubhouse,Intercom,Landscaped_Gardens,Indoor_Games,Gas_Connection,Jogging_Track,Swimming_Pool,Location):
        self.area=Area
        self.Bedrooms=Bedrooms
        self.New_Resale=New_Resale
        self.Gymnasium=Gymnasium
        self.Lift_Available=Lift_Available
        self.Car_Parking=Car_Parking
        self.Maintenance_Staff=Maintenance_Staff
        self.Security=Security
        self.Play_Area=Play_Area
        self.Clubhouse=Clubhouse
        self.Intercom=Intercom
        self.Landscaped_Gardens=Landscaped_Gardens
        self.Indoor_Games=Indoor_Games
        self.Gas_Connection=Gas_Connection
        self.Jogging_Track=Jogging_Track
        self.Swimming_Pool=Swimming_Pool
        self.Location="Location_"+Location
    def data(self):
        with open('mumbai_house.pkl','rb')as f:
            self.model=pickle.load(f)
        with open('mumbai_house_data.json','r')as f:
            self.json_data=json.load(f)
    def prediction(self):
        self.data()
        array=np.zeros(len(self.json_data['columns']))
        location_index=np.where(self.json_data['columns'].index(self.Location))
        array[0]=self.area
        array[1]=self.Bedrooms
        array[2]=self.New_Resale
        array[3]=self.Gymnasium
        array[4]=self.Lift_Available
        array[5]=self.Car_Parking
        array[6]=self.Maintenance_Staff
        array[7]=self.Security
        array[8]=self.Play_Area
        array[9]=self.Clubhouse
        array[10]=self.Intercom
        array[11]=self.Landscaped_Gardens
        array[12]=self.Indoor_Games
        array[13]=self.Gas_Connection
        array[14]=self.Jogging_Track
        array[15]=self.Swimming_Pool 
        array[location_index]=1
        predict=self.model.predict([array])[0]
        print(f"Predicted price of the house is {predict.round(2)} ₹ ")
        return predict
if __name__=="__main__":
    Area=50000
    Bedrooms=3
    New_Resale=1
    Gymnasium=1
    Lift_Available=1
    Car_Parking=0
    Maintenance_Staff=1
    Security=1
    Play_Area=1
    Clubhouse=1
    Intercom=1
    Landscaped_Gardens=1
    Indoor_Games=1
    Gas_Connection=1
    Jogging_Track=1
    Swimming_Pool=1
    Location="Kharghar"
    obj=MumbaiPrice(Area,Bedrooms,New_Resale,Gymnasium,Lift_Available,Car_Parking,Maintenance_Staff,Security,Play_Area,Clubhouse,Intercom,Landscaped_Gardens,Indoor_Games,Gas_Connection,Jogging_Track,Swimming_Pool,Location)
    obj.prediction()
