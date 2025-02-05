db = []

def add_comment(comment):
    db.append(comment)

def get_comments(query=None):
    return db