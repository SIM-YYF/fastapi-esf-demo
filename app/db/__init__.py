# SQLAlchemy specific code, as with any other app
import databases
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database


DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/esf"

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "esf_user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

roles = sqlalchemy.Table(
    "esf_roles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    echo=True
)

metadata.create_all(engine)
