# Flavored Fitness 

Welcome to Flavored Fitness, A site where you can find a number of programs and exercise with them!
There is also a list with recipes because 90% of abs are made in the kitchen!
You can stay in touch with other users and people in the forum where you can either
make your own topic or respond to ones others have made!

I made this site because me and my girlfriend love to do fitness but with corona going on we 
dont have anyone to talk to about it but that changes with this website! Now you can chat
and talk about your most favorite equipment, programs, recipes and much more!


## UX 

This project is made for people that love fitness but have none to talk to about it

### Authentication
* As a user, I want to be able to register my own account easily
* As a user, I want to be able to make my own account and log in and log out
* As a user, I want to be able to be able to request my password and be send an email
* As a user, I want to be able to be remembered so I can log in more easily
* As a registered user, I want to have a list of my previous orders and my payment information saved

### Ordering
* As a customer, I want to be able to view a list of products and pick which id like to buy
* As a customer, I want to have an easy overview of the items I have added to purchase
* As a customer, I want to be able to remove and edit things inside of my shopping bag
* As a customer, I want to be able to sort the products in the store to my liking
* As a customer, I want to be able to search the store for something I might want to purchase

### recipes
* As a user, I want to be able to view a list of recipes I can user
* As a user, I want to be able to view the details of a recipe and look at the ingredients and steps
* As an admin, I want to be able to easil: Create, Update and Delete recipes

### Forum
* As a user, I want to be able to interact with other users in an online Forum


## Features

### Existing Features
* Authentication - Allows users to log in, out, sign up, request lost password and get an email notification
* Store - Allows users to purchase items, view items in details, look at the shopping bag and go to the checkout forum
* Checkout - Allows users to easily check out their order by having their purchase information saved
* Profile - Allows users to add their payment information to their profile and look at their previous orders
* Recipes - Allows users to view a list of recipes and look at the details of each by clicking on them
* Programs - Allows fitness enthousiasts to look at more different programs for them to user
* Forum - Allows users to chat with one another on the website and share ideas and tips

### Features Left to Implement

#### These are some features I would like to have done but did not have the time or knowledge for
* Add a working subscription method that would allow users to view the programs
* Adding Featured Programs to the home page to entice users to subscibe to the site
* Make the programs only be visible to Subscribers of the site


## Technologies Used

These are some of the technologies that I have used and implemented in my project
* Html
* Css
* JavaScript
* Python

* Django
* JQuery for simplified DOM manipulation
* AWS for static file control
* Postgres for databases


## Testing

### Authentication
1. Users are able to successfully create accounts
    * Email must have the correct template
    * Confirmation email must match the previous email
    * correct Password Template used
    * password confirmation must match previous password
    * Password can not be too similar to the email address
2. Useres can log  in and out as they please with no issues
    * If wrong login credentials are used, the correct error is displayed
3. Users can request their passwords in case they forgot
    * Requesting password form works
4. Users get send authentication emails to verify their emails

### orders
1. Customers are able to have an easy overview of all the products and can sort them as they want
    * The overview can not be broken in any way
2. Customers can add things to their shopping bad and remove and update products from their bags
3. Customers are able to browse the store for their name or descriptions.
    * the views display the correct details for the right products

### Recipes and Programs
1. Users are able to correctly view the lists of recipes and programs
2. Users can view the details of targeted programs and recipes
3. Admins can easily create new recipes and programs, update them and delete them

### Forum 
1. Users can create their own topics in the forum
2. Users are able to post a message to topics made by others
3. Users can view the different topics

The project minimizes itself on smaller browsers but keeps its functionality.

There had been a problem with the collapsible navbar not working as intended and upon
adding the new bootstrap version it was made to work but adding the new version made the
main nav bar not clickable causing me to have to add both bootstrap versions to my project


## Deployment

I am hosting my project on Heroku.
* Heroku and gitpod first were using different databases but now are both using Postgres
* Heroku and Gitpod use the same config variables to make the system work

My static files are saved and moderated through AWS
You can run my code by using the command "python3 manage.py runserver" in the terminal


## Credits

### Content
I have gotten the coding for the Pybb forum from "https://github.com/hovel/pybbm"
Since I am unable to make a forum myself I decided to use their code and functionality and slightly
modify it to make it fit my needs better

### Media
The images on this site were taken from google and their respective links.