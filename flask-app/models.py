# from app import db
# print("At models")
from app_factory import db
from sqlalchemy.dialects.postgresql import JSON

# from sqlalchemy.dialects.postgresql import JSON


class Rule(db.Model):
    __tablename__ = 'rules'

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String())
    parameter = db.Column(db.String())
    condition = db.Column(db.String())
    threshold_value = db.Column(db.String())
    result =  db.Column(db.String())
    
    # result_no_stop_words = db.Column(JSON)

    def __init__(self, device_name, parameter, condition, threshold_value, result):
        self.device_name = device_name
        self.parameter = parameter
        self.condition = condition        
        self.threshold_value = threshold_value
        self.result=result
        

    def __repr__(self):
        return '<id {}, device_name {}, parameter, {}, condition {},\
        threshold_value {}, result= {} >'.format(self.id,
            self.device_name,self.parameter,self.condition,
            self.threshold_value,self.result)
    
    def serialize(self):
        return {
            'id': self.id, 
            'device_name': self.device_name,
            'parameter': self.parameter,
            'condition': self.condition,
            'threshold_value':self.threshold_value,
            'result': self.result
        }       


class HealthData(db.Model):
    __tablename__ = 'healthdata'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String())
    userName = db.Column(db.String())
    device_name = db.Column(db.String())
    detail_results = db.Column(JSON)
    result =  db.Column(db.String())
    
    # result_no_stop_words = db.Column(JSON)

    def __init__(self, timestamp, userName, device_name, detail_results):
        self.timestamp = timestamp
        self.userName = userName
        self.device_name = device_name        
        self.detail_results = detail_results        
        

    def __repr__(self):
        return '<id {}, timestamp {}, userName, {}, device_name {},\
        detail_results {} >'.format(self.id,self.timestamp,
            self.userName,self.device_name,self.detail_results)
    
    def serialize(self):
        return {
            'id': self.id, 
            'timestamp': self.timestamp,
            'userName': self.userName,
            'device_name': self.device_name,
            'detail_results':self.detail_results            
        }                

# print("End of models")