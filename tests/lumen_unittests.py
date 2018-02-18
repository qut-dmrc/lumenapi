from api import Lumen
from nose.tools import assert_equal, assert_not_equal, assert_raises, assert_true


class TestLumen(object):
    def __init__(self):
        self.lumen = Lumen()

    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search(self):
        search_dict = {'recipient_name': 'youtube', 'per_page': 1, 'sort_by': 'date_received desc'}
        results = self.lumen.search(search_dict)
        assert_true(results['meta']['total_entries'] > 40000)


    def test_get(self):
        notice = '14457992' # '12853850'
        results = self.lumen.get(notice)
        assert_equal(results.body, 'Defamation complaint')
        assert_equal(results.title, 'Re: Takedown Request regarding Defamation Complaint to YouTube')
        assert_equal(results.recipient_name, 'YouTube (Google, Inc.)')
