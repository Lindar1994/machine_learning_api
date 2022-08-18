# How to deploy a model
* Follow the python developer class to create instance on GCP
* Modify this folder 
* Zip the folder and upload it to GCP instance
* Ssh into your machine: 
```
ssh user_name@IP
sudo apt-get update 
sudo apt-get install zip unzip
```
* Install pip3 on gcp & unzip the folder & install packages
```
pip3 install -r requirements.txt 
```
* Watch `Making Web App Available to End Users` on techlent & set up firewall & run those commands on gcp instance 
* To test whether the api works, in a jupyter notebook
```import requests
df = pd.read_csv('data/sales.csv')
test_row = df.iloc[0,:].to_dict()
d = {'query':test_row}
url = 'http://INSERT_PUBLIC_IP:5000/'
headers =  {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.get(url, data=json.dumps(d),headers=headers,timeout=3)
response.json()
```

