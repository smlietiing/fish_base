from fish_base import bayes
# import jieba

nb = bayes.ClassNaiveBayes()

nb.train()

test_list = ['love', 'my', 'dalmation']
print(test_list, 'classified as: ', nb.run_nb(test_list))

test_list = ['stupid', 'garbage']
print(test_list, 'classified as: ', nb.run_nb(test_list))

nb.train_doc_list = []
nb.train_doc_sent_vec = []

# for Chinese

nb.init_cut_word()

nb.open_train_doc_ch('train_bayes/good.txt', 0)
nb.open_train_doc_ch('train_bayes/bad.txt', 1)

nb.train()
print(nb.p0_v, nb.p1_v, nb.p_ab)

print(nb.test_nb('train_bayes/test.txt'))

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