from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# Blueprint object for all departments routes
comments = Blueprint('comments', __name__)


#------------------------------------------------------------
# Post a comment to a particular post
@comments.route('/comments/p<postID>', methods=['POST'])
def add_comment_to_post(postID):
    the_data = request.json
    current_app.logger.info(the_data)
    
    query = '''
            INSERT INTO Comments (
                PostId,
                OwnerId,
                PostContent
            ) VALUES (%s, %s, %s)
        '''
        
    params = (
        postID, 
        the_data['owner_id'], 
        the_data['comment_content']        
    )

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    db.get_db().commit()
    cursor.close()
    
    return make_response({"message": "Successfully added comment"}, 200)