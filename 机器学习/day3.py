from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
import joblib
import pandas as pd
import numpy as np
import tensorflow


def mylinear():
    """线性回归直接预测房子价格"""
    # 获取数据
    lb = load_boston()

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
    print(y_train, y_test)
    # 特征值和目标值都必须进行标准化实例化两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    # 目标值
    std_y = StandardScaler()

    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 数据转换成二维
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # 预测房价结果
    model = joblib.load("./temp/test.pkl")

    y_predict = std_y.inverse_transform(model.predict(x_test))
    print("预测的结果：", y_predict)
    # 正规方程求解方式预测结果
    # lr = LinearRegression()
    # lr.fit(x_train, y_train)
    # print("coef", lr.coef_)
    # # 保存训练好的模型
    # joblib.dump(lr, "./temp/test.pkl")
    # 预测测试集的房子价格
    # y_predict = std_y.inverse_transform(lr.predict(x_test))
    #print("测试集里每个房子的预测价格：", y_predict)
    #print("正规方程的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_predict))

    # # 梯度下降进行房价预测（适用于数据量大）
    # sgd = SGDRegressor()
    # sgd.fit(x_train, y_train.ravel())
    # print("sgdcoef", sgd.coef_)
    # # 预测测试集的房子价格
    # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # s = sgd.predict(x_test).reshape(-1, 1)
    # # *********************************
    # y_sgd_predict = std_y.inverse_transform(s)
    # print("SGD测试集里每个房子的预测价格：", y_sgd_predict)
    # print("梯度下降的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict))
    #
    # 岭回归进行房价预测
    rd = Ridge(alpha=1.0)
    rd.fit(x_train, y_train)
    print("rdcoef", rd.coef_)
    # 预测测试集的房子价格

    y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
    print("岭回归测试集里每个房子的预测价格：", y_rd_predict)
    print("岭回归的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_rd_predict))

    return None


def logistic():
    """
    逻辑回归做二分类进行癌症预测
    :return:
    """
    # 构造列标签名字
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']

    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=column)
    print(data)
    data = data.replace(to_replace='?', value=np.nan)
    # 删除na数据
    data = data.dropna()
    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)
    # 标准化处理
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    # 逻辑回归预测
    lg = LogisticRegression(C=1.0)
    lg.fit(x_train, y_train)
    print(lg.coef_)
    y_predict = lg.predict(x_test)
    print("准确率", lg.score(x_test, y_test))
    print("召回率", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))
    return None


if __name__ == '__main__':
    mylinear()
    #logistic()
