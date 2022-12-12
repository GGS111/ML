# Comparison of CatBoost vs XGBoost

### This is a machine learning model that uses a gradient boosting algorithm based on decision trees for classification, regression problems.


### Changes in CatBoost:

- *iterations:* Number of iterations
- *learning_rate:* Learning rate. The larger lr, the faster the training will occur, but the quality is worse. And vice versa
- *depth: Maximum tree depth*
- *Overtraining detector:*. The point that shows when the retraining occurred
- *l2_leaf_reg:* L2 Regularization - Fights overfitting
- *random_strange:* - Noise that can be added for random
- *bagging_temperature:* - Used in the Byows bootstrap.
- *Tree depth:* - usually worth trying 6 or 10
- *feature_border_type:* Binarization Size - Worth picking, trying
- *rsm:* rsm - Select the number of features to build the tree structure