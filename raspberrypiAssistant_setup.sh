: ' Create google cloud project. 
 	Click  API & service  from side bar
 	Go to -> Library. Search for Google Assistant. Enable it
	Create and download OAuth Credentials. client_secret.json file.
'

sudo apt install python3-dev
sudo apt install portaudio19-dev libffi-dev 

sudo pip install google-assistant-sdk[samples]

pip install --upgrade google-auth-oauthlib[tool]
google-oauthlib-tool --client-secrets path/to/client_secret_XXXXX.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless﻿

echo "Go enabl 

: ' Gets redirected to a website. Allow it to authenicate
 Now enable access permissions from myaccount.google.com/activitycontrols

 Now run Assistant
'
echo "Did you enable access permissions? check comments : "
read permissions

 python -m googlesamples.assistant

# up and running!!
