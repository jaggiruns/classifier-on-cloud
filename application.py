import json

from flask import Flask, request, json
#from sklearn.externals joblib
#from azure.storage.blob import BlockBlobService

app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():    
    # Parse request body for model input 
    body_dict = request.get_json(silent=True)    
    data = body_dict['data']     
    
    # Load model
    #model = load_model(MODEL_FILE_NAME)
    # Make prediction 
    #prediction = model.predict(data).tolist()
    # Respond with prediction result
    result = {'prediction': 'prediction is 2386'}    
   
    return json.dumps(result)
#if __name__ == '__main__':    
    # listen on all IPs 
    #app.run()


#def load_model(key):    
    #ACCOUNT_KEY = ''
    #CONTAINER_NAME = 'model'

    #block_blob_service = BlockBlobService(account_name= 'ticketclassification2386', account_key=ACCOUNT_KEY)

    #generator = block_blob_service.list_blobs(CONTAINER_NAME)

    #fp = open('modelfile', 'ab')

    #for blob in generator:
       # service.get_blob_to_stream(CONTAINER_NAME, blob.name, fp)
	#    model = joblib.load(fp)
    #fp.flush()
    #fp.close()
    #return model


