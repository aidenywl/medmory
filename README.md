# Medmory

Project for HackTeck 2019 @ California Institute of Technology. A SMS system to help patients manage chronic medications via a SMS and cellular call reminder system.

The devpost for this project can be found [here](https://devpost.com/software/sms-05bcei).

## Architecture

- Django for backend server and SQLite database management.
- React for frontend webpages serving doctors and pharmacists.
- Twilio APIs for patient-facing services.

## How to set-up and run the project

Requirements:

- Python 3 and Django for backend
- NodeJS and React installed
- Yarn for node package management.
- Redis to be able to run `redis-server` for SMS and Reminder scheduling and brokering.
- Ensure that the Huey python library is installed for patient medication reminder scheduling.
- **Set-up your Twilio api credentials in a python file called `credentials.py` in project root.`**

### For development

0. Install `virtualenv` and start a virtual environment for managing your python dependencies by running `virtualenv` and starting it up by `source env/bin/activate`.
1. **Install Dependencies**
1. Head to the React source code in `frontend` and install all dependencies with `yarn`.
1. In the root folder, run `pip install -r requirements.txt` to install django dependencies.
1. Run `yarn start` to start the development server on `localhost:3000`.
1. After redis-cli is installed, run `redis-server` on the server.
1. Run ./manage.py run_huey in the root folder to enable task scheduling.
1. In the same root directory, run `python manage.py runserver 0.0.0.0:8000` to start the Django server to begin talking to Twilio APIs and serve the react frontend.
1. Head over to `localhost:3000` to start using the application.

### For production

0. Install `virtualenv` and start a virtual environment for managing your python dependencies by running `virtualenv` and starting it up by `source env/bin/activate`.
1. **Install Dependencies**
1. Head to the React source code in `frontend` and install all dependencies with `yarn`.
1. In the root folder, run `pip install -r requirements.txt` to install django dependencies.
1. Run `yarn build` to build the static files, CSS, HTML, and Javascript code from the react files.
1. After redis-cli is installed, run `redis-server` on the server.
1. Run ./manage.py run_huey in the root folder to enable task scheduling.
1. In the same root directory, run `python manage.py runserver 0.0.0.0:8000` to start the Django server to begin talking to Twilio APIs and serve the react frontend.
1. Head over to `localhost:8000` to start using the application.

## Team Members

This weekend project was made possible and fun with the amazing people below.

- [Aiden Low Yew Woei](https://github.com/fionaroni)
- [Brian Cheung](https://github.com/bcheung)
- [Fiona Tang](https://github.com/fionaroni)
- [David Chen](https://github.com/CDavid99)
