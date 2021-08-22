# Installation

## Installtion and starting server for backend
Install the requirement for the django restful api
```bash
cd backend
```
Install the requirement by using 
```bash
pip install -r requirements.txt
//or
pip3 install -r requirements.txt
```

Run the server
```bash
cd code

python manage.py runserver 
// or
python3 manage.py runserver 
```

If migration is needed for running the django server, use commend below:
```bash
python manage.py makemigrations
python manage.py migrate
// or
python3 manage.py makemigrations
python3 manage.py migrate
```

##Installation and starting server for frontend
```bash
cd frontend
yarn install
yarn start 
```