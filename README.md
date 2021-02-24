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
* As a logged user, H should be able to contact with admin by life chating

## App Preview
### The Website Dimo 

## API Endpoints
These are some of the EndPoints we used in this project

| #  |  Action  |  Method |  URL  |  Description  |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|   1| View  | get  | / | To view Home page|
|   2|  CRAETE | POST  |   /login |  To login to the user account|
|   3| CREATE | POST  |/signup   | To create new account|
|   4| View | POST  |/logOut   | To log out from the account|
|   5| CREATE  | post  | /post/create | To create new post|
|   6| View | get  | /post/post_id | To veiw exist post|
|   7| EDIT | PATCH  | /post/<int:pk>/update/  | To edit a specific post|
|   8|   INDEX | get  |  /user/posts/|  To view all user's posts list|
|   9|   INDEX |get   |  /user/posts/published// | To view all user's published posts list | 
|   10|    INDEX |get   | /user/posts/notPublished/  | To view all user's unpublished posts list |
|   11|    INDEX |get   | /user/posts/refused/  | To view all user's refused posts list|
|   12|    INDEX |POST   |  /user/posts/draft/ | To view all user's draft posts list|
|   12|    CREATE |POST   |  /category/create/ | To create new category|
|   13|    Update |patch   |   | |
|   14|    Update |patch   |   | |
|   15|    Update |patch   |   | |
|   16|    Update |patch   |   | |

## Code Installation
#### Python 3.8
Follow instructions to install the latest version of python for your platform in the <a href= 'https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python' target="_blank"> python docs </a> 
#### Django 
Installing Django by type on command line `pip install Django` 
#### Requirements 
Installing all project's requirements by type on command line `pip install -r Requirements.txt` 

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

4- Open a tab to `http://127.0.0.1:8000/admin/` to open the admin panel and add some data.


## Future Features:
- As a User, I should be able to share any articles via social networking like: twitter or Facebook
- As a logged User, I should be able to replay on exist comments

## Collaborating
- <a href= 'https://git.generalassemb.ly/ashwagzabani'>Ashwag Zabani</a>
- <a href='https://git.generalassemb.ly/bushra-mulla'>Bushra Mulla</a>
- <a href= 'https://git.generalassemb.ly/fatmahhelal'>Fatimah Alhelal</a>
