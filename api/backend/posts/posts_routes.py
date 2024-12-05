from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# Blueprint object for all posts routes
posts = Blueprint('posts', __name__)


#------------------------------------------------------------
# Get all posts in the system from a certain group
@posts.route('/posts/<pgroup>', methods=['GET'])
def get_post_by_group(pgroup):
    current_app.logger.info('GET /posts/<pgroup> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Posts WHERE PGroup = %s', (pgroup,))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Enter a new post into the system
@posts.route('/posts', methods=['POST'])
def add_new_post():
    the_data = request.json
    current_app.logger.info(the_data)
    
    query = '''
            INSERT INTO Posts (
                PostTitle,
                PostContent,
                PostType,
                PGroup
            ) VALUES (%s, %s, %s, %s)
        '''
        
    params = (
        the_data['post_title'],   
        the_data['post_content'], 
        the_data['post_type'],    
        the_data['group']         
    )

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    db.get_db().commit()
    cursor.close()
    
    return make_response({"message": "Successfully added post"}, 200)


#------------------------------------------------------------
# Delete a specific post from the system based on the given PostId
@posts.route('/posts/p<postID>', methods=['DELETE'])
def del_post(postID):
    cursor = db.get_db().cursor()    
    query = 'DELETE FROM Posts WHERE PostId = %s'
    cursor.execute(query, (postID))
        
    db.get_db().commit()
    cursor.close()
        
    return make_response({"message": f"Successfully deleted post {postID}"}, 200)
