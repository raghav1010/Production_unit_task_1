This is a RestApi coding task for credit card churning database to fetch results according the different queries.
Tech Stack used - Flask (python) , SQLite (database) , SQLAlchemy (ORM)


Feautures :
    
    1. Clean and understandable approach to design the solution following Rest principles . Packages and classes are separately created and used as and when required.
    2. SQLAlchemy for better and easy query fetching
    3. Flask Admin Dashboard (http://127.0.0.1:5000/admin on local server) 
    4. Error checks for invalid query fields or no records fetched
    5. Additional README documentation is contained in each solution folder for better understanding for future reference.
    6. Python script to design an approach to import given CSV data into the newly created database.
    7. Pagination on results in applied
    8. API testing document done with the help of Postman . The link has been provided. 
    9. The application has been deployed using Heroku
    
 Improvements :
  1. Creating a docker container for the application


postman_lin - contains the link to view my api testing result documentation for various endpoints.
Please go to the link which gives a html snippet , import that to your postman workplace and check the results of the different query based api calls on which i have tested my rest api

Some sample api links with queries:
 1. https://credit-card-churn-restapi.herokuapp.com/customers?Customer_Age=28&Card_Category=Blue&Gender=M 
 2. https://credit-card-churn-restapi.herokuapp.com/customers?Education_Level=High%20School 
 3. https://credit-card-churn-restapi.herokuapp.com/customers?Education_Level=High%20School&Marital_Status=Married 
 
 Important Note :
 Please enter the query fields (eg. Customer_Age , Education_Level , Marital_Status) as mentioned in the original csv data file , query fields like "age", "education" , "marital" are invalid and errors are handled carefully in the api service . 
