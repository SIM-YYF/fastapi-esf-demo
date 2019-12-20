# SQLAlchemy specific code, as with any other app
import databases
import sqlalchemy
from sqlalchemy import Integer, String
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/test_esf"

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "esf_user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("role_id", sqlalchemy.ForeignKey('esf_roles.id', ondelete='CASCADE')),  # 级联删除
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("full_name", sqlalchemy.String)

)

roles = sqlalchemy.Table(
    "esf_roles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('esf_user.id', ondelete='CASCADE')),  # 级联删除
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("display", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    echo=True
)

metadata.create_all(engine)
