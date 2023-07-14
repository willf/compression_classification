from compression_classification.compression_classification import hello_world


class TestCompressionClassification(unittest.TestCase):

    def test_hello_world(self):
        assert hello_world() == "Hello World!"
