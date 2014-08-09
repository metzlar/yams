from yams.collect import BaseCollector

try:
    from sqlalchemy import func, create_engine, MetaData, Table
    from sqlalchemy.orm import sessionmaker
except ImportError:
    raise Exception((
        'DBCollector depends on sqlalchemy to be installed'
    ))

class DBCollector(BaseCollector):

    def __init__(self, db_url, *args, **kwargs):
        super(DBCollector, self).__init__(*args, **kwargs)

        self.engine = create_engine(db_url)
        self.metadata = MetaData(self.engine)
        self.func = func
        self.queries = {}

    def _get_table(self, name):
        return Table(
            name,
            self.metadata,
            autoload=True
        )

    def add_query(self, name, callable):
        '''
        Add and prepare a query to this collector. A query is a
        callable that expects a reference to its table. Example:

        db.add_query(
           'count',
           lambda table: db.session.query(
              db.func.count(table.c.id)
           ).filter(
              table.c.start_time > db.func.now()
           ).scalar())

        This adds the query with name 'count' that returns a single
        scalar that contains the count of the table's records that
        have a start_time greater then now().

        To execute (schedule) this query for the table 'appointment'

        db.execute('appointment', 'count')

        Use self.func and self.session to build the actual query.
        '''
        self.queries[name] = callable

    @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def execute(self, table_name, query_name, property_name = None):
        if property_name is None:
            property_name = '%s_%s' % (query_name, table_name)
        def _f(pname, t, q):
            query = self.queries[q]
            table = self._get_table(t)
            result = query(table)
            self.write(pname, result)

        self.schedule(_f, property_name, table_name, query_name)
