# Chill_Com

This project was a group effort, the product itself is a very soft means of anxiety therapy, it detects you emotions based off of Google's Vision API and generated animation that will calm you accordingly. It also has text input as well as overall generally relaxing UX.

## Motivation
This was a submission for nwHacks, a prominent hackathon on the west coast, where we (the dev team) wanted to created a web app that contributed to social good. With social anxiety being a large issue, we thought that some means of mitigating stress and tension would be a great way to reach our goal.
 
## Screenshots
Under Construction

## Tech/framework used
Built with:
- [Django](https://www.djangoproject.com/)
- [Google Vision API](https://cloud.google.com/vision/docs/)
- [Google Cloud](https://cloud.google.com/)


## Setup
You will need a google cloud account with credits availible on it. As well as [install and initialize the Cloud SDK](https://cloud.google.com/sdk/docs/)
1. Acquire new credentials to use the Cloud SQL Admin API:
```gcloud auth application-default login```
2. Clone the git repo
```git clone https://github.com/gitUmaru/chillCom```
3. Change directory
```cd chillCom```
4. Enable the Cloud SQL Admin API
```gcloud services enable sqladmin```
5. Install the Cloud SQL Proxy
Right-click https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe and select Save Link As to download the proxy. Rename the file to cloud_sql_proxy.exe.
6. *Start Cloud SQL Proxy
```cloud_sql_proxy.exe -instances="nwhacks20:us-central1:nwhacks"=tcp:3306```
7. Create env
```
pip install virtualenv
pip install django-bootstrap4
virtualenv env
env\scripts\activate
pip install -r requirements.txt
```
8. Run Django
```
pip install --upgrade google-cloud-vision
python manage.py makemigrations
python manage.py makemigrations polls
python manage.py makemigrations auth
python manage.py migrate
```
9. Run server
```
python manage.py runserver
http://localhost:8000
```
#### *Optional Steps (Initialize your own Cloud SQL Instance)
1. [Create a Cloud SQL Sequence for MySQL 2nd gen instance](https://cloud.google.com/sql/docs/mysql/create-instance)
2. Use the Cloud SDK to run the following command where ```[YOUR_INSTANCE_NAME]``` represents the name of your Cloud SQL instance:
```gcloud sql instances describe [YOUR_INSTANCE_NAME] ```. In the output, note the value shown for ```[CONNECTION_NAME]```. The ```[CONNECTION_NAME]``` value is in the format ```[PROJECT_NAME]:[REGION_NAME]:[INSTANCE_NAME]```.
3. Start the Cloud SQL Proxy by using the ```[CONNECTION_NAME]``` value from the previous step:
```cloud_sql_proxy.exe -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306```
4. Create a new database by using the Cloud Console for your Cloud SQL instance polls-instance. For example, you can use the name polls. Create a new user by using the Cloud Console for your Cloud SQL instance polls-instance.

## Deploy the App to the App Engine Environment
1. ```python manage.py collectstatic```
2. ```gcloud app deploy```
3. ```https://<your-project-id>.appspot.com```




[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=appengine/standard_python37/django/README.md

This repository is an example of how to run a [Django](https://www.djangoproject.com/) 
app on Google App Engine Standard Environment. It uses the 
[Writing your first Django app](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) as the 
example app to deploy.


# Tutorial
See our [Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.
