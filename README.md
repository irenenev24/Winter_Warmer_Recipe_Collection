# Winter Warmer Recipes

![Image showing the website displayed on different screen sizes](/static/images/responsive-image-readme.png)

This site is a website for winter themed recipes. 
It is designed to be a base for people to upload and view recipes. 
It has various different categories of recipes (eg: Breakfast, Lunch etc.)
The user has to ability to view the home page but to view the content
on the rest of the site the user must create an account.
After creating an account they will be automatically taken to their profile page.
Everyone with a profile can create/read/update/delete recipes,
while only someone with an admin login account
can create/read/update/delete categories.

## UX

## Who is this website for?

* This website is for people who are interested in easily finding
 inspiration for recipes during the winter months.
* This website will provide recipes across a range of categories 
 and can have more categories added by admin.
* This website is for people who may wish to create their own recipes and
 share with the community.
* It is aimed at people worldwide and of any age group.
* It is suitable for people who may wish to revisit as they will have an 
 account where they can view their recipes.

### Strategy

### What do visitors want?

* Clear information across the site with easy to use navigation.
* Recipes that are divided into different categories.
* A search bar that can be used to search by category, recipe name or keyword. 
* Ability to create/read/update/delete recipes.
* Ability to add recipes with a pre-designed form that helps keep information concise
and relevant.
* Ability to edit recipes on a pre-populated form that makes editing easy.
* A trustworthy site that is easy to use with a personal profile page and 
useful links found in the footer section for easy navigation.


### Business Goals:

* As a business owner I want to appeal to a wide variety of audiences. 
* Launching as a winter site but with potential to expand with summer, spring, autumn
 etc, as the year progresses.
* Build an interactive platform where users can add to the information and build a 
community for sharing.

### Admin Goals:

* Build a platform where users can create/read/update/delete recipes and 
as an admin I can create/read/update/deletecategories.
* I want user to create an account to access the site.
* Users can delete recipes but as a security measure I have included a JavaScript to 
prevent accidental deletion.
* I have also included this for the deletion of categories to prevent errors.
* I want to create a user friendly area that will become more useful overtime with 
the inclusion of more recipes and categories.
* I want a site that is responsive across all devices for ease of use.
* Some features are not available unless you have an admin password,
such as categories.

### Customer Goals:

#### First time customer

1. Is this site trusthworthy and easy to navigate?
1. Can I add to the infomation provided?
1. Can I look at recipes on this site?
1. Is the information provided relevant to my needs?
1. Is the purpose of this site clear?
1. Am I able to make a profile for my own recipes?
1. Is it easy to create an account?
1. Can I follow this site on social media for more updates?
1. Do I understand the aim of this site?
1. Can I use this site on all my devices?

#### Repeat customers

1. If I see a recipe I wish to use in the future 
am I able to access the site again to use it?
1. Can I add to this site?
1. Will I be able to use this on all my devices?
1. Is this site easy to navigate to save time?
(eg: navigation bar, search bar, categories)

### Scope

* How to add recipes?.
* What the site has to offer, differnet categories etc 
  - Dinner
  - Breakfast
  - Lunch etc.
* Responsive across all screens.
* Easy to use.
* Flash message to alert user to different message.
* JavaScript alerts to prevent accidental deletion.
* User can create/read/update/delete recipes.
* Admin can create/read/update/delete recipes and categories.  

## Future Features

* Adding extra sections for cooking tutorials.
* Adding sections for seasonal recipes like summer etc.
* Ability to add saved recipes to your profile. 
* Building on the different allergy requirements such
as gluten, dairy free, sugar free etc.
* Adding in christmas/easter sections and more.
* Adding a profile picture to the profile.

### Structure
1. Home page will be viewable to anyone regardless of log in status.
1. Create Account page will allow user to create a new account with validation required 
for username and password. Alert will show if either username or password is already in use.
Otherwise the user will be directed to a profile page and an alert will welcome the user.
Hi {{ user }}! Create account page also has a link to the login page for someone who 
may already have an account.
1. Login page will allow user to log into their account with validation required 
for username and password. Alert will show if either username or password is incorrect.
"Incorrect Username and/or Password"
Otherwise the user will be directed to a profile page and an alert will welcome the user.
Hi {{ user }}! Login page also has a link to the Create Account page for someone who 
may not already have an account.
1. The profile page will show Hi {{ user }}! Followed by a welcome statement.
There is also a button thats provides a quick link to add a recipe.
1. The Recipe page will show a search bar that is set to search by category, recipe name or keyword.
Below this all recipes will show with an image and brief dewscription. A button will feature for
each one with the words View Recipe.
1. The view button will connect to a page that shows each recipe individually. Using recipe.id to select them.
They will display on the page with the recipe name, category and created by sections highlighted 
at the top of the page. Below will feature an image, recipe ingredients and recipe description.
Below will be a two buttons. on for edit and one for delete. The delete button will trigger an 
alert from JavaScript to prevent accidental deletion.
1. The edit button will lead to a page that is pre-populated using the recipe.id
The user will have the option to edit and submit the recipe or cancel and return to the recipe page.
1. The Add recipe page will allow users to fill out a form to share their recipes with the other
users of the site. The info submitted on this form will be used to prepopulate the edit recipe form.
#### For admin use only
1. The category page will show a list of categories which will feature an edit and a delete button.
1. The edit button will lead to a page that lets the admin edit the category title.
1. The delete button will lead to a page that lets the admin delete the category title. 
The delete button will trigger an alert from JS to prevent accidental deletion.
1. The add category page will allow admin to add new categories.
#### Messages
All submit/login/delete buttons will trigger flash messages.

### Skeleton
#### Wireframes 
* Nav bar featuring links to various areas in the site taken from MaterializeCss.com
* Image carousel with a welcome paragraph about Winter Warmer Recipes and what the site aims to provide for users.

* Footer with social media links, legal info.

### Surface
#### Typography
* All fonts were taking from fone-awesome.
#### Colors
#### Media 
* All media used on home page from unsplash.com.
* Logo made for me on Fiverr.com
[static/images/Original Logo.png]
* All recipes and images submitted by the admin(myself) taken from BBC GoodFood.
[https://www.bbcgoodfood.com/]


## Features 


## Building of site

### Languages Used
- [HTML5] (https://en.wikipedia.org/wiki/HTML5)
- [CSS] (https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Frameworks
- [Google Fonts](https://fonts.google.com/)
    Google fonts were used to import the fonts used in this site. 
    Lobster and Noto-sans-display 
- [Font Awesome](https://fontawesome.com/)
    The icons used throughout the site have been taken from Font Awesome.
- [GitHub](https://github.com/)
    For storing project.
- [Gitpod](https://www.gitpod.io/)
    Used for editing my code.site code.
- [Balsamiq](https://balsamiq.com/)
    Used for Wireframe creation for my site.
- [Am I responsive](http://ami.responsivedesign.is/)
    This was used to generate the image at the top of this README.
- [jQuery](https://jquery.com/)
    Required for some of the elements used from Materialize.com
- [Heroku](https://dashboard.heroku.com/apps)
    For deployment of the application
- [MongoDB](https://www.mongodb.com/)
    Used to store data in the database.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    Framework we have used for building our applications.

### Testing

- Contained in a seperate file [TESTING.md]