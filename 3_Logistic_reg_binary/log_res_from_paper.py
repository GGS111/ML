import numpy as np
from sklearn.datasets import make_blobs


class LogisticRegression:
    def __init__(self, X, learning_rate=0.1, num_iters=10000):
        self.lr = learning_rate
        self.num_iters = num_iters

        # m for #training_examples, n for #features
        self.m, self.n = X.shape

    def train(self, X, y):
        # init weights
        self.weights = np.zeros((self.n, 1))
        self.bias = 0

        for it in range(self.num_iters + 1):
            # calculate hypothesis. 
            # С помощью Сигмоиды мы только получаем Предикт, так как нам нужен класс
            y_predict = self.sigmoid(np.dot(X, self.weights) + self.bias)

            # Берем Лосс Бинарную Кросс Энтропию так как рассматриваем 2 класса. 0 или 1
            loss = (-1 / self.m * np.sum(y * np.log(y_predict) + (1 - y) * np.log(1 - y_predict)))

            # back prop / gradient calculations
            # Производные при бинарной Кросс энтропии. Х вылетает когда берется производная 
            dw = 1 / self.m * np.dot(X.T, (y_predict - y)) 
            db = 1 / self.m * np.sum(y_predict - y)

            # gradient descent update step
            # Обновляем веса, количество весов зависит от количества Признаков
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # print cost sometimes
            if it % 1000 == 0:
                print(f"Cost after iteration {it}: {loss}")

        return self.weights, self.bias

    def predict(self, X):
        y_predict = self.sigmoid(np.dot(X, self.weights) + self.bias)
        y_predict_labels = y_predict > 0.5

        return y_predict_labels

    def sigmoid(self, z):
        #print('z', z.shape)
        return 1 / (1 + np.exp(-z))


if __name__ == "__main__":
    np.random.seed(1)
    X, y = make_blobs(n_samples=1000, n_features=2, centers=2)
    y = y[:, np.newaxis]

    logreg = LogisticRegression(X, num_iters=10000)
    w, b = logreg.train(X, y)
    y_predict = logreg.predict(X)

    print(f"Accuracy: {np.sum(y==y_predict)/X.shape[0]}")