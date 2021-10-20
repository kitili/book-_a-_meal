{MOURINE KITILI,PATRICK KIMANTHI}

{BOOK A MEAL}, {2021}

## Description
{Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customers want to eat. }

## Technologies Used
{DJANGO,HTML,CSS,JAVASCRIPT}
* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface

## Features

As a user of the application you will be able to:
1. Users can create an account and log in 
2. Admin (Caterer) should be able to manage (i.e: add, modify and delete) meal options in the application. Examples of meal options are: Beef with rice, Beef with fries etc 
3. Admin (Caterer) should be able to set up a menu for a specific day by selecting from the meal options available on the system. 
4. Authenticated users (customers) should be able to see the menu for a specific day and select an option out of the menu. 
5. Authenticated users (customers) should be able to change their meal choice. 
6. Admin (Caterer) should be able to see the orders made by the user 
7. Admin should be able to see amount of money made by end of day .


### Installation and setup instructions

1. Clone this repo: git clone https://github.com/kitili/book-_a-_meal.git
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database bookameal using the command below.


       CREATE DATABASE bookameal;
5. Migrate the database using the command below


       python3 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python3 manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## LIVE LINK
  bookameal.herokuapp.com/



## Support and Contact Details:

{For enquiries feel free to contact us : 
email - Contact us at mourinekitilimourine@gmail.com or patrick.kimanthi@student.moringaschool.com
or Tel:+2457 12544598 or +254 723768573}


Copyright (c) {2021}

Licence
MIT License Copyright (c) [2021] [bookameal] Permission is hereby granted, free of charge, to any person obtaining a copy of this website and associated documentation files (the "book a meal"), to deal in the Website without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Website, and to permit persons to whom the Website is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Website. THE WEBSITE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE WEBSITE OR THE USE OR OTHER DEALINGS IN THE WEBSITE.
