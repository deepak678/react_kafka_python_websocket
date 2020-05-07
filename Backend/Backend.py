from flask import request
from config import app,producer,consumer
 
messages=[]

@app.route('/',methods=['GET','POST'])
def sendData():
    if request.method=='POST':
        data=request.json
        try:
            print(data['msg'])
            producer.send('test',data['msg'].encode()).get(timeout=300)
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))
        return "success"
    elif request.method=='GET':
        data1=consumerData()
        print(data1)
        return data1
    

def consumerData():
    for msg in consumer:
        return msg.value
    
if __name__ == "__main__":
    app.run(port=5000, debug=False)