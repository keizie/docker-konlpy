# docker-konlpy

`docker build . --tag konlpy`

`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/corpus.py`
`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/hannanum.py`
`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/kkma.py`
`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/komoran.py`
`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/mecab.py`
`docker run -it --rm --volume=$(pwd):/opt/konlpy konlpy python examples/okt.py`
