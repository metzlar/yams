from yams.collect import BaseCollector

try:
    from sqlalchemy import func, create_engine, MetaData
    from sqlalchemy.orm import sessionmaker
except ImportError:
    raise Exception((
        'DBCollector depends on sqlalchemy to be installed'
    ))

class DBCollector(BaseCollector):

    def __init__(self, db_url, *args, **kwargs):
        super(BaseCollector, self).__init__(*args, **kwargs)

        self.engine = create_engine(db_url, ehco=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.metadata = MetaData(self.engine)

    def count(self, subject, property_name = None):
        if property_name is None:
            property_name = 'count_%s' % subject

        def _f(pname, session, s):
            result = session.query(func.count(s)).scalar()
            self.write(pname, result)

        self.schedule(_f, property_name, self.session, subject)
