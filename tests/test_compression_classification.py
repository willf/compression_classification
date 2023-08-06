import unittest

from compression_classification.compression_classification import CompressionClassifier


class TestCompressionClassification(unittest.TestCase):
    def test_basics(self):
        clr = CompressionClassifier(n=4)
        clr.train("FilterGenie 的基础设施旨在处理大量数据而不影响性能。 无论您拥有小型项目还是大型企业应用程序，我们 的 API 都可以轻松扩展以满足您的需求。", "zh")
        clr.train("FilterGenie's infrastructure is built to handle high volumes of data without compromising performance. Whether you have a small-scale project or a large enterprise application, our API scales effortlessly to meet your needs.", "en")
        assert clr.predict("This is the day they give babies away.") == "en"
        assert clr.predict("这是主所造的日子") == "zh"
