build: clean copy tar

clean:
    rm -rf dist dist.tar.gz

copy:
    pip freeze > requirements.txt
    mkdir dist
    cp -R pq.py dist
    cp -R .crossbar dist
    cp requirements.txt dist
    cp Makefile dist

bench:
	sh benchmark.sh

tar:
    tar -zc dist/ | gzip > dist.tar.gz
