# coding: utf-8

# manage.py

import click
from flask.cli import with_appcontext

from app import guard
from app.model import User

from app.database import Session, engine
from app.orm import start_mapper, metadata

@click.command(name="create_users")
@with_appcontext
def create_users():
    start_mapper()
    metadata.create_all(bind=engine)
    
    user1 = User("user1", guard.hash_password("secret1"))
    user2 = User(username="user2", password=guard.hash_password("secret2"))
    user3 = User(username="user3", password=guard.hash_password("secret3"))

    Session.add_all([user1, user2, user3])
    Session.commit()

@click.command(name="user")
@with_appcontext
def user():
    start_mapper()
    user = Session.query(User).filter_by(username="user1").first()
    print(user.id)