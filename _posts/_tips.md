---
#test
title: "깃허브(GitHub) 블로그 폰트 바꾸는법 (otf, woff 파일 사용)"
excerpt: "깃허브 블로그 폰트 바꾸기 otf, woff, ttf 파일을 사용해서 리디바탕 및 웹폰트를 jekyll minimal mistakes 테마에 적용하는법"

categories:
    - Blog
tags:
    - Blog
    - tag2
last_modified_at: 2020-12-13T23:13:02+09:00

# 썸네일
image: 
  feature: feature-image-filename.jpg
  thumb: thumbnail-image.jpg #keep it square 200x200 px is good

  author_profile: true / false #작성자 프로필 출력여부
read_time: false # read_time을 출력할지 여부 1min read 같은것!

toc: true #Table Of Contents 목차 보여줌
toc_label: "My Table of Contents" # toc 이름 정의
toc_icon: "cog" #font Awesome아이콘으로 toc 아이콘 설정
toc_sticky: true # 스크롤 내릴때 같이 내려가는 목차

gallery: #이미지 갤러리
  - url: /assets/images/unsplash-gallery-image-1.jpg
    image_path: /assets/images/unsplash-gallery-image-1-th.jpg
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: /assets/images/unsplash-gallery-image-2.jpg
    image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Image 2 title caption"
#다음과 같이 본문에서 사용한다.
{% include gallery caption="This is a sample gallery with **Markdown support**." %}

header:  # 헤더에 유튜브 비디오 삽입
  video:
    id: XsxDH4HcOWA
    provider: youtube


link: https://github.com # Direct Link 만들기
---

../assets/images/clipboard/thumnai-image.png

# jekyll 실행
bundle exec jekyll serve

# 제목 글자수 팁
코로나19로 인한 정부 재난지원금을 받을 수 있는 조건과 신청방법 뛰어쓰기 포함 25~32자로 완성



