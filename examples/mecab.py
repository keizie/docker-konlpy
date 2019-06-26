# MeCab installation needed
from konlpy.tag import Mecab
mecab = Mecab()
print(mecab.morphs(u'영등포구청역에 있는 맛집 좀 알려주세요.'))
print(mecab.nouns(u'우리나라에는 무릎 치료를 잘하는 정형외과가 없는가!'))
print(mecab.pos(u'자연주의 쇼핑몰은 어떤 곳인가?'))
