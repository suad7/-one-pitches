from app import app
from app import db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitch

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def add_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(debug=True)
