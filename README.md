# Bank-Info

## This web project is deployed successfully on Railway.app: 
## https://bankinfo-production.up.railway.app/home/


## To run project locally

* Create virtual environment and activate
* cd bankinfo
* Run ```pip install -r requirements.txt```
* Change ```ALLOWED_HOSTS = ['bankinfo-production.up.railway.app']``` to ```ALLOWED_HOSTS = []``` in settings.py file
* Finally run ```python manage.py runserver```

## Navigating in localhost

* Navigate to ```http://127.0.0.1:8000/home/```

  ![image](https://github.com/user-attachments/assets/b90dd860-3731-43cd-8c19-a276d7addcd9)

* API endpoint for all bank lists, by branch name, and bank name is provided along with JSON format
* Sample JSON request:

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


  

