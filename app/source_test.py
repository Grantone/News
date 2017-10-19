import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
