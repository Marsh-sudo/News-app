
import unittest
from ..models import news,articles
Articles = articles.Articles
Sources = news.Sources

class SourceTest(unittest.TestCase):
    '''
    test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Sources('cnn','Cnn','The Cables News Network is the worlds most popular news hub in the globe','https://edition.cnn.com','en','USA')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == '__main__':
    unittest.main()
