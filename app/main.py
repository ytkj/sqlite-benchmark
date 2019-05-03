import argparse
from statistics import mean
from random import random
from flask import Flask

from .mapper import db, ItemMapper
from .util import random_text, StopWatch


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--inmemory', action='store_true', help='use sqlite in-memory mode. if not, file-mode.')
parser.add_argument('-i', '--iterations', type=int, default=10, help='number of iteration of measurements. default: 10')
parser.add_argument('-r', '--records', type=int, default=1000000, help='number of records. default: 1,000,000')
args = parser.parse_args()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

if args.inmemory:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'

db.init_app(app)

with app.app_context():

    reports = []

    for i_measure in range(args.iterations):

        print('-- measurement #{0} --'.format(i_measure+1))

        db.create_all()
        sw = StopWatch()
        sw.start()

        entities = [dict(
            text1=random_text(3),
            text2=random_text(3),
            number1=random(),
            number2=random(),
        ) for i in range(args.records)]
        sw.wrap('generate {0} records'.format(args.records))

        db.session.execute(ItemMapper.__table__.insert(), entities)
        db.session.commit()
        sw.wrap('bulk insert {0} records'.format(args.records))

        del entities

        item = ItemMapper()
        item.text1 = 'aaa'
        item.text2 = 'bbb'
        item.number1 = 0.1
        item.number2 = 0.2
        db.session.add(item)
        db.session.commit()
        sw.wrap('insert 1 records')

        result1 = ItemMapper.query.order_by(ItemMapper.text1, ItemMapper.text2).offset(1000).limit(20).all()
        sw.wrap('select order by text1, text2 offset 1000 limit 20')

        result2 = ItemMapper.query.order_by(ItemMapper.number1, ItemMapper.number2).offset(1000).limit(20).all()
        sw.wrap('select order by number1, number2 offset 1000 limit 20')

        result3 = ItemMapper.query.filter(ItemMapper.text1.startswith('a')) \
            .filter(ItemMapper.number1 > 0.5).offset(1000).limit(20).all()
        sw.wrap('select where text1 like a* and number1 > 0.5 offset 1000 limit 20')

        ItemMapper.query.filter(ItemMapper.text1 == 'aaa').update(dict(text1='bbb'))
        db.session.commit()
        sw.wrap('update text1 bbb where text1==aaa')

        ItemMapper.query.filter(ItemMapper.text1 == 'bbb').delete()
        db.session.commit()
        sw.wrap('delete where text1 == bbb')

        sw.describe()
        reports.append(sw.get_report())

        db.drop_all()

    # calc average time
    average_report = reports[0]
    for i, d in enumerate(average_report):
        d['time'] = mean([r[i]['time'] for r in reports])

    print('-- average --')
    StopWatch().describe(average_report)
