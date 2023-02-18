from operator import itemgetter
from apibackend import ALLOWED_EXTENSIONS

#process of file upload in /questionnaire_upd
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Sort the tuples by the second item using the itemgetter function
def sort_tuples(tup):
    return sorted(tup, key=itemgetter(0))
