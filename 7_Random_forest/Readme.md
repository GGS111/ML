# Random Forest Model from Sklearn

### We simply divide the training sample into many separate models, and at the end we consider which model responses, and choose the response of which is greater. Models can be retrained and be as random and different from each other as possible. This is the main concept

![plot](./rf.jpg)


### Changes:

- n_estimators: number of trees
- max_depth: max depths of model
- min_samples_split: min number of features in Node
- max_features: number of features
- criterion: Criterion: Gini, Entropy, LogLoss
- bootstrap='True` (default), otherwise the whole dataset is used for building.