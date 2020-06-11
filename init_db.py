from sqlalchemy import create_engine, MetaData
from project.settings import config

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    