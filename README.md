# ImageClassifierServer

Requirements
------------
1. Python 3
2. Conda

How to run
----------
#### Before running the server make sure you have the following set up.

* Make sure to be running in a conda environment
    * First Install [anconda](https://docs.continuum.io/anaconda/install/)
    * conda create --name venv
    * When conda asks `proceed ([y]/n)?` pick yes
    * Now activate the environment `source activate venv`
    
* Now to install the requirements
    * `cd ImageClassifier`
    * `pip install requirements.txt`
  
    Note: If the installation of the requirements didn't work, install each of them one by one. Most of them will install  but some will fail for some reason.
   
  


 
#### Runnin locally
 
 * Run `python debug.py f` this will set the debug variable in settings to true
 * Then run `python manage.py runserver`
 * At this point the website will be running on http://127.0.0.1:8000/upload_picture
  
#### Deplyoing running on Heroku
  
    


