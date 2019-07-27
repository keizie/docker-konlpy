import sys
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Okt
from konlpy.tag import Mecab
from konlpy.tag import Komoran

hannanum = Hannanum()
kkma = Kkma()
#komoran = Komoran(userdic='/tmp/dic.txt')
#mecab = Mecab()
okt = Okt()

def main():
    while 1:
        line = sys.stdin.readline()
        if not line:
            break

        nouns = []
        nouns.extend(hannanum.nouns(line))
        nouns.extend(kkma.nouns(line))
        #nouns.extend(komoran.nouns(line))
        #nouns.extend(mecab.nouns(line))
        nouns.extend(okt.nouns(line))

        nouns = set(nouns)

        for noun in nouns:
            print(noun)

if __name__ == "__main__":
    main()

# curl https://twitter.com/gakumu/status/1154946332957609986| ~/go/bin/pup 'p.tweet-text text{}' | docker run -i --rm docker-konlpy python3 main.py