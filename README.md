# csc648-team07

- add ALL your team members to your team's repo.
  
- [Team Lead] Sean Sutherland
- [Front End Lead] Lance Larsen
- [Back End Lead] Corey Humeston
- [Front End] Mark Soriano
- [Front End] Girish Tiwale
- [Back End] Amelie Cameron
- [Back End]  Ali Alavi

# To Work on Repo

```diff
+ Click the GREEN Clone or download button
```
+ Copy the HTTPS to your clipboard
+ Go to a directory (desktop for ease of access)
+ git clone "paste from clipboard here"

## Backend Stuff for Us to Remember

- heroku run python manage.py migrate
- heroku open

- give everyone SSH key for repo
- ask Anthony questions about Heroku

## Windows Users

0) add to collaborators
1) Download Heroku CLI and type "heroku login" from terminal/cmd in your desktop directory. 
   login with your heroku account.
2) Windows - heroku git:clone -a csc648team07
3) cd to cloned file
4) download python 3.6.4 to machine
5) download git to machine
6) use command - pip install pipenv 
7) pipenv --three
8) pipenv install
9) pipenv shell
10) python manage.py collectstatic (if it asks question, type ‘yes’)
11) heroku local web -f Procfile.windows

## Requirements.txt 

Installing prerequisites:
1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: pip install -r requirements.txt in your shell.

https://pip.readthedocs.io/en/1.1/requirements.html
