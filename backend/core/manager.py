from core import core 
from core import db 
from flask_migrate import Migrate ,MigrateCommand
from flask_script import Manager

migrate = Migrate(core,db)

manager = Manager(core)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

