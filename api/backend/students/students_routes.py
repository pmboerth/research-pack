from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

students = Blueprint('students', __name__)


#------------------------------------------------------------
# Get all students from the system
@students.route('/students', methods=['GET'])
def get_all_students():
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT *
                   FROM Students
    ''')
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all students with the particular DepartmentID
@students.route('/students/d<departmentID>', methods=['GET'])
def get_students_by_department(departmentID):
    current_app.logger.info('GET /students/d<departmentID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Students WHERE DepartmentId = {0}'.format(departmentID))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Add a new student to the system
@students.route('/students', methods=['POST'])
def add_new_student():
    the_data = request.json()
    current_app.logger.info(the_data)
    
    query = '''
            INSERT INTO Students (
                FirstName,
                LastName,
                Email,
                SkillId,
                DepartmentId,
                ResearchInterest,
                Year,
                Major,
                StudentType
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        
    params = (
        the_data['first_name'],
        the_data['last_name'],
        the_data['email'],
        the_data['skill_id'],
        the_data['department_id'],
        the_data['research_interest'],
        the_data['year'],
        the_data['major'],
        the_data['student_type']
    )

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    db.get_db().commit()
    cursor.close()
    
    return make_response({"message": "Successfully added student"}, 200)

#------------------------------------------------------------
# Update a specific student based on their StudentId
@students.route('/students/s<studentID>', methods=['PUT'])
def update_student(studentID):
    
    the_data = request.get_json()
    
    valid_fields = {
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'email': 'Email',
            'skill_id': 'SkillId',
            'department_id': 'DepartmentId',
            'research_interest': 'ResearchInterest',
            'year': 'Year',
            'major': 'Major',
            'student_type': 'StudentType'
        }

    # build the set dynamically based on which fields were provided
    update_fields = []
    params = []
        
    for json_key, db_column in valid_fields.items():
        if json_key in the_data:
            update_fields.append(f"{db_column} = %s")
            params.append(the_data[json_key])

    if not update_fields:
        return make_response({"error": "No valid fields to update"}, 400)

    query = f'''
        UPDATE Students 
        SET {', '.join(update_fields)}
        WHERE StudentId = %s
    '''
        
    params.append(studentID)

    cursor = db.get_db().cursor()
    cursor.execute(query, params)            
    db.get_db().commit()
    cursor.close()

    return make_response({"message": f"Successfully updated student {studentID}"}, 200)

#------------------------------------------------------------
# Delete a specific student from the system
@students.route('/students/s<studentID>', methods=['DELETE'])
def del_student(studentID):
    cursor = db.get_db().cursor()    
    query = 'DELETE FROM Students WHERE StudentId = %s'
    cursor.execute(query, (studentID))
        
    db.get_db().commit()
    cursor.close()
        
    return make_response({"message": f"Successfully deleted student {studentID}"}, 200)
    

