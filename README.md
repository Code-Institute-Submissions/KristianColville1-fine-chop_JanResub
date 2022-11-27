# Fine Chop

Developer: Kristian Colville

[Visit this website]()

![Responsive Image]()

<br>

## Table of Contents

* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owners Goals](#site-owners-goals)
* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Typography](#typography)
    * [Structure](#structure)
        * [Wireframes](#wireframes)
* [Business Model](#business-model)
    * [Goals](#goals)
    * [Target Audience](#target-audience)
    * [Strategy](#strategy)
* [Web Marketing](#web-marketing)
* [Agile Methodology](#agile-methodology)
    * [Epics](#epics)
* [Information Architecture](#information-architecture)
    * [Database](#database)
    * [Data Modeling](#data-modeling)
* [Features](#features)
* [Testing](#testing)
* [Bugs](#bugs)
* [Technologies & Tools](#technologies--tools)
* [Development & Deployment](#development--deployment)
    * [Version Control](#version-control)
    * [Cloning this Repository](#cloning-this-repository)
    * [Heroku](#heroku)
    * [AWS](#aws)
    * [Stripe](#stripe)
* [Credits](#credits)
* [Acknowledgments](#acknowledgments)

## Project Goals

The project's main goal was to develop an Asian-style restaurant/takeaway eCommerce website that takes advantage of UI/UX design concepts, offers users services to meet their demands, is fully operational, and has a distinct business model.

Another goal for the project was to show a love for Asian cuisine and develop a website that gives a big shout-out to businesses that cater in Ireland.

### User Goals

* Quick login options
* Create an account on FineChop and personalize a profile
* Add meals to a basket for purchase
* Order food for delivery or for dining in
* Quickly order a meal and have multiple options
* Keep up to date with offers and deals
* Have the ability to provide feedback or reviews
* Ability to repeat orders
* Buy vouchers or gifts
* Book tables and seating for groups

### Site Owners Goals

* Create an Asian-style eCommerce restaurant website that has the look and presentation of an experienced brand
* Allow users to use CRUD functionality where ever possible to keep people engaged in a meaningful and interactive way
* Provide users with the ability to purchase meals for delivery or for in house dining
* Provide clear navigation for users to easily follow and get to their final destination
* Build a responsive and accessible website for a wide audience
* Build the website with the Asian culture in mind that shows admiration and respect
* Effectively use digital marketing for email & social media
* Show users a clear well defined business and keep simplicity wherever possible
* Provide staff of the restaurant methods of improved productivity for the eCommerce web app
* Build a website that provides ways of improved data analytics to help with the business goals

[Back to Top](#table-of-contents)

## User Experience
### Target Audience

* Any user that is interested in Asian cuisine
* Users who would like to order a delivery meal
* Users interested in booking tables for a dine in experience
* Users familiar with the Asian culture and the types of services offered in the restaurant industry
* People who enjoy the services provided by an experienced brand
* Users that would like to share their experiences and leave feedback/reviews
* Users with an interest in purchasing delicious food

### User Requirements and Expectations

* Simplicity throughout the website for clear navigation with the goal of completing an order
* Information is structured in an organized and easy-to-follow manner
* The CRUD functionality works as expected with feedback provided for each appropriate response
* The simplicity is perfectly implemented with no unnecessary complexity diminishing the user experience
* The design should look authentic & respectful with a care to avoid making an artificial imitation of an Asian-style restaurant
* The website needs to address a wide audience and so should provide ease of accessibility for visually impaired users
* This eCommerce site needs to be built with a mobile first design and a good level of responsive design
* The content should be minimal and avoid long keyword phrases for mobile users
* The website should take multiple user interactions into account
* Bring engagement from digital marketing and provide systems and accounts to build the brand
* Show users a consistent design across all channels of engagement
* Calls to action should be built and implemented with care
* Any and all personal information is securely stored and protected
* The website should be built with genuine love for the food and not bring about a plastic experience
* Provide multiple options for engagement and successfully implement methods strategies for the business model
* The business model and intentions of the website are clear to the user
* When building for eCommerce a huge amount of UI/UX design has been thoughtfully implemented for common practices
* The user can predict actions and outcomes successfully because of the UI/UX design
* Avoid distracting colors and patterns, decorate with simplicity and provide appealing imagery
* As eCommerce relies heavily on users purchasing products and services it is important that the SEO is perfectly implemented
* Effectively build with user roles in mind and abstract issues for designing the website

### User Stories

User roles:

    User
    Customer,
    Staff Member,
    eCommerce Business Owner,
    Marketer,
    Developer

#### User (New & Returning site user)

| Issue ID | User Story |
|---|---|
|[#1](https://github.com/KristianColville1/fine-chop/issues/1)|As a New User I can create an account so that I can store my personal information and not have to reenter details for each visit|
|[#2](https://github.com/KristianColville1/fine-chop/issues/2)|As a New User I can quickly create an account to store personal information so that I can speed up the process and navigate through the website faster|
|[#3](https://github.com/KristianColville1/fine-chop/issues/3)|As a Returning User I can sign into the website so that I don't have to reenter personal information again for each visit|
|[#4](https://github.com/KristianColville1/fine-chop/issues/4)|As a Returning User I can I have the option to quickly sign in so that I can avoid having to reenter personal information at each visit and navigate the website faster|
|[#5](https://github.com/KristianColville1/fine-chop/issues/5)|As a New User I can easily navigate around the web app so that I can find whatever content I am interested in|
|[#6](https://github.com/KristianColville1/fine-chop/issues/6)|As a New User, I can intuitively & easily understand the purpose of the web app, so that I have perceived expectations/actions I can perform on the web app|
|[#7](https://github.com/KristianColville1/fine-chop/issues/7)|As a New user, I can receive an email to confirm that my account has been registered successfully, so that I know my new account is activated and have confirmation of username selected|
|||
|||
|||

<br>

#### Customer (Shopper & Consumer)

| Issue ID | User Story |
|---|---|
|[#14](https://github.com/KristianColville1/fine-chop/issues/14)|As a shopper, I can view menu items, so that select some to purchase|
|[#15](https://github.com/KristianColville1/fine-chop/issues/15)|As a Shopper, I can view individual food items from the menu and view their details, so that check the description, the rating, the image, the size and the price|
|[#16](https://github.com/KristianColville1/fine-chop/issues/16)|As a shopper, I can find special offers and deals, so that take advantage of the offer and save money on food I would like to purchase|
|[#17](https://github.com/KristianColville1/fine-chop/issues/17)|As a shopper, I can easily view my trolley total at any time, so that avoid spending too much and keep within my preferred budget|
|[#18](https://github.com/KristianColville1/fine-chop/issues/18)|As a shopper, I can sort through the list of menu items, so that easily find the highest rated & best priced food items to purchase|
|[#19](https://github.com/KristianColville1/fine-chop/issues/19)|As a shopper, I can sort through the menu to find a specific category of food items, so that find what i'm looking for or search for the best-priced or best-rated food item in that category or find the product by name|
|[#20](https://github.com/KristianColville1/fine-chop/issues/20)|As a shopper, I can sort multiple categories of food items simultaneously, so that find the best-priced or best-products across broad categories, such as "Thai Noodles" or "Rice Noodles"|
|[#21](https://github.com/KristianColville1/fine-chop/issues/21)|As a Shopper, I can search for a food item by name or description, so that I can find a specific food item I would like to purchase|
|[#22](https://github.com/KristianColville1/fine-chop/issues/22)|As a shopper, I can easily see what I have searched for and the results of my search, so that I can quickly locate the food item or check the food item availability|
|[#23](https://github.com/KristianColville1/fine-chop/issues/23)|As a Shopper, I can easily identify that I have selected the correct food item and the right size meal, so that I ensure I don't accidentally select the wrong food item or meal size|
|[#27](https://github.com/KristianColville1/fine-chop/issues/27)|As a consumer, I can have a personalised user profile, so that view my order history, confirmations and save my payment information|
|[#31](https://github.com/KristianColville1/fine-chop/issues/31)|As a Consumer, I can Leave a review on a food item, so that I can express my dissatisfaction/ satisfaction with something I have purchased|
|[#37](https://github.com/KristianColville1/fine-chop/issues/37)|As a consumer, I can identify with relative ease what the new food menu items are, so that I can try new meals and have more options to choose from|
|[#39](https://github.com/KristianColville1/fine-chop/issues/39)|As a consumer, I can book a table to dine in, so that I can have the option to visit FineChop if I am interested in a dine-in experience|
|[#40](https://github.com/KristianColville1/fine-chop/issues/40)|As a shopper, I can have the option to purchase a gift card, so that I can give someone a gift or use as an alternate method of transaction|
|[#51](https://github.com/KristianColville1/fine-chop/issues/51)|As a shopper, I can update the quantity of individual menu items in the cart, so that make changes to my purchase and the food I will receive|
|[#52](https://github.com/KristianColville1/fine-chop/issues/52)|As a Customer, I can enter my payment information, so that so I can checkout quickly and with no hassle|
|[#53](https://github.com/KristianColville1/fine-chop/issues/53)|As a Customer, I can feel that my personal and payment information is safe and secure, so that I can confidently provide the needed information to make a purchase on this website|
|[#54](https://github.com/KristianColville1/fine-chop/issues/54)|As a Customer, I can view an order confirmation after I checkout, so that I can verify that I have made a purchase and check if I haven't made any mistakes|
|[#55](https://github.com/KristianColville1/fine-chop/issues/55)|As a Consumer, I can receive an email confirmation after checking out, so that so I have a record of the transaction and a confirmation of what I have purchased|

<br>

#### Staff Member

| Issue ID | User Story |
|---|---|
|[#26](https://github.com/KristianColville1/fine-chop/issues/26)|As a staff member, I can update food item images, so that our food items always have the best representation online|
|[#33](https://github.com/KristianColville1/fine-chop/issues/33)|As a staff member, I can reply to reviews and help dissatisfied customers, so that I can provide a higher level of customer service for the business|
|[#38](https://github.com/KristianColville1/fine-chop/issues/38)|As a staff member, I can post new job roles on the website and collect resumes, so that I can fill roles that are vacant and choose from a custom talent pool of applicants|
|||

<br>

#### eCommerce Business Owner (site owner)

| Issue ID | User Story |
|---|---|
|[#24](https://github.com/KristianColville1/fine-chop/issues/24)|As a eCommerce Business Owner, I can quickly add or remove products from food menu's, so that I can keep the menu up to date with correct meals purchased when people dine-in|
|[#25](https://github.com/KristianColville1/fine-chop/issues/25)|As a eCommerce Business Owner, I can manipulate prices of items on the menu, so that I can compete with the wider market of restaurant owners, manage expenditure and predict future sales|
|[#32](https://github.com/KristianColville1/fine-chop/issues/32)|As a eCommerce Business Owner, I can have a method of authentication for reviewing food items, so that I can protect my business from malice and help improve my business based off of genuine reviews|
|[#36](https://github.com/KristianColville1/fine-chop/issues/36)|As a eCommerce Business Owner, I can have a feature in my website that helps new food Items to stand out, so that customers are aware of new meals and can help me test new and exciting food menu options|

<br>

#### Marketer

| Issue ID | User Story |
|---|---|
|[#28](https://github.com/KristianColville1/fine-chop/issues/28)|As a marketer, I have the ability to easily create & manipulate content for the website, so that help keep people engaged and drive sales for the business|
|[#29](https://github.com/KristianColville1/fine-chop/issues/29)|As a Marketer, I have the ability to target an audience of FineChop and send them emails about the latest offers, promotions and specials available, so that I can perform my function and help drive business to website to increase sales|
|[#30](https://github.com/KristianColville1/fine-chop/issues/30)|As a Marketer, I can access a special menu so I can perform tasks like email & content marketing, so that I can perform my function easily and quickly on the site to help increase user engagement and drive sales|
|[#34](https://github.com/KristianColville1/fine-chop/issues/34)|As a marketer, I can be notified of reviews on products, so that I can identify food item satisfaction and come up with strategies to improve the user experience|
|[#35](https://github.com/KristianColville1/fine-chop/issues/35)|As a marketer, I can keep track of marketing campaigns, so that I can identify the best times of year to promote products and services for the website, measure performance and improve user engagement|

<br>

#### Developer

| Issue ID | User Story |
|---|---|
|[#41](https://github.com/KristianColville1/fine-chop/issues/41)|As a Developer, I can implement a 404 error page to alert users that they have accessed a page that does not exist, so that good design principles are practised and the user can navigate back to the home page|
|[#42](https://github.com/KristianColville1/fine-chop/issues/42)|As a Developer, I can implement a 500 error page to alert users that a server error has occurred, so that good design principles are implemented and the user can navigate back to the home page|
|||
|||

<br>
[Back to Top](#table-of-contents)

## Design
### Color Scheme
### Typography
### Structure
#### Wireframes

[Back to Top](#table-of-contents)

## Business Model

The business model for FineChop is B2C, the target audience for selling products and services is for customers only. The sole focus is on individual transactions and catering for the individual. The business model aims at providing individuals with an excellent option for a takeaway/dine-in experience.

### Goals

- Provide excellent customer satisfaction
- Provide a UI/UX design for the website that helps customers perform actions
- Create a lively atmosphere for people and show excellent all round service
- Bring flavour to life and showcase delicious meals
- Bring the website to life and make it as inviting as possible
- Provide staff with improved productivity methods to increase sales and performance
- Improve wait times
- Market the business effectively across all channels

### Target Audience

The **FineChop** web app is aimed at targeting a wide audience and being well rounded for all demographics to achieve their goals. Everyone has a favorite go to meal they might get in an Asian-style restaurant. The restaurant aims at providing everyone with the best possible service. The age criteria that we aim to provide services to would be at least 18 and older. Customers of **FineChop** need a good user experience so providing them with the ability to find products and services they are looking for is essential. **FineChop** aim to offer the best service available in the food industry and strive to make wait times low & food perfect whether thats in house or takeaway. 

### Strategy Trade-Off

The restaurant business is highly competitive and the strategy trade-off for **FineChop** is to design and build an application capable of improving performance so it needs to be as user friendly as possible.

* Consistent design
* Simple navigation
* Intuitive interface
* Ease of accessibility
* Full access for ordering without account
* Quick and simple purchase
* Optimized for mobile users
* Simple pricing system
* Excellent SEO
* Improved productivity for essential staff members

[Back to Top](#table-of-contents)

## Web Marketing

[Back to Top](#table-of-contents)

## Agile Methodology
This project was developed using agile methodologies through small-medium sized feature incremental sprints. Their were 3 major sprints spaced out for the project.

A Kanban board was created using github projects and can be found at [my github project FineChop](https://github.com/users/KristianColville1/projects/3). All stories were categorized into three main stages for development and testing. User stories were prioritized using the Moscow method and updated accordingly to higher or lower levels if improvements or further considerations were met.

Moscow Method in order of prioritization:

- Must Have
- Should Have
- Could Have
- Wont Have

Sprints:

- Sprint 1
- Sprint 2
- Sprint 3

### Epics

#### 1 Base Project Setup

Setting up the project and having the basics put together for incremental development. The next step after initial designing and wire-framing.

#### 2 User Authentication

Providing the ability to login or sign up through various methods such as social media with Google, Facebook, Instagram & Twitter.
Designing the Allauth templates and building everything for an intuitive UI.

#### 3 Reservations Application

Successfully implementing the ability to reserve tables at FineChop Restaurant and additional features like purchasing gift cards.

#### 4 Subscriptions

A precursor for the marketing milestone. Successfully acquiring email addresses and providing the ability for email marketing.
Additional smaller features like offers and gift cards.


#### 5 Home Application

Providing a nice UI and providing additional routes for ordering and more information.

#### 6 Menu Application

An application that handles the menu items for creation.

#### 7 Marketing

Provide staff of multiple kinds with the ability to do their tasks for content and email marketing.

#### 8 Deployment

Completing a minimal viable product with as many user stories completed for the website and successfully sending it out into the world.

#### Documentation

Tasks such as the README file

[Back to Top](#table-of-contents)

## Information Architecture
### Database

For the first migrations and testing during the development phases, SQLite was the main database. The main database was switched over to Postgres on Heroku when the project was deployed

### Data Modeling

An entity relationship diagram was made using [Trevor.io](https://trevor.io/) to model the connections between the various backend data structures

With the help of this tool, we can visualize the relationships between the data structures in a way that is both aesthetically beautiful and beneficial for comprehending the overall relationship between the data structures.

Through Heroku's add-ons, the technology was utilized to offer a rapid method of access.

We can quickly locate practically any relationship with the help of this information architecture. This is advantageous to use and work with from the perspective of a coder.

![Entity Relationship Diagram]()

#### Allergen Model

Allergen model for food items served at FineChop

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Name| **name** |CharField|max_length=100|
|Friendly_Name|**friendly_name**|**MessageManager**|max_length=100, null=True, blank=True|

#### Category Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Name| **name** |CharField|max_length=254|
|Friendly_Name|**friendly_name**|CharField|max_length=254, null=True, blank=True|


#### FoodItem Model

Abstract Model
Abstract class created for the MenuItem Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Name| **name** |CharField|max_length=250, unique=True|
|Description|**description**|TextField| none |
|Image|**image**|ImageField|null=True, blank=True|
|Image URL|**image_url**|URLField|max_length=1024, null=True, blank=True|

#### FoodItemProductDetails Model

Abstract Model
Abstract class created for the MenuItem Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Product_Code| **product_code** |CharField|max_length=255, null=True, blank=True|
|Price|**price**|CharField|max_digits=6, decimal_places=2|

#### MenuItem Model

Mixin Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Category| **category** |ForeignKey|Category,null=True, blank=True,on_delete=models.SET_NULL|
|Allergens|**allergens**|ManyToManyField|Allergen, blank=True|
|Status|**status**|IntegerField|choices=STATUS_CHOICES, default=1|
|Portion Sizes|**portion_sizes**|BooleanField|default=False, null=True, blank=True|
|Rating|**rating**|DecimalField|max_digits=6,decimal_places=2,null=True,blank=True|

#### Order Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Order Number|**order_number**|CharField|max_length=32, null=False, editable=False|
|Full Name|**full_name**|CharField|max_length=50, null=False, blank=False|
|Email|**email**|EmailField|max_length=254, null=False, blank=False|
|Phone Number|**phone_number**|CharField|max_length=20, null=False, blank=False|
|Country|**country**|CharField|max_length=40, null=False, blank=False|
|PostCode|**post_code**|CharField|max_length=20, null=True, blank=True|
|Town or City|**town_or_city**|CharField|max_length=40, null=False, blank=False|
|Street Address 1|**street_address_1**|CharField|max_length=80, null=False, blank=False|
|Street Address 2|**street_address_2**|CharField|max_length=80, null=False, blank=False|
|County|**county**|CharField|max_length=80, null=False, blank=False|
|Date|**date**|DateTimeField|auto_now_add=True|
|Delivery Cost|**delivery_cost**|DecimalField|max_digits=6,decimal_places=2,null=False,default=0|
|Can Deliver|**can_deliver**|BooleanField|default=False, null=False, blank=False|
|Order Total|**order_total**|DecimalField|max_digits=10,decimal_places=2,null=False,default=0|
|Grand Total|**grand_total**|DecimalField|max_digits=10,decimal_places=2,null=False,default=0|
|Original Cart|**original_cart**|TextField|null=False, blank=False, default=''|
|Stripe PID|**stripe_pid**|CharField|max_length=254,null=False,blank=False,default=''|

#### OrderLineItem Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Order|**order**|ForeignKey|Order,null=False,blank=False,on_delete=models.CASCADE,related_name='lineitems'|
|Menu Item|**menu_item**|ForeignKey|MenuItem,null=False,blank=False,on_delete=models.CASCADE|
|Portion Size|**portion_size**|CharField|max_length=2, null=True,blank=True|
|Quantity|**quantity**|IntegerField|null=False, blank=False, default=0|
|Line Item Total|**lineitem_total**|DecimalField|max_digits=6,decimal_places=2,null=False,blank=False,editable=False|

#### Table Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Table Number|**table_number**|IntegerField|choices=TABLE_NUMBER, default=1|
|Seating Amount|**seating_amount**|IntegerField|default=2|
|Disabled Friendly|**disabled_friendly**|BooleanField|default=True|

#### Booking Model

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|Order Number|**order_number**|CharField|max_length=32, null=False, editable=False|
|Customer|**customer**|ForeignKey|User,on_delete=models.CASCADE,related_name="booking_customer"|
|Booked Table|**booked_table**|ForeignKey|Table, on_delete=models.CASCADE,related_name="booking_table"|
|Guest Amount|**guest_amount**|IntegerField|default=2|
|Date|**date**|DateField| none |
|Time|**time**|IntegerField|choices=BOOKING_TIMES, default=1|

[Back to Top](#table-of-contents)
## Features

All the features documentation can be found [here](/FEATURES.md)

[Back to Top](#table-of-contents)

## Testing
All the Testing documentation can be found [here](/TESTING.md)

[Back to Top](#table-of-contents)

## Bugs

| Issue ID | Expected Behaviour | Behaviour reported | Bug Fix |
|---|---|---|---|
|[#8](https://github.com/KristianColville1/fine-chop/issues/8)|When the dropdown menu is clicked it slides a menu downwards to display the menu for the user|Dropdown menu slides up and down but the page also scrolls up to the top. Bad user experience| Added preventDefault to jquery event for sliding dropdown menu's and reevaluated using a general purpose event, fixed issue and created general purpose click event for dropdown menu's|
|[#9](https://github.com/KristianColville1/fine-chop/issues/9)|DjLint was expected to help conform to code standards and best practices|It works locally but when deploying on Heroku the extended pip packages are effecting the deployment running successfully| Even after uninstalling djlint the dependencies it brought with it still affected the project. I deleted the virtual environment and created a new one with my requirements.txt before I installed djlint|
|[#10](https://github.com/KristianColville1/fine-chop/issues/10)|Click on a drop down menu in the navigation and it slides down that menu|Click on a drop down menu in the navigation and it scrolls the page up to the start. This bug interferes with the visual design when viewing allauth forms| A temporary fix included making sure the navigation is always viewable on pages with allauth forms by always adding the background. After investigating further it was because I hadn't included any link path to resources|
|[#11](https://github.com/KristianColville1/fine-chop/issues/11)|Expected Imperavi to import it's widget properly so a nice text editor could be used for creating html newsletters|Fails to import the widget|Removed apps for the newsletter, imperavi and widget |
|[#12](https://github.com/KristianColville1/fine-chop/issues/10)|Widget to display itself for creating general newsletter|Type Error at /admin/newsletter/message/add/ because too many positional arguments given in admin| Removed apps for the newsletter, imperavi and widget |
|[#13](https://github.com/KristianColville1/fine-chop/issues/13)|Home page should load when deployed|Getting internal 500 server error| Reset virtual environment and removed unused imports before deploying project again and this fixed the issue |
|[#48](https://github.com/KristianColville1/fine-chop/issues/48)|static files to load properly|Not loading static files|Fixed any links by removing / from urls and added static root url and this seemed to fix the problem. I identified it as a static file issue from looking at the heroku logs for the deployment |
|[#49](https://github.com/KristianColville1/fine-chop/issues/49)|Images to slide over the next image with ease| I added a min height for the body element in css and manipulated the z axis of my project contents to display on top of the darker overlay behind for the home page |
|[#50](https://github.com/KristianColville1/fine-chop/issues/50)|Expected Heroku to automatically store static and media files on AWS S3 Bucket|Prevents storage to S3 bucket|Removed whitenoise and django heroku from the extensions and reloaded my requirements.txt file and this fixed the static files loading on heroku|
[Back to Top](#table-of-contents)

## Technologies & Tools

[Back to Top](#table-of-contents)
## Development & Deployment
### Version Control

I used [Visual Studio Code](https://code.visualstudio.com/) as a local repository and IDE & [GitHub](https://github.com/) as a remote repository.

1. Firstly, I needed to create a new repository on Github [fine-chop](https://github.com/KristianColville1/fine-chop).
2. I opened that repository on my local machine by copying the URL from that repository and cloning it from my IDE for use.
3. Visual Studio Code opened a new workspace for me.
4. I created files and folders to use.
5. To push my newly created files to GitHub I used the terminal by pressing Ctrl + shift + `.
6. A new terminal opened and then I used the below steps.

    - git add (name of the file) *This selects the file for the commit*
    - git commit -m "Commit message: (i.e. Initial commit)" *Allows the developer to assign a specific concise statement to the commit*
    - git push *The final command sends the code to GitHub*

### Cloning this Repository

If you would like to clone this repository please follow the bellow steps.

Instructions:

1. Log into GitHub
2. Navigate to the repository you want to clone
3. Click on the green button labelled 'Code'
4. Copy the URL under the HTTPS option
5. Open an IDE of your choosing that has Git installed
6. Open a new terminal window in your IDE
7. Type this exactly: git clone the-URL-you-copied-from-GitHub
8. Hit Enter

You should have a local copy of the repository to use on your machine.

If you encounter problems after cloning this project please make sure you have also installed the requirements to run this project

- Create a virtual environment by running the command in the terminal:
    - **python3 -m venv .venv**

- Activate your virtual environment by running the command:
    - **source .venv/bin/activate**

- Run the command to install these requirements:
    - **pip3 install -r requirements.txt**

Please see this [page](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) for a comprehensive walk-through and explanation of how to use Git and GitHub if you are unsure how to do so or if you encounter any more problems.

### Heroku

I selected [Heroku](https://dashboard.heroku.com) as a deployment option. As of the time of writing, it provides customers with a free tier, allowing them to quickly publish apps if they are just starting as developers

To deploy a project using Heroku follow these steps:

- Log into heroku

![Heroku Login](documentation/readme_folder/heroku-login.png)

- Go to the heroku dashboard

![Heroku Dashboard](documentation/readme_folder/heroku-dashboard.png)

- Create a new app by selecting 'New'

![Heroku New App](documentation/readme_folder/heroku-newapp.png)

- Give your application a name and select a preferred location
    - The EU region was chosen for this application as the developer is located in this region

![Heroku Create App](documentation/readme_folder/heroku-createapp.png)

- Click the 'Create app' button

- If you have config variables in your application
    - Click on settings
    - Click 'Reveal config vars'
    - Input your deployment variables

![Heroku Settings](documentation/readme_folder/heroku-settings.png)

- If you need specific build packs
    - Click on settings
    - Click on build pack
    - Add your packs as needed (Please be aware that the order matters)
    - No specific build packs were selected for this project as Django used.

![Heroku Buildpacks](documentation/readme_folder/heroku-buildpacks.png)

- Once these steps are completed
    - Go to the deploy section
    - Select your version control system
    - For Daily Sync, GitHub was selected

![Heroku Deploy](documentation/readme_folder/heroku-deploy.png)

- Connect your version control system
- Add your repository
- Connect the app selecting 'connect'
- Either choose automatic deployment or manual deployment
- Once all these steps are completed and the build is successful
    - You can click the 'view' button
    - It will reveal your deployed app

### AWS

For this project I chose to use an AWS S3 bucket to store my static files. If you would like to also do the same please follow my instructions to create an S3 bucket. I wouldn't consider AWS console to be the most user friendly tool so follow my instructions carefully.

1. Sign into [AWS console](https://aws.amazon.com/console/)

![AWS console](documentation/readme_folder/sign-into-aws-console.png)

2. If you don't have an AWS account create one and add your credit card details

Be mindful of charges on your account. Use free tier products and don't go overboard. You can check your account in the top right corner of the screen by clicking on the username you chose when creating an account. There you will see multiple options to check your account and billing information

3. Once you have successfully logged in navigate to the top left corner of the page where the AWS logo and services are located

![AWS console](documentation/readme_folder/aws-logo-and-services.png)

4. You'll see a search bar. Type in S3 and select the one called S3 from the list of options

![AWS console](documentation/readme_folder/select-s3-bucket.png)

5. You'll be brought to the main dashboard for AWS S3 and you can create a bucket here. The button to create a bucket is located on the right hand side of the screen

![AWS console](documentation/readme_folder/create-s3-bucket.png)

6. Click the button and enter the information as I have below and change the name of the bucket to your preferred chosen bucket name (usually made identifiable by your project name). Choose your preferred location also. To access the bucket publicly you need to allow access

![AWS console](documentation/readme_folder/create-bucket-1.png)
![AWS console](documentation/readme_folder/create-bucket-2.png)
![AWS console](documentation/readme_folder/create-bucket-3.png)

7. On this page those are the only settings that need configuration so click 'create bucket' at the end of the page

![AWS console](documentation/readme_folder/create-bucket.png)

8. You'll be brought to your AWS S3 buckets page. Click on the bucket you just created

![AWS console](documentation/readme_folder/buckets.png)

9. Navigate to the properties tab of your bucket and find you should find static hosting in the list (at the time of writing it is at the bottom of the page) so click edit

![AWS console](documentation/readme_folder/bucket-properties.png)
![AWS console](documentation/readme_folder/static-web-hosting.png)

10. Enable static hosting and add in index.html and error.html (these don't matter but need config for this project) and click save changes at the bottom of the screen

![AWS console](documentation/readme_folder/edit-static-hosting.png)

11. You'll be brought back to the bucket dashboard for your bucket the next thing to do is to configure permissions. We have three tasks to do in the permissions tab

![AWS console](documentation/readme_folder/bucket-permissions.png)

12. We need to add a bucket policy so click edit here and then lets use the policy generator

![AWS console](documentation/readme_folder/edit-policy.png)
![AWS console](documentation/readme_folder/policy-generator.png)

13. You'll be brought to a new tab to create your policy.

- The type of policy is S3 Bucket policy
- The principal is a * symbol so we can access everything in our bucket
- We only need to perform one action and its 'GetObject'
- The ARN can be found on the previous tab at the top of the page
- Click add statement
- Then click Generate Policy
- We have no special conditions to add for this project

![AWS console](documentation/readme_folder/policy-1.png)
![AWS console](documentation/readme_folder/policy-2.png)

- Copy the policy generated using Ctrl + a and Ctrl + c or using your mouse
![AWS console](documentation/readme_folder/policy-3.png)

14. Switch tabs back to your edit bucket policy page and paste the generated policy into the text editor area. We want to use all the resources in the bucket so we're not finished yet here.
In the policy you can see a key for "Resource" and at the end of the value add /* so we can access all items inside the bucket then click save changes at the bottom of the screen

![AWS console](documentation/readme_folder/policy-config.png)

15. The second task we need to complete here in the permissions tab of the bucket is configuring the Access control list. It allows users to access the bucket. Click edit

![AWS console](documentation/readme_folder/access-control-list.png)

- You only need to change one setting here for Everyone to have public access and you only want to change list

![AWS console](documentation/readme_folder/access-control-1.png)

- Accept that you understand these changes for granting access and click save changes

![AWS console](documentation/readme_folder/access-control-2.png)

16. The last step for the S3 bucket is to go to the very end of this tab section under permissions and add a CORS configuration. Click edit and paste the following code block

![AWS console](documentation/readme_folder/cors.png)

    [
        {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
        "GET"
        ],
        "AllowedOrigins": [
        "*"
        ],
        "ExposeHeaders": []
        }
    ]

17. We've finished everything we need to do inside our bucket the next thing we need to do is configure our identity and access management settings for accessing our AWS resources. In the search bar enter IAM and select the first option called IAM

![AWS console](documentation/readme_folder/iam.png)

18. Click on User groups and create a new user group

![AWS console](documentation/readme_folder/user-groups.png)

![AWS console](documentation/readme_folder/create-group.png)

![AWS console](documentation/readme_folder/create-group-1.png)

- You don't need to do anything yet so just click create group at the end of the page after you create a name for your user group

19. You'll be brought to the dashboard for your user groups, click on the user group you created
and navigate to permissions

![AWS console](documentation/readme_folder/group-permissions-1.png)

- Click on add permissions and click attach policies

![AWS console](documentation/readme_folder/group-permissions-2.png)

- You will be brought to another page to create your policy, navigate to the JSON tab

![AWS console](documentation/readme_folder/group-permissions-3.png)

- Click on import managed policy

![AWS console](documentation/readme_folder/group-permissions-4.png)

- Type in S3 and select the option for full access, when you return the JSON text will have changed

![AWS console](documentation/readme_folder/group-permissions-5.png)

- Remove the value for the Resource key and replace it with your ARN for your S3 Bucket. 
Open a separate tab and navigate to the S3 dashboard and then to your bucket and get the ARN like we did in a previous step. create an array for the Resource key and paste in your ARN twice but for the second value in the array put a /* at the end so we can access the bucket and the buckets contents.

![AWS console](documentation/readme_folder/group-permissions-6.png)

![AWS console](documentation/readme_folder/group-permissions-7.png)

- When completed click next and next again skipping the tag section as it's irrelevant for this project and add a name and description for the policy you created

![AWS console](documentation/readme_folder/group-permissions-8.png)

20. Navigate back to user groups and click on your group go to the permissions tab and lets attach the policy we created

![AWS console](documentation/readme_folder/group-permissions-9.png)

21. The last thing we need to do to complete our set up and access to our S3 bucket is to create a user for our user group so they can use the permissions we created

- Navigate to the the user sections of our IAM

![AWS console](documentation/readme_folder/user-permissions-1.png)

- Click on add user

![AWS console](documentation/readme_folder/user-permissions-2.png)

- Create a user for our user group and allow programmatic access so we can use it in our Django project, click next and skip the tag section and click on create user

![AWS console](documentation/readme_folder/user-permissions-3.png)

22. We have now completed our set up for our S3 bucket and we need to download the .csv file for our access key and secret access key. You can also copy those from here to put in your project

![AWS console](documentation/readme_folder/user-permissions-4.png)

23. As a final mention you must install boto3 and django-storages in order to use your S3 bucket.

- In your settings.py file of your project directory paste in this and also changing the bucket name and region that you chose for your S3 bucket

        # static file config heroku
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }

        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'fine-chop2'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

- You will also need to configure django to use your S3 bucket so create a file as below and place it in the main project directory

![AWS console](documentation/readme_folder/custom-storage.png)

[Back to Top](#table-of-contents)
### Stripe

[Back to Top](#table-of-contents)

## Credits

## Acknowledgments

[Back to Top](#table-of-contents)
