# Plus Resources: Django Project Starter

# {{ Ida Eriksson }} - She Codes News Project
## About This Project
{{ The purpose of this project was to create a She Codes News site in Django. The starter code was provided and then it was up to the cohort to build on this code and create their own site. Inspiration was drawn from a standard newssite but the purpose was to use Django to make it dynamic and give it some personality and flair.  }}
## How To Run This Code
{{
Give a quick step-by-step guide on how to download and run your codebase.
It's ok to assume the reader is another developer here, so don't feel like you
have to explain what a virtual environment is, etc.
Give directions like "clone the repo to your local machine", "create a virtual
environment", "migrate the database", etc.
When you need to specify terminal commands, you can surround them with
backticks, like so: `python manage.py runserver`. This formats them as
code in the markdown document. (The backtick key is to the left of the
number 1 at the top of your keyboard.)
}}
## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )
## Project Features
- [x] A form for adding new stories
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Users app: create account, login, logout
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Order stories by date
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Styled "new story" form
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add a field to the NewsStory model for an image url and use this image url rather than the default images provided in the starter
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Story images
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Account view so authors can see their profile information
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Log-in/log-out
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Account view" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Create Account" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] View stories by author
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button
only visible when a user *is* logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Create Story" functionality only available when user is logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories by
category.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to update and delete stories (consider permissions - who
should be allowed to update or and/or delete stories). - Django's UpdateView and DeleteView classes
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to “favourite” stories and see a page with your favourite
stories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Our form for creating stories requires you to add the publication date,
update this to automatically save the publication date as the day the
story was first published (maybe you could then add a field to show
when the story was updated).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
[ ] Gracefully handle the error where someone tries to create a new story when
they are not logged in.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

<!-- Ida's notes
1. I have added a message when the user is not logged in it says 'Please log in to write a story' and this sentence is also a link to the log in page -->