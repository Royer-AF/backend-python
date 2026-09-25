from sqlmodel import SQLModel, Session, create_engine

sqlite_file_name = "tienda_relacional.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session