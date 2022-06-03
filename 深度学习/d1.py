import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.disable_eager_execution()
# 创建一张图包含了一组op和tensor,上下文环境
# op:只要使用tensorflow的API定义的函数都是op
# tensor:就指代的是数据
# g = tf.Graph()
# print(g)
# with g.as_default():
#     c = tf.constant(10.0)
#     print(c.graph)
#
# # (tensorflow2.0)保证sess.run()能够正常运行
# tf.compat.v1.disable_eager_execution()
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# sum1 = tf.add(a, b)
# # print(sum1)
# # 默认的这张图，相当于给程序分配一段内存
# graph = tf.compat.v1.get_default_graph()
# print(graph)
# var1 = 2.0
# # 有重载机制，默认会给运算符重载称op类型
# sum2 = a + var1
# print("sum2:", sum2)
# # 会话只能运行一个图，可以在会话当中指定图去运行
# # 只要有会话的上下文环境，就可以使用eval()
#
# # 训练模型
# # 实时提供数据去进行训练
#
# # placeholder是一个占位符,feed_dict是一个字典
# plt = tf.compat.v1.placeholder(tf.float32, [None, 3])
# print(plt)
# with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess:
#     print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 6, ], [2, 3, 4]]}))
#     print(a.graph)
#     print("-" * 50)
#     print(a.shape)
#     print(plt.shape)
#     print("-" * 50)
#     print(a.name)
#     print("-" * 50)
#     print(a.op)
#     # print(sum1.graph)
#     # print(sess.graph)

# tensorflow:打印出来的形状表示
# 0维：（） 1维：（） 2维：（5，6） 3维：（2，3，4）

# 形状的概念
# 静态形状和动态形状
# 对于静态形状来说，一旦张量形状固定了，不能再次设置静态形状，不能跨维度修改1D->1D,2D->2D
# 动态形状可以去创建一个新的张量,改变的时候一定要注意元素数量要匹配

# plt = tf.compat.v1.placeholder(tf.float32, [None, 2])
# print(plt)
# plt.set_shape([3, 2])
# print(plt)
# # plt.set_shape([2, 3])#报错，不能再次修改
# plt_reshape = tf.reshape(plt, [2, 3])  # 元素个数不能不匹配
# print(plt_reshape)
# with tf.compat.v1.Session() as sess:
#     pass

# 变量op
# 1.变量op能够持久化保存，普通张量op不行
# 2.当定义一个变量op时，一定要在会话中去运行初始化
# 3.name参数：在tensorboard使用的时候显示名字，可以让相同op名字的进行区分
a = tf.constant(3.0,name="a")
b = tf.constant(4.0,name="b")
c = tf.add(a, b)
var = tf.Variable(tf.random.normal([2, 3], mean=0.0, stddev=1.0),name="variable")
print(a, var)
# 必须做一步显式的初始化

init_op = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    # 必须运行初始化op
    sess.run(init_op)

    # 把程序的图结构写入事件文件

    filewriter = tf.compat.v1.summary.FileWriter("./summary/test/", graph=sess.graph)
    print(sess.run([c, var]))
