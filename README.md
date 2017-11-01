# BongDal 중고 서점 프로젝트
책을 파는 사람과 사는 사람을 매칭해주는 웹 서비스

## 핵심기능
- Naver Book API 연동하여 책 검색 및 정보 기입 [구현]
- 책 파는 사람과 책 사는 사람 매칭(동일한 ISBN이 각각 리스트에 존재하면 알람 발송) [구현]
- 별점 [구현] + 책 리뷰
- 태그 댓글 등록시 태그 대상 사용자에게 알람 발송 [구현]
- 책 추천 알고리즘
- 장바구니 [구현]
- 관심 사용자가 글을 등록하면 팔로우 한 사용자에게 알람 발송 [구현]

## 개발환경
- OS: Mac OS
- Language: Python 3.6.1
- Database: SQLite3, PostgreSQL
- Framework: Django 1.11.3
- Docker: 17.06.0
- deploy: AWS Elastic Beanstalk
