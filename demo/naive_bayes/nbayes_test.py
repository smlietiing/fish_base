from fish_base import naive_bayes
import jieba


nb = naive_bayes.NaiveBayes()

nb.train()

test_list = ['love', 'my', 'dalmation']
print(test_list, 'classified as: ', nb.run(test_list))

test_list = ['stupid', 'garbage']
print(test_list, 'classified as: ', nb.run(test_list))


# for Chinese

# 初始化系统变量
nb.train_doc_list = []
nb.train_doc_sent_vec = []

# 初始化分词
nb.init_cut_word()

# 读入停用词
nb.load_stopword()

# 打开中文训练文档
nb.open_train_doc_ch('train_bayes/good.txt', 0)
nb.open_train_doc_ch('train_bayes/bad.txt', 1)

print(nb.train_doc_list)

# 训练
nb.train()
print(nb.p0_v, nb.p1_v, nb.p_ab)

print(nb.test('train_bayes/test.txt'))

# 指定测试
print()
test_s = '这个手机很好,我很喜欢'
print(test_s)
test_list = list(jieba.cut(test_s))
p = nb.run(test_list)
if p == 0:
    print('classified as good ')
else:
    print('classified as bad ')

# while 1:
#     test_s = input('input comment:')
#     test_list = list(jieba.cut(test_s))
#     print(test_list)
#     p = nb.run_nb(test_list)
#     if p == 0:
#         print('classified as good ')
#     else:
#         print('classified as bad ')
#
#     print()

# 2016.5.18
# {'01': 1, '10': 5, '00': 7, '11': 3}
# (0.875, 0.375)
#
#
# 2016.5.18 增加去除停用词,一般意义
# {'11': 4, '00': 8, '10': 4, '01': 0}
# (1.0, 0.5)

