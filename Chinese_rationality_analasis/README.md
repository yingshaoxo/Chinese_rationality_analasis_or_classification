# Tutorial for Chinese Sentiment analysis with hotel review data
The repo contains the trainig data located in the data folder and a jupyter notebook for the tutorial.

## Dependencies
Python 3.6, numpy, pickle, keras, tensorflow, [jieba](https://github.com/fxsjy/jieba)

### Optional Dependencies for plotting
pylab, scipy

### How to Run
Run the python notebook by cd into the directory in command line then run
```
jupyter notebook
```
choose this in the browser: **chinese_sentiment_analysis.ipynb**

### Thanks to [Tony607/Chinese_sentiment_analysis](https://github.com/Tony607/Chinese_sentiment_analysis)

___

### 中文说明

你好，我叫 yingshaoxo ，我们这次的项目用到了 keras。

该模型可以检测语言是否理性，理性为`positive`，非理性为`negative`.

#### 训练自己的模型

训练属于自己的文本分类器，你需要准备好编码格式为`utf-8`的文本文件，把它们放在`Data/positive`或`Data/negative`文件夹(其内在格式可以参考原文件夹txt文件)

然后使用`jupter notebook` 按照 `training.ipynb` 的说明操作

你也可以直接在线看这个 [traning.ipynb]()

#### 应用模型做预测

运行 `demo.py`

配置好`selenium`环境的可以运行 `demo_website.py`