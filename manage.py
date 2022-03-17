
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Meal, Order
from flask_migrate import Migrate, MigrateCommand


app= create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Running the Unittests"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#creating shell context

@manager.shell
def make_shell_context():
<<<<<<< HEAD
    return dict(app=app, db=db, User=User, Meal=Meal, Order=Order)
=======
    return dict(app=app, db=db, User=User)
 if __name__ == '__main__':
    manager.run()



from app import create_app,db
from app.models import User
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
>>>>>>> 8477f906db3241b00534d09a22eb2f442e163f96

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
@manager.command
def test():
    """Running the Unittests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User )
if __name__ == '__main__':
    manager.run()