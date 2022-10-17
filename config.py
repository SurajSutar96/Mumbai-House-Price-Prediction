HOST='0.0.0.0'
PORT=5555
import pickle
import json
with open('mumbai_house.pkl','rb')as f:
    PICKLE=pickle.load(f)
with open('mumbai_house_data.json','r')as f:
    JSON_DATA=json.load(f)
