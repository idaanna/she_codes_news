# Plus Resources: Django Project Starter

# {{ Ida Eriksson }} - She Codes News Project
## About This Project
The purpose of this project was to create a She Codes News site in Django. The starter code was provided and then it was up to the cohort to build on this code and create their own site. Inspiration was drawn from a standard newssite but the purpose was to use Django to make it dynamic and give it some personality and flair. 
## How To Run This Code
 1. Clone the repo to your local machine, the repo can be found here; SheCodesAus/plus-django-news-project-template. 
    2. Navigate to the folder where you want to start your project and run 'git clone' in your terminal.
    3. To ensure you always run your project on the same Django release set up your virtual environment
    4. install pip
    5. make yourself familiar with the folders and code
    6. upload your code to your repo as soon as you make any changes
    7. Have fun and try to not loose your shit 
    8. Don't forget that you have to make migrations as soon as you chnage something in your models 
## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )
## Project Features
- [x] A form for adding new stories
![ A form for adding new stories has been styled with new background colour, white text and the time the article is published has been added ]( project_img\A form for adding new stories.png. )

- [x] Users app: create account, login, logout
![Nav menu when logged out shows that there are links to creating an account as well as logging in for a new user or for a user that is not logged in. It tells the user that they have to log in/ create an account to post a story ] ( ./ 
project_img\Nav Menu when logged out.png.  )

- [x]!Nav menu when logged in displays the username, the log out option, 'my profile' and the option to post an article. ( ./project_img/Nav%20Menu%20when%20logged%20in.png )

- [x]!Create account view shows the standard Django view and this is where the link 'create account' takes the user ( ./project_img/Creat%20Account%20View.png )

- [x] Order stories by date
![ Image shows how the newest story is in storycard-1 and older stories are filtered based on date and time they were published ]( project_img\Order stories by date.png )

- [x] Styled "new story" form
![ See 'A form for adding new stories' point above ]( project_img\A form for adding new stories.png. )

- [x] Add a field to the NewsStory model for an image url and use this image url rather than the default images provided in the starter
![ {{ When creating a story this form has had 'add image URL' added to it }} ]( {{ project_img\A form for adding new stories.png }} )

- [x] View stories by a particular author
![ In view stories by a particular author it is possible to see all the stories published by the same author. You access this view by clicking the authors name ]( project_img\View stories by author.png )

- [x] Account view so authors can see their profile information
![ This is access by the 'my profile' line in the nav bar. The user can see their profile infromation including user name, last login and member since. ]( project_img\Account View.png )

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button
only visible when a user *is* logged in
![ In the nav bar different options are visible depending on if the user is logged in or logged out. It also says 'please log in to write a story' if you are not logged in, this changes once the user is logged in ]( C:\Users\Owner\she_codes\she_codes_news\project_img\Nav Menu when logged in.png, project_img\Nav Menu when logged out.png )


## Additional Features:
- [x] Add the ability to update and delete stories (consider permissions - who
should be allowed to update or and/or delete stories). - Django's UpdateView and DeleteView classes
![When an author is logged in they can edit or delete their own stories, this option is not available of not logged in or the user is not the author ]( project_img\Edit delete story when logged in.png )

- [x] Gracefully handle the error where someone tries to create a new story when
they are not logged in.
![ The page says 'please log in to write a story', if the user clicks that link it will take them to the log in page where they also have the option to create an account ]( project_img\log in link from create story.png, project_img\Log in to write a story.png,)

