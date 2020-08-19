# Practical Python and Data-Centric Development Milestone Project
***

## Table of Contents:
* [Project Summery ](#project-summery)
* [Functionality of Project](#functionality-of-project)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Template](#3-template)
        * [4. Geometry](#4-geometry)
        * [5. Wireframing](#5-wireframing)
        * [5. UX](#5-ux)
* [Technology Used](#technology-used)
* [Features](#features)
    * [Future Features](#future-features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

***

## Welcome to Recipify 

## Project Summary
Recipify - Recipe sharing app. The purpose is to build a full-stack site that allows users to manage a common dataset about a particular domain that allows users to create, locate, read, update and delete (CRUD) recipes. Recipify gives access to all the recipes in the database to all users. All users can add new recipes as well as edit, locate, and delete other recipes.


The project can be viewed <a href="https://recipify-food-app.herokuapp.com/">here</a>


### Functionality of Project
This application contains the key CRUD requirement functionality and utilises a data handling document based database, MongoDB. The user functionality is created using Flask, HTML templates and CSS. One of the most prominent frontend frameworks was used in building the frontend interface structure, Bootstrap, and includes all the main attributable points of a modern day website/application such as a Navigation bar and Footer elements.

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables are held in a git ignored file and held _secret_ to ensure the project integrity is held to present day and project requirement standards.

[Back to top](#table-of-contents)

## User Experience:

#### User Stories:
_Generic (Guest/Public) User:_
* As a Generic User, I want to view all recipes.
* As a Generic User, I want to add recipes.
* As a Generic User, I want to edit recipes.
* As a Generic User, I want to delete recipes.
* As a Generic User, I want to search recipes.
* As a Generic User, I want to navigate the app easily.

#### Design

##### 1. Font
The project has a main font <a href="https://fonts.google.com/specimen/Roboto">Roboto</a> which greatly complement each other throughout the site.
  
“Sans-Serif” is used as the default backup font in cases where these fonts have difficulty loading.
Maven Pro sports a unique curvature allowing it the ability to stand out and be distinguishable when in context. It is used throughout the site as the main font for headers, unique stand-out pieces of information and button text etc, drawing the user’s attention to these main focus points and calls to actions.

The secondary font used is Roboto. With its natural widths per character, and increased effectiveness for reading rhythm, it was the perfect choice using this font for the lengthier text elements. Used on all major paragraphs, it offers a pleasing reading ability to the user and is easy on the eyes. This font is a staple used in many websites and applications today worldwide and is reminiscent of how an application should look, clean, professional and very readable amongst all major languages.

##### 2. Color Scheme
This project went through multiple theme iterations whilst in Wireframe stage. Ultimately, I was always lead back to professional high contrast finish that would normally be seen in most day-to-day apps with a touch of pastel color to highlight to the user the breakaway elements.

* ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff` - Primary color
* ![#03a9f4](https://placehold.it/15/03a9f4/000000?text=+) `#03a9f4` - Secondary color
* ![#ff9800](https://placehold.it/15/ff9800/000000?text=+) `#ff9800` - Tertiary color

The background colour and the heading in font in the navbar and call to action buttons used the primary colour, ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) , setting the immediate tone for the rest of the application to be professional and aesthetically pleasing. All fonts used throughout the application utilise this primary color as-well.

The navbar is colored in our Secondary color choice, ![#03a9f4](https://placehold.it/15/03a9f4/000000?text=+) , which offered the first splash of vibrant color to contrast the logo and the nav-link elements.

The call to action buttons utilised , ![#ff9800](https://placehold.it/15/ff9800/000000?text=+) , when not active, focused or hovered. 

The tertiary color, ![#ff9800](https://placehold.it/15/ff9800/000000?text=+) , was also used on the icons and H1 headings.

##### 3 Template
The app was created uasing the <a href="https://materializecss.com/getting-started.html">Materialize starter template</a> to reduce setup up time

##### 4. Geometry

The application is primarily rectangular shaped with subtle rounded edges around elements such as cards, forms and interactive buttons. On desktop the recipes are displayed in grids of three. On mobile the recipes are displayed in a single column.
An example of this would be the Home page:
* The Latest Recipes heading is vertically into thirds, each card contains a featured image, a title, preperation time snipet,  servings and a Call To Action.
* Search recipies takes on a simular grid structure. 
* There is a search bar built into the header that produces results on the Search Resipes page.
* The Add Resipes page is a simple responsive form.

##### 5. Wireframing

Wireframing for this project were created using AdobeXD. Each page or view of the application was rendered as a wireframe in both Mobile and Desktop viewports to show the difference between the aesthetics and showing how the elements per page would react to differing viewport sizes. 

Initial Wireframes for the site: <a href="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/tree/master/wireframes">Wireframes</a> 

***

* Home Page:

The Home (Index) Page contained all the major navigation points for the user. It does not contain a hero image to maintain a clean and simple theme not destracting fromt the main focus of the app. A simple heading and subheading defining nature of the application as well as a choice of call to action buttons. 
Below the Latest Recipes are desplayed. 

<details>
<summary>Home Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Mobile%20home%20page.png" alt="Home page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Desktop%20homepage.png" alt="Home page tablet-desktop wireframe">
</p>
</details>

***

* Login Page:

STILL IN PRODUCTION
A simple page as normal inheriting the navbar and footer from the base.html file.

<details>
<summary>Login Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/mobile%20login%20page.png" alt="Login page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Desktop%20login%20page.png" alt="Login page tablet-desktop wireframe">
</p>
</details>

***

* Create Recipe Page:


<details>
<summary>Create Recipe Wireframes</summary>

<p align="center">
    <img height="350" src="" alt="Create Recipe page mobile wireframe">
</p>

<p align="center">
<img height="350" src=" " alt="Create Recipe page tablet-desktop wireframe">
</p>
</details>

***

* Search Recipe Page:


<details>
<summary>Search Recipe Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Desktop%20search%20recipe%20page.png" alt="Create Recipe page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Desktop%20search%20recipe%20page.png" alt="Create Recipe page tablet-desktop wireframe">
</p>
</details>

***

* Recipe Page:


<details>
<summary>Recipe Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/mobile%20recipe%20page.png" alt="Create Recipe page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/TobinWebDesign/Milestone-Project-Data-Centric-Development-Milestone-Project-/blob/master/wireframes/Desktop%20recipe%20page.png" alt="Create Recipe page tablet-desktop wireframe">
</p>
</details>

***

##### 6. UX

My main goal in UX was to build a responsive website that is simple to use. The users can create their own recipes, view all the recipes created on the database, edit and delete all recipes. The target audience for this app is anyone who has passion for cooking, wants to discover new recipes or needs to store their own recipes online.
Creating a modern and user-friendly interface with easy access to all information is the key to giving users a feeling of reliability and positiveness. I developed this app in a way that everyone can view and edit all the recipes on the website. The next phase of the project would be to only authors make changes to their recipes.
The structure of the website is well-organised and easy navigation.

[Back to Top](#table-of-contents)

## Technology Used

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS & Python ~ core languages used to create this multi-page CRUD application.
* <a href="https://materializecss.com/"> Materalize</a> ~ Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* <a href="https://git-scm.com/">Git</a> ~ Installed on local device and integrated to PyCharm as a Plugin to enable version controlling.
* <a href="https://github.com/tobinwebdesign/">Github</a> ~ Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.
* <a href="https://www.heroku.com/">Heroku</a> ~ A cloud platform as a service enabling deployment for this CRUD application.

## Technologies Used
### <a href="https://github.com/">GitHub</a>

* Used as remote storage of my code online.
* <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* for installation of necessary tools.

## Front-End Technologies
### <a href="https://jquery.com/">JQuery</a>
* The project uses JQuery to simplify DOM manipulation.
### <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">Javascript</a>
* I used JavaScript from the Google Maps API website and for the reset button
### <a href="https://en.wikipedia.org/wiki/HTML5">HTML5</a>
* HTML5 was used for the semantic structure and presenting the content of the webpage.
### <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3">CSS3</a>
* CSS3 was used for the styling of the content to produce an aesthetically pleasing viewing experience.
### <a href="https://materializecss.com/">Materialize</a>
* Used as the design framework.
## Back-End Technologies

### <a href="https://www.python.org/">Python</a>
* back-end programming language used in this project.
### <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>
* microframework for building and rendering pages.
### <a href="https://www.mongodb.com/">MongoDB Atlas</a>
* NoSQL database for storing back-end data.
### <a href="https://api.mongodb.com/python/current/">PyMongo</a>
* for Python to get access the MongoDB database.
### <a href="https://werkzeug.palletsprojects.com/en/0.16.x/">Werkzeug</a>
* to generate and verify password hashing.
### <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>
* templating language for Python, to display back-end data in HTML.
### <a href="https://heroku.com/">Heroku</a>
* to host the project.

## Libraries

### <a href="https://fontawesome.com/">Font Awesome</a>
* Font Awesome was used for the social links, mainly the social media icons for a professional finish.
### <a href="https://fonts.google.com/">Google Fonts</a>
* I used Google Fonts for the font families.

##  Features

### Existing Features

* If user wants to search recipes for a particular it can be done by putting in a keyword that is in a Recipe Title into the search box
Add a Recipe ([CRUD] Create or 'add' a new recipe)
* All users can add recipes.User name will automatically populate in the add recipe form as Recipe Author.For selective fields,user can select the options from drop down.All the fields of the form is well explained with the 'placeholder' to make it user friendly.
Viewing Recipes ([CRUD] Read or 'review' recipes)
* On the recipes page, all recipes are displayed. If user wants to see a particular recipe,the recipe will open in a full screen where all the details of the recipe can be found.
Update a Recipe ([CRUD] Update recipes)
* Users can update or 'edit' recipes on Edit page.
* Delete a Recipe ([CRUD] Delete recipes)
* Users can delete or 'remove' recipes. Delete option will only be visible for a user on their own recipe pages.

### Features Left to Implement
* Register User allowing anybody can register for free.
* Log in and log out features
* Delete option that will only be visible for a user on their own recipe pages.
* Edit option that will only be visible for a user on their own recipe pages.
* Search Button,more filters to make recipes more easily accessible.
* Page view counter for recipe pages
* Like buttons on recipes
* Social share buttons
* Comments section

## Testing

Testing was performed in 3 different ways.
- Browser Testing
- User testing
- Manual Testing

### Browser Testing
While my main choice of browser for development is google chrome, I regularly checked the performance on the Microsoft Edge and Safari browsers. Making use of browser resizing and dev tools device toolbars on each browser to test responsiveness and how the grid, fonts and media queries were performing and the consistency between each. Adjusting to find a happy medium for all three.
After I had test deployed the site to heroku I was able to see the real life versions which I was able to test on android and iphone phone.
Known Issue
* Mobile nav animation

### Manual Testing

View | Add | Edit | Delete | Search
#### All recipes and single recipe display

#### Add New Recipe

* I added plenty of test recipes to check the functionality throughout the development. If I leave some of the required fields empty, I will not be able to submit the form. 

#### Edit Recipe

* Edit recipe button is visible on the recipe page. Once clicked it opens a page with a form that allows the user to edit the recipe. 
#### Delete Recipe

* Delete button is visible on the recipe page.  Once clicked it deletes the recipe from the database
#### Search Recipe

* The search box is visible on all pages and allows users search keywords in the recipe title. 

### Issues discovered while testing and how they were rectified.
* This site was tested across multiple browsers (Chrome, Microsorft Edge, FireFox) and on multiple mobile devices (iPhone 4, 5, 7, 8, X, iPad, iPad Pro, Galaxy S5, Pixel 2, and Pixel 2XL) to ensure compatibility and responsiveness.  
* For testing the responsive aspect of the website I used a Google Chrome Developer Tools
* Side nav - the mobile side nav was not functioning correctly. This was rectifies by using URL_for as the source
* Search box - there was a bug where I had incorrect defination resulting in the search_recipes page not displaying. I also had issues with searching for keyword in the recipe name. This was rectified with help from the toutors and my mentor. 
### Known Issues
* The search box works effectively for words found in the recipe titles it is upper and lowercase sensitive sometimes resulting in no resipies being found. 


### Validators

HTML -
<a href="https://validator.w3.org/nu/#textarea">W3C HTML Validator</a>
CSS -
<a href="https://jigsaw.w3.org/css-validator/">W3C CSS Validation Service, Jigsaw</a>
JavaScript -
<a href="https://jshint.com/">JSHint</a>
Python
<a href="http://pep8online.com/">PEP8 Online</a>


This website is currently viewable with no deployment issues in:
* Google Chrome
* Microsorft Edge
* Safari


## Deployment

This multi-page application was developed in Gitpod and version controlling was utilised via local (git) and online (github) repository technologies. 

In order to deploy my project to Heroku I have completed the following steps, you can view it <a href="https://recipify-food-app.herokuapp.com/">here</a>.

Deploying this application was achieved by:
* Created a Procfile with the command echo web: python run.py > Procfile.
* Created a requirement.txt file so Heroku know what python modules it will need to run my application with the command pip freeze > requirements.txt
* Created a new branch to test deployment to heroku changing MONGO_URI from local to mongo atlas, changed app.run() to set debug to False.
* Created a new project on heroku and in the deploy section linked my github repository with heroku in order to deploy straight from the source.
* Configured any environment variables in Heroku App Settings > Config Vars such as my Secret Key, IP PORT and MONGO_URI.
* Finalised all code, and made sure that it was production ready and ensured that my .gitignore was not uploading any secret keys.
* Deployed the application from heroku admin page using linked repository and master branch.
* The application is now fully deployed to Heroku

To clone the repository:
* Select the Repository from the Github Dashboard.
* Click on the "Clone or download" green button located above and to the right of the File Structure table.
* Click on the "clipboard icon" to the right of the Git URL to copy the web URL of the Clone.
* Open yourthe Gitpod (IDE) and navigate to the terminal window.
* Change the directory to where you want to clone the repository too.
* Paste the Git URL copied from above and click "Ok".

[Back to Top](#table-of-contents)

### Deployment to Heroku



## Credits

* I got the recipes and images from <a href="https://www.bbc.co.uk/food/recipes">BBC FOOD</a> 
* I got the website template from <a href="https://materializecss.com/getting-started.html">Materalize</a> 
* I got the python code from the Code institute lectures

</ul>


## Acknowledgements

My thanks to my mentor Anthony Ngene also helped me out with python issues and the tutoring team at the Code Institute. The tutor team support has been excellent.  