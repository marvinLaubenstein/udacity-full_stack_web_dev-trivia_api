import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from settings import DB_NAME, DB_USER, DB_PASSWORD

database_name = DB_NAME
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432', database_name)


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    '''
    # test QUESTION related OPERATIONS
    ''' 
    def test_get_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['success'])
        self.assertTrue(data['total_questions'])

    def test_delete_question(self):
        response = self.client().delete('questions/7')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 7)

    def test_question_create(self):
        new_dummy_question = {
            "question":"Can I pass this courses?", 
            "answer":"Yes, of course", 
            "category":"2", 
            "difficulty":"6"
        }
        response = self.client().post('/questions', json=new_dummy_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['created'])


    def test_search_questions(self):
        response = self.client().post('/questions/search', json={"searchTerm": "What"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_404_questions_get_invalid_pages(self):
        response = self.client().get('/questions?page=10000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], "resource not found")
    
    def test_422_questions_delete_invalid_question(self):
        response = self.client().delete('/questions/10000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test_404_search_questions_invalid_question(self):
        res = self.client().post('/questions/search', json={"search": "1TGH9"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')
    

    '''
    # test CATEGORY related OPERATIONS
    ''' 

    def test_get_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertTrue(data['success'])
        

    def test_get_question_by_category(self):
        response = self.client().get('/categories/2/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_404_get_question_by_invalid_category(self):
        res = self.client().get('/categories/500/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found') 


    '''
    # test QUIZ related OPERATIONS
    ''' 
    def test_get_quiz(self):
        quiz_data = {
            'previous_questions': [5, 9],
            'quiz_category': {
                'id': 4,
                'type': 'History'
            }
        }

        response = self.client().post('/quizzes', json=quiz_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], 4)

    def test_get_quiz_invalid_quiz_data(self):
        quiz_data = {'previous_questions': []}
        response = self.client().post('/quizzes', json=quiz_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

if __name__ == "__main__":
    unittest.main()