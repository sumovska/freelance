from unittest import TestCase
from encoders import JsonEncoder
from datetime import datetime
import json


class TestJsonEncoder(TestCase):
    def test_loadEmptyDict(self):
        self.assertEquals('{}', json.dumps({}, cls=JsonEncoder))

    def test_loadSimpleDict(self):
        self.assertEquals('{"foo": 32}', json.dumps({'foo': 32}, cls=JsonEncoder))

    def test_loadDateTime(self):
        self.assertEquals(
            '{"date": "2014-12-12T01:46:57"}', json.dumps(
                {'date': datetime(2014, 12, 12, 1, 46, 57)},
                cls=JsonEncoder))

    def test_arbitruary_with_asdict(self):
        class Foo(object):
            def as_dict(self):
                return {'hey': 'there'}
                
          
        self.assertEquals(
            '{"arbitruary": {"hey": "there"}}', json.dumps(
                {'arbitruary': Foo()},
                cls=JsonEncoder))