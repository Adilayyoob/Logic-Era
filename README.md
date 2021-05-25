![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# FK EMP
Farookian event management portal helps you to create and join events 
happening at Farook College. Easy to manage interface and responsive 
pages are the main advantage of FK EMP. Being a responsive and simple 
website, FK EMP is accessible on any devices and support almost any 
browsers. Animated pages in this website give the user a feel-good mood.
And FK EMP requires login to create or join an Event that means FK EMP 
is secure. "Logic-Era" is only a code name for the project.
## Team members
1. Ali Muflih [https://github.com/Alimuflih]
2. Sahal EKZ [https://github.com/sahalekz]
## Team Id
BFH/reczAdB3PEGhWSg25/2021
## Link to product walkthrough
[https://www.loom.com/share/5c6a484540f445f4948016dded41f59e?sharedAppSource=personal_library]
## How it Works ?
1. FK EMP has a welcome page where anyone can view. The welcome page contains 
a small description of FK EMP and below you will be provided with a view which
 is an invitation to the last created event on FK EMP. The welcome page also 
has a link to log in or register. After register and login user reaches the 
home page. 
2. On the home page at the navbar, the user can see the FK-EMP logo, 
link to the home page, link to create the page, link to join page and a button 
to log out. The home page shows a card view of Upcoming Events and below two 
cards show statistics of joined events and created events.
3. On create page, the User has a form to create an event, by submitting the form 
the user can create an event. below which, a table shows user-created events. 
Participants of particular events can be seen by clicking the "view" button 
in the table showing user-created events.User can also delete events by
clicking the "delete" button in a table showing user-created events.
4. On the join page, the user can join in events by selecting events from the 
select box and clicking "join". The upcoming event list is provided on top to 
assist join. Joined events can be seen in the "joined events" table below. 
User can delete join by "clicking" the delete button in particular events. 
5. In every view, clicking images shows an enlarged view.
## Link to product host
[https://fk-emp.herokuapp.com/]
## Libraries used
Python 3.8.5
virtualenv 20.4.6
arabic-reshaper==2.1.3
asgiref==3.3.4
Django==3.2.3
future==0.18.2
gunicorn==20.1.0
html5lib==1.1
Pillow==8.2.0
PyPDF2==1.26.0
python-bidi==0.4.2
pytz==2021.1
reportlab==3.5.67
six==1.16.0
sqlparse==0.4.1
webencodings==0.5.1
whitenoise==5.2.0
## How to configure
1. python should be installed
   Download python from https://www.python.org/downloads/ 
   (Note: While installing python tic add to PATH variable)
2. Install virtual environment to your project folder
   To install code in command line is : 
   pip install virtualenvwrapper-win
3. make a virtual env 
   mkvirtualenv myproject 
   (Note: myproject is name, it can vary according to you)
4. Get inside vertual environment by 
   .\myproject\Scripts\activate
5. Install django by code
   pip install django
6. Rest is coding
## How to Run
1. Go to folder in Command line.
2. Activate vertual environment. ubuntu : source myproject/bin/activate || windows :   .\myproject\Scripts\activate
3. Run requirements.txt by code: - pip install -r requirements.txt
4. To open server: - python manage.py runserve .       (Server provide url in which you can see site. Eg: http://127.0.0.1:8000/)
5. To close server - ctrl+c
6. Migrate making, code: python manage.py makemigrations
7. Migrateing , code: python manage.py migrate 
   (Note: To get out of vertualenvironment code is : deactivate)  