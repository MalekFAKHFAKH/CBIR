# Content-Based Image Retrieval Projet

## Description
It's about an Image search Engine application that locates, retrieves and displays images from a database alike to one given as a query, using a set of features.

- Database : The used dataset is a combination of 100 000 images related to the e-commerce field. 
- Feature extraction : Relevant features are extracted from these images (using VGG16 algorithm) and stored in elasticsearch after reducing their dimension from 4096 vector's length to 600.
- Throughout the remaining steps, we used elastiknn which is an elasticsearch plugin in order to index images and define the research methodology.
As well we enclosed the work by developing the web interface using Flask.

## Technical documentation
### How to run the application ?

#### Database :
- You can access to our database through this url : 
`https://drive.google.com/file/d/1TPEGpHC9_2l1n1aoOjRFxJGmcN0Kg6Ke/view?usp=sharing`

#### Elasticsearch
- Download and Install elasticsearch 7.14.1 
- Install Elastiknn plugin
- Index each image with his Id, feature vector and path

#### Run the application :
- Install dependencies : tensorflow...
- `Flask run`

![Home](https://user-images.githubusercontent.com/96119446/148931061-90c16b15-45e4-4cde-8949-83fbdace8997.PNG)

![res1](https://user-images.githubusercontent.com/96119446/148929779-8119ddb1-237b-445d-b3ff-b2635dd8c260.PNG)

![re2](https://user-images.githubusercontent.com/96119446/148929795-2e21ad44-d454-49f4-bd63-8d7186d6295b.PNG)
