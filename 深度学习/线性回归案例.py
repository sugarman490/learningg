import tensorflow as tf
import os

tf.compat.v1.disable_eager_execution()

# 训练参数问题：trainable
# 添加权重参数，损失值等在tensorboard观察的情况 1. 收集变量2.合并变量

# 定义命令行参数
# 1.首先定义有哪些参数需要在运行时候指定
# 2.程序当中获取定义命令行参数
# 第一个参数：名字，默认值，说明
tf.compat.v1.app.flags.DEFINE_integer("max_step", 100, "模型训练的步数")
tf.compat.v1.app.flags.DEFINE_string("model_dir", " ", "模型文件的加载路径")

# 定义获取命令行参数名字
FLAGS=tf.compat.v1.app.flags.FLAGS
def myLinear():
    """自实现一个线性回归预测"""
    with tf.compat.v1.variable_scope("data"):
        # 1.准备数据，x 特征值[100,1] y 目标值[100]
        x = tf.random.normal([100, 1], mean=1.75, stddev=0.5, name="x_data")
        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8
    with tf.compat.v1.variable_scope("model"):
        # 2.建立线性回归模型 1个特征，1个权重，一个偏置 y=xw+b
        # 随机给一个权重和偏置的值，计算损失，然后在当前状态下优化
        # 用变量定义才能优化
        # trainable参数：指定这个变量能跟着梯度下降一起优化
        weight = tf.Variable(tf.random.normal([1, 1], mean=0.0, stddev=1.0, name="w"))  # 一行一列
        bias = tf.Variable(0.0, name="b")
        y_predict = tf.matmul(x, weight) + bias
    with tf.compat.v1.variable_scope("loss"):
        # 3.建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))
    with tf.compat.v1.variable_scope("optimizer"):
        # 4.梯度下降优化损失 learning_rate:0~1,2,3,5,7,10
        train_op = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)
    # 1.收集tensor
    tf.compat.v1.summary.scalar("losses", loss)
    tf.compat.v1.summary.histogram("weights", weight)
    # 2.定义合并tensor的op
    merged = tf.compat.v1.summary.merge_all()
    # 定义一个初始化变量的op
    init_op = tf.compat.v1.global_variables_initializer()
    # 定义一个保存模型的实例
    saver = tf.compat.v1.train.Saver()
    # 通过会话运行程序
    with tf.compat.v1.Session() as sess:
        # 初始化变量
        sess.run(init_op)
        # 打印随机最先初始化的权重和偏置
        print("随机初始化的参数权重为：%f，偏置为：%f" % (weight.eval(), bias.eval()))
        # 建立事件文件
        fw = tf.compat.v1.summary.FileWriter("./summary/test2/", graph=sess.graph)

        # 加载模型，覆盖模型当中随机定义的参数，从上次训练的参数结果开始
        if os.path.exists("./ckpt/checkpoint"):
            saver.restore(sess,"./ckpt/model")
        # 循环训练 运行优化
        for i in range(500):
            sess.run(train_op)
            # 运行合并的tensor
            summary = sess.run(merged)
            fw.add_summary(summary, i)
            print("第%d次优化的参数权重为：%f，偏置为：%f" % (i, weight.eval(), bias.eval()))
            saver.save(sess, "./ckpt/model")
    return None


if __name__ == '__main__':
    myLinear()
