import numpy as np
import pickle as pkl
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
from sklearn.decomposition import PCA
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

app = Flask(__name__)
##partie elasticsearch 
es = Elasticsearch('127.0.0.1',port=9200,timeout=600,)
es.cluster.health(wait_for_status='yellow', request_timeout=600)
index = 'rihabmalekcbir'
#source_no_vecs = ['id', 'title', 'author', 'tags', 'labels', 'imgPATH']
source_no_vecs = ['id', 'imgPATH']
# #feature_extraction & pca
fe = FeatureExtractor()
pca = pca = pkl.load(open("E:/RihabMalekCBIR/pca.pkl",'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result1.html', methods=[ 'POST' , 'GET']) 

def search_by_image_query():
  if request.method == 'POST' :

    

    file = request.files['query_img']

            # Save query image
    img = Image.open(file.stream)  # PIL image
    uploaded_img_path = "static/uploaded/" + file.filename
    img.save(uploaded_img_path)

            # #Run search
    img_features = fe.extract(img)
    vector= pca.transform(img_features.reshape(1,-1))[0].tolist()

    image_id = file.filename[:-4]
  
    if image_id==None :
        raise ValueError("Please enter an Image ID or a Feature Vector")
    
    if image_id:
        res =es.search(
            index="rihabmalekcbir", 
            size=12, 
            body={
            "query": {
                "elastiknn_nearest_neighbors": {
                  "vec": {
                    "index": index,
                    "field": "featureVec",
                    "id": image_id
                  },
                  "field": "featureVec",
                  "model": "lsh",
                  "similarity": "l2",
                  "candidates": 100
                }
            }
            }
        )
        url = "http://127.0.0.1:8887"
        answers =[] 
        for hit in res['hits']['hits']:
        
        
            s = hit['_source']
            
            # print(f"ID      {s.get('id', None)}")
            # print(f"Score   {hit.get('_score', None)}")
            
            x=(s.get("imgPATH"))[16:]
            var = url+x
            answers.append(var)     
       
        return render_template('result1.html', query_path=uploaded_img_path,answers=answers)
  else :
        return render_template('result1.html')




if __name__=="__main__":
    app.run("0.0.0.0")