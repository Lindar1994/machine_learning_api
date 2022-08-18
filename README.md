# How to deploy a model
1.) Follow the python developer class to create instance on GCP
2.) Modify this folder 
3.) Zip the folder and upload it to GCP instance
4.) Ssh into your machine: 
```
ssh user_name@IP
sudo apt-get update 
sudo apt-get install zip unzip
```
5.) Install pip3 on gcp & unzip the folder & install packages
```
pip3 install -r requirements.txt 
```
6.) Watch `Making Web App Available to End Users` & set up firewall & run those commands on gcp instance 
7.) To test whether the api works, in a jupyter notebook
```import requests
df = pd.read_csv('data/sales.csv')
test_row = df.iloc[0,:].to_dict()
d = {'query':test_row}
url = 'http://INSERT_PUBLIC_IP:5000/'
headers =  {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.get(url, data=json.dumps(d),headers=headers,timeout=3)
response.json()
```

