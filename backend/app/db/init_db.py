from sqlmodel import Session, select
from .base import create_db_and_tables, engine
from ..models.user import User, Role

def init_db():
    create_db_and_tables()


    with Session(engine) as session:
        if not session.exec(select(Role)).first():
            admin_role = Role(name='admin', description='admin role')
            user_role = Role(name='user', description='user role')
            session.add(admin_role)
            session.add(user_role)
            session.commit()

            user = User(
                username='admin',
                email='admin@draiver.com',
                hashed_password='password',
                roles=[admin_role],
            )
            session.add(user)
            session.commit()

