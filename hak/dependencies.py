from typing import Generator

from hak.databases.session import SessionLocal


def get_database() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
