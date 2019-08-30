from sqlalchemy.orm import sessionmaker
from csgostash.models import SkinDB, db_connect, create_table


class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        quotedb = SkinDB()
        quotedb.name = item["name"]

        try:
            session.add(quotedb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item