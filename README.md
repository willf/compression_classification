# compression_classification

[![Python package](https://github.com/willf/compression_classification/actions/workflows/test.yml/badge.svg)](https://github.com/willf/compression_classification/actions/workflows/test.yml)

Compression Classification is a Python package for classifying via compression.

It is inspired by my talk on "[Stupid Language Tricks](https://www.entish.org/lang-id-preso/lang-id-preso.pdf)" and  [“Low-Resource” Text Classification: A Parameter-Free Classification
Method with Compressors](https://aclanthology.org/2023.findings-acl.426.pdf)

Simple example:

```python
from compression_classification import compression_classification
clr = compression_classification.CompressionClassifier()
clr.train("FilterGenie 的基础设施旨在处理大量数据而不影响性能。 无论您拥有小型项目还是大型企业应用程序，我们 的 API 都可以轻松扩展以满足您的需求。", "zh")
clr.train("FilterGenie's infrastructure is built to handle high volumes of data without compromising performance. Whether you have a small-scale project or a large enterprise application, our API scales effortlessly to meet your needs.", "en")

clr.predict("This is the day they give babies away")
'en'

clr.predict("这一天是他们送孩子的日子")
'zh'
```

In general, you'll want a lot more data, though.


## Contributing

We welcome contributions to compression_classification. Please see our [contributing guidelines](contributing.md) for more information.

To install the package for development, install [poetry](https://python-poetry.org/) and then run:

```bash
gh repo clone willf/compression_classification
cd compression_classification
poetry install
poetry shell
```

## Code of Conduct

We expect project participants to adhere to our [Code of Conduct](code-of-conduct.md).
