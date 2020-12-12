import sys

from flask.cli import FlaskGroup

from src import create_app, db
from src.api.users.models import User
from src.api.places.models import Place

from get_mapdata import get_mapdata

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='test', email="test@cornell.edu", password="password123"))
    db.session.add(User(username='test123', email="test123@cornell.edu", password="password123"))
    db.session.commit()

    mdata = get_mapdata()
    for data in mdata:
        db.session.add(
            Place(
                lat=data["lat"], lon=data["lon"], name=data["name"], types=data["types"]
            )
        )
    db.session.commit()


if __name__ == '__main__':
    cli()
