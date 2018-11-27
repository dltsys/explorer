FROM ubuntu:16.04
RUN apt update && \
    apt-get install -y apache2 libapache2-mod-fcgid python-flup python-crypto
RUN apt-get install -y python-psycopg2 git curl python-dev build-essential

RUN git clone https://github.com/rlaime/c11_hash && \
    cd c11_hash && \
    python setup.py install

#ADD dash-abe /abe/
RUN git clone https://github.com/nightlydash/dash-abe /abe/

ADD Smash.py /abe/Abe/Chain/Smash.py
ADD C11Chain.py /abe/Abe/Chain/C11Chain.py
ADD C11PosChain.py /abe/Abe/Chain/C11PosChain.py
ADD abe.fcgi /abe/cgi-bin/abe.fcgi
ADD abe-apache.conf /etc/apache2/sites-available/abe.conf
ADD abe.conf /abe
ADD abe.css /abe/Abe/htdocs/abe.css
ADD favicon.ico /abe/Abe/htdocs/favicon.ico
ADD logo32.png /abe/Abe/htdocs/logo32.png

RUN cd /abe && python setup.py install && update-rc.d apache2 enable && \
    rm -Rf /etc/apache2/sites-enabled/*.conf && \
    ln -s /etc/apache2/sites-available/abe.conf /etc/apache2/sites-enabled/abe.conf && \
    mkdir /data

VOLUME /data
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
