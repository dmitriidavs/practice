from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DADTABASE_URL


def main():
    engine = create_engine(DADTABASE_URL)
    session = Session(bind=engine.connect())

    session.execute("""
        CREATE TABLE users(
            id integer not null primary key,
            email varchar(256),
            password varchar(256),
            first_name varchar(256),
            last_name varchar(256),
            nickname varchar(256),
            created_at varchar(256)
        )
    """)

    session.execute("""
        CREATE TABLE auth_token(
            id integer not null primary key,
            token varchar(256),
            user_id integer references users,
            created_at varchar(256)
        )
    """)

    session.execute("""
        CREATE TABLE stream(
            id integer not null primary key,
            user_id integer references users,
            title varchar(256),
            topic varchar(256),
            status varchar(256),
            created_at varchar(256)
        )
    """)

    session.close()


if __name__ == '__main__':
    main()
