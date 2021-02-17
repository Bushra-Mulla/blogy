# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Blogy Project 

## Introduction
A blog is an online diary or journal located on a website. Users can create their own blog and post content that typically articles or sharing any information with others for engaging with them.

### Wireframe
Started the app by designing its layout framework by <a href= 'https://wireframepro.mockflow.com/'>mockflow</a>. 

<img src="img/frame.png">

### ERD
Designing the Entity Relationship Diagram by <a href= 'https://app.diagrams.net/'>Draw.io</a>

<img src="img/erd.png">

### Technologies Used.
* HTML
* CSS
* Bootstrap
* Postages 
* Python 
* Django 
* Trello

### User Stories
* As admin, I should be able to manage blog website
* As admin, I should be able to confirm to publish a blog on the website
* As a User, I should be able to see the article content
* As a User, I should be able to search by article title
* As a User, I should be able to see author profile
* As a User, I should be able to filter the article by its categories
* As a User, I should be able to sign up
* As a User, I should be able to log in
* As a visitors User, I should not be neither able edit, delete on article content or add comments
* As a logged User, I should be able to log out
* As a logged User, I should be able to see all my posts and its status   
* As a logged User, I should be able to create new article
* As a logged User, I should be able to edit an exist article
* As a logged User, I should be able to delete an exist article
* As a logged User, I should be able to add comments to any article
* As a logged User, I should be able to add article to user like list
* As a logged User, I should be able to edit profile information
* As a logged User, I should be able to edit own comments
* As a logged User, I should be able to delete own comments
* As a logged User, I should be able to report any post

## App Preview
### The Website Dimo 

## API Endpoints
These are some of the EndPoints we used in this project

| #  |  Action  |  Method |  URL  |  Description  |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  1|  CRAETE | POST  |   /login |  To login to the user account|
|   2|  CREATE | POST  |/signup   | To create new account|
|   3|   create |post  | | |
|   4|   Add | patch  |   | |
|   5|   delete | delete  |  | |
|   6|   Remove |patch   |   | |
|   7|    Update|patch   |   | |

## Code Installation
#### Python 3.8
Follow instructions to install the latest version of python for your platform in the <a href= 'https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python' target="_blank"> python docs </a> 
#### Django 
Installing Django by type on command line `pip install Django` 

#### Running the server
1- clone the repository using this code:
`git clone https://git.generalassemb.ly/ashwagzabani/Project-4`

2- run the flowing command:
```
CREATE DATABASE blogy
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
3- Open browser to `http://127.0.0.1:8000` to see the website.

4- Open a tab to `http://127.0.0.1:8000/admin/` to open the admin panel and add some.


## Future Features:
- As a User, I should be able to share any articles via social networking like: twitter or Facebook
- As a logged User, I should be able to replay on exist comments

## Collaborating
- <a href= 'https://git.generalassemb.ly/ashwagzabani'>Ashwag Zabani</a>
- <a href='https://git.generalassemb.ly/bushra-mulla'>Bushra Mulla</a>
- <a href= 'https://git.generalassemb.ly/fatmahhelal'>Fatimah Alhelal</a>
