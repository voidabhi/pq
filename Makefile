build: clean copy tar

clean:
    rm -rf dist dist.tar.gz

copy:
    mkdir dist
    cp -R pq.py dist
    cp -R .crossbar dist
    cp requirements.txt dist
    cp Makefile dist

tar:
    tar -zc dist/ | gzip > dist.tar.gz
