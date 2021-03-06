from gensim.models import word2vec

model_file = '02_watanabe_w2v_model.model'

model = word2vec.Word2Vec.load('src/' + model_file)
#調べたいワード
words = ['SFC','楽しい','デザイン']
for word in words:
    similar_words = model.most_similar(positive=[word])
    print(word,':',[w[0] for w in similar_words])