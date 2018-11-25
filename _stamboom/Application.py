from _stamboom.app import app, db
from _stamboom.app.Models import User, Post, Person, ParentChildRelationship

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Person': Person, 'ParentChildRelationship': ParentChildRelationship}

if __name__ == '__main__':
    app.run()
