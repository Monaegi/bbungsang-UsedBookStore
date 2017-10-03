FROM            usedbookstore_ubuntu
MAINTAINER      bbungsang@gmail.com

ENV             LANG C.UTF-8

# 현재 경로의 모든 파일을 컨테이너의 /srv/used-book-store 폴더에 복사
COPY            . /srv/used-book-store

# cd /srv/used-book-store와 같은 효과
WORKDIR         /srv/used-book-store

# requirements 설치
RUN             /root/.pyenv/versions/used-book-store/bin/pip install -r .requirements/deploy.txt

# supervisor 파일 복사
COPY            .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY            .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx 파일 복사
COPY            .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY            .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf

# 기존 80 포트 요청을 받는 default 제거
RUN             rm -rf /etc/nginx/sites-enabled/default
# symbolic link 생성
RUN             ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.ini
