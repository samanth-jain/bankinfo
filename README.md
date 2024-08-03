# Bank-Info

## This web service project is deployed successfully on Railway.app: 
## https://bankinfo-production.up.railway.app/home/

## Time taken to develop and deploy: 4-5 hours

## Method used to build the project:
* Used Django REST Framework to create APIs
* Created a management command to load CSV data into the database.
* Create the serializer to convert model instances to JSON
* Implement a views to handle POST requests and retrieve:
  + all banks list details
  + details by branch name
  + details by bank name
* Created URL endpoints for the views
* Tested the endpoint by sending a POST request with the branch name or bank name in JSON format.

## To run project locally

* Create virtual environment and activate
* Clone the project
* ```cd bankinfo```
* Run ```pip install -r requirements.txt```
* Change ```ALLOWED_HOSTS = ['bankinfo-production.up.railway.app']``` to ```ALLOWED_HOSTS = []``` in settings.py file
* Finally run ```python manage.py runserver```

## Navigating in localhost

* Navigate to ```http://127.0.0.1:8000/home/```

  ![image](https://github.com/user-attachments/assets/b90dd860-3731-43cd-8c19-a276d7addcd9)

* API endpoint for all bank lists, by branch name, and bank name is provided along with JSON post format
* Sample POST request:

  http://127.0.0.1:8000/bank/get
  ```
  {
  "bank_name" : "ABU DHABI COMMERCIAL BANK"
  }
  ```
  ![image](https://github.com/user-attachments/assets/ea483cf0-7bda-4017-878b-53ba36575391)

  http://127.0.0.1:8000/branch/get
  ```
  {
  "branch_name" : "DOMBIVLI"
  }
  ```

  ![image](https://github.com/user-attachments/assets/07358f34-04f3-4f52-a34d-583483179acc)


  

