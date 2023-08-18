# API Development and Documentation Final Project (Udacity)

#### This project is my variant of the API Development and Documentation final project created for Udacity's Full Stack Web Developer course. This application is intended to show a small basic quiz. The frontend was provided by Udacity and is therefore a bit unfinished. The main part of my code can be found under the 'DONE' comments. 

## Installation

How to start the application:

- Install all required project dependencies
```sh
npm i
```
- Start the Development Server
```sh
npm start
```

### Load the Backend 

How to start the backend related processes

- Install all required backend dependencies
```sh
pip install -r requirements.txt
```

- Start the Server
```sh
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Application Overview 

## Dashboard List (/)
All quiz questions at a glance

![Screenshot 2023-08-18 at 11 23 44](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/d58a066d-f49d-492b-9e9e-e6c8bea16332)

## Create Question Page (/add)
Create a new question for the quiz

![Screenshot 2023-08-18 at 11 24 06](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/14c2cc7f-c7b0-456d-b9ab-9651357fdc5b)

## Start the Quiz Page (/play)
Choose a quiz category 

![Screenshot 2023-08-18 at 11 24 19](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/80c12208-bf9e-464a-969c-62bc1fd908d3)

Start answering the quiz questions...

![Screenshot 2023-08-18 at 11 24 49](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/c1b63d1e-f60d-4509-bede-3920cd7bced9)

... and continue

![Screenshot 2023-08-18 at 11 24 58](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/d3d073f8-ff7e-4fd8-9e79-b83aaf088d74)

## Database Structure 
## Questions Table

![Screenshot 2023-08-18 at 11 46 36](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/0e93eaac-5272-475b-8394-735caddf9852)

## Categories Table

![Screenshot 2023-08-18 at 11 46 13](https://github.com/marvinLaubenstein/udacity-full_stack_web_dev-trivia_api/assets/82942834/55c2d889-419b-4a45-89bd-b1c955f1be83)

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.
