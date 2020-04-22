## Install & run locally

Install:
```
git clone https://github.com/samg9/image_upscaler/be_flask.git  
cd be_flask
```  
Create a virtualenv called v:  
```
python3 -m venv v   
```  
Activate it on Linux:
```
. v/bin/activate  
```  
Or on Windows cmd:  
```
v\Scripts\activate.bat  
```  
Install requirements:
```
pip install -r requirements.txt  
```  

export variables
```
export FLASK_APP=routes.py
```

Run app 
```
FLASK run
```
