# Arctic Shores Python/Web Programming Exercise

## Future Updates

This exercise is not complete, and the immediate tasks which would need to be worked on next are:
- Completing the 'get-candidate' endpoint.
- Incorporating unit tests.

Further tasks to improve the usability of this api include:
- Add a landing page for '/' and 'api/' endpoints
- Update the regex validator on candidate_ref to only accept alphanumeric inputs

## Installation

- clone this guthub repo
- move to the root project folder:
  ```bash
  cd arcticshores_test/
  ```
- initialise the python virtual environment:
  ```bash
  python3 -m venv env
  ```
  ```bash
  source env/bin/activate
  ```
- install dependencies:
  ```bash
  pip install django djangorestframework
  ```
    note: this project was created using the following versions:
    - Django: 4.0.1
    - Django Rest Framework: 3.13.1
    - Built using Ubuntu 20.04.3 LTS
- initialise the database:
  ```bash
  python manage.py makemigrations
  ```
  ```bash
  python manage.py migrate
  ```
- run server to start interacting with the API
  ```bash
  python manage.py runserver
  ```

## Available Endpoints
Once the above steps are completed, the following endpoints will be available to create candidates annd scores.

During development, the web browser and Insomnia were both used to input data.

http://127.0.0.1:8000/create-candidate/

http://127.0.0.1:8000/create-score/







