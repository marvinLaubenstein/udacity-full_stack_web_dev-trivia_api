import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the DONEs
    """    

    CORS(app, resources={'/': {'origins': '*'}})

    """
    @DONE: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    """
    @DONE:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():
        categories = db.session.query(Category).order_by(Category.id).all()

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'categories': {category.id: category.type for category in categories},
            'success': True,
        })

    """
    @DONE:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def get_questions():
        questions = Question.query.all()
        total_questions = len(questions)
        current_questions = paginate_questions(request, questions)
        categories = Category.query.all()
        categories_dict = {category.id: category.type for category in categories}

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'categories': categories_dict,
            'questions': current_questions,
            'success': True,
            'total_questions': total_questions,
        })


    """
    @DONE:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:question_id>', methods=['GET', 'DELETE'])
    def delete_question(question_id):
    # Function body remains the same
        try:
            question = Question.query.get(question_id)

            if question is None:
                abort(404)
            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id
            })
        except:
            abort(422)

    """
    @DONE:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def create_question():
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')
        category = data.get('category')
        difficulty = data.get('difficulty')

        if not all([question, answer, category, difficulty]):
            abort(422)

        new_question = Question(
            question=question,
            answer=answer,
            category=category,
            difficulty=difficulty
        )
        new_question.insert()

        all_questions = Question.query.all()
        current_questions = paginate_questions(request, all_questions)

        return jsonify({
            'success': True,
            'created': new_question.id,
            'questions': current_questions,
            'total_questions': len(all_questions)
        })

    """
    @DONE:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        data = request.get_json()
        search_term = data.get('searchTerm', None)

        searched_questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

        if not searched_questions:
            abort(404)

        output = paginate_questions(request, searched_questions)

        return jsonify({
            'success': True,
            'questions': output,
            'total_questions': len(searched_questions)
        })



    """
    @DONE:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_question_by_category(category_id):
        category = Category.query.get(category_id)
        if category is None:
            abort(404)

        try:
            questions = Question.query.filter_by(category=category.id).all()
            current_questions = paginate_questions(request, questions)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'current_category': category.type,
                'total_questions': len(questions)
            })
        except:
            abort(500)

    """
    @DONE:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def get_quiz():
        try:
            data = request.get_json()
            quiz_category = data.get('quiz_category')
            previous_questions = data.get('previous_questions')
            quiz_category_id = quiz_category['id']

            if quiz_category_id == 0:
                questions = Question.query.filter(
                    Question.id.notin_(previous_questions),
                    Question.category == quiz_category_id
                ).all()
            else:
                questions = Question.query.filter(
                    Question.id.notin_(previous_questions),
                    Question.category == quiz_category_id
                ).all()
            
            question = random.choice(questions) if questions else None

            return jsonify({
                'success': True,
                'question': question.format()
            })
        except:
            abort(422)

    """
    @DONE:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        response = {
            "success": False,
            "error": 404,
            "message": "resource not found"
        }
        return jsonify(response), 404

    @app.errorhandler(422)
    def unprocessable_error_handler(error):
        response = {
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }
        return jsonify(response), 422
    @app.errorhandler(500)
    def unprocessable_error_handler(error):
        response = {
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }
        return jsonify(response), 500

    
    


    return app