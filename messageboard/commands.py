import click
from messageboard import app, db
from messageboard.models import Message

@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initial Database')

@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    faker = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name = faker.name(),
            body = faker.sentence(),
            timestamp = faker.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo("Created %d fake messages" % count)

    