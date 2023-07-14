# compression_classification

[![Python package](https://github.com/willf/compression_classification/actions/workflows/test.yml/badge.svg)](https://github.com/willf/compression_classification/actions/workflows/test.yml)

Compression Classification is a Python package for classifying via compression.

It is inspired by my talk on "Stupid Entropy Tricks" (reference to come) and  [“Low-Resource” Text Classification: A Parameter-Free Classification
Method with Compressors](https://aclanthology.org/2023.findings-acl.426.pdf)

Simple example:

```python
In [4]: from compression_classification import compression_classification


In [5]:

In [5]: clr = compression_classification.CompressionClassifier()

In [6]: clr
Out[6]: CompressionClassifier()

In [7]: clr.train_with_examples({"zh": "FilterGenie 的基础设施旨在处理大量数据而不影响性能。 无论您拥有小型项目还是大型企业应用程序，我们
   ...: 的 API 都可以轻松扩展以满足您的需求。", "en": "FilterGenie's infrastructure is built to handle high volumes of data without compro
   ...: mising performance. Whether you have a small-scale project or a large enterprise application, our API scales effortlessly to meet
   ...: your needs."})

In [8]: clr.predict_text("This is the day they give babies away")
Out[8]: 'en'

In [9]: clr.predict_text("这一天是他们送孩子的日子")
Out[9]: 'zh'
```



## Contributing

We welcome contributions to compression_classification. Please see our [contributing guidelines](contributing.md) for more information.

## Code of Conduct

We expect project participants to adhere to our [Code of Conduct](code-of-conduct.md).
