---
title: "깃허브(GitHub) 블로그 시작하기 Jekyll로 누구나 쉽게 만들기 가능"
excerpt: "GitHub를 이용한 블로그 시작하기 퀵스타터 쉬운 방법"

categories:
    - Blog
tags:
    - Blog
last_modified_at: 2020-12-12T20:21:02+09:00

gallery:
  - url: /assets/images/001-Create-a-GitHub-Blog/tistory_kakao.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/tistory_kakao.png
    alt: "티스토리 카카오 블로그"
  - url: /assets/images/001-Create-a-GitHub-Blog/티스토리-수익.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/티스토리-수익.png
    alt: "티스토리 수익 샘플"
gallery0:
  - url: /assets/images/001-Create-a-GitHub-Blog/no-style-please.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/no-style-please.png
    alt: "no-style-please"
  - url: /assets/images/001-Create-a-GitHub-Blog/Chirpy-theme.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/Chirpy-theme.png
    alt: "Chirpy-theme"
gallery1:
  - url: /assets/images/001-Create-a-GitHub-Blog/github-hompage.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/github-hompage.png
    alt: "깃허브 홈페이지"
  - url: /assets/images/001-Create-a-GitHub-Blog/create-your-account.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/create-your-account.png
    alt: "깃허브 회원가입"
gallery2:
  - url: /assets/images/001-Create-a-GitHub-Blog/create-new-repository.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/create-new-repository.png
    alt: "create new repository"
  - url: /assets/images/001-Create-a-GitHub-Blog/repository-name.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/repository-name.png
    alt: "repository name"
gallery3:
  - url: /assets/images/001-Create-a-GitHub-Blog/jekyll-theme.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/jekyll-theme.png
    alt: "jekyll theme example"
  - url: /assets/images/001-Create-a-GitHub-Blog/jekyll-themes.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/jekyll-themes.png
    alt: "jekyll themes"
gallery4:
  - url: /assets/images/001-Create-a-GitHub-Blog/import-code-another-repository.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/import-code-another-repository.png
    alt: "import code-another repository"
  - url: /assets/images/001-Create-a-GitHub-Blog/clone-themes.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/clone-themes.png
    alt: "clone themes"
  - url: /assets/images/001-Create-a-GitHub-Blog/Preparing-new-repository.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/Preparing-new-repository.png
    alt: "Preparing new repository"    
gallery5:
  - url: /assets/images/001-Create-a-GitHub-Blog/config-yml-file.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/config-yml-file.png
    alt: "_config.yml 파일 수정 방법1"
  - url: /assets/images/001-Create-a-GitHub-Blog/Edit-this-file.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/Edit-this-file.png
    alt: "_config.yml 파일 수정 방법2"
  - url: /assets/images/001-Create-a-GitHub-Blog/site-settings.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/site-settings.png
    alt: "_config.yml 파일 수정 방법3"   
gallery6:
  - url: /assets/images/001-Create-a-GitHub-Blog/settings-menu.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/settings-menu.png
    alt: "깃허브 페이지 설정1"
  - url: /assets/images/001-Create-a-GitHub-Blog/GitHub-Pages.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/GitHub-Pages.png
    alt: "깃허브 페이지 설정2"
gallery7:
  - url: /assets/images/001-Create-a-GitHub-Blog/blog-main.png
    image_path: /assets/images/001-Create-a-GitHub-Blog/blog-main.png
    alt: "블로그 메인"

---
## 새로운 블로그를 시작하다
필자는 블로그를 약 **8년간** 운영하고 있다. 그 히스토리를 짧게 요약 해보자면 아래와 같다. 만드는 방법만 간단히 보고싶은 분들은 스킵해도 좋다.

성인이 되기 이전에는 네이버 블로그에서 하루 만명 이상의 방문자수를 내는 블로그를 운영해보았고, 여러가지 제품을 무료로 제공 받거나 포스팅 비용을 받고 수익을 창출했다.

{% include gallery id="gallery" %}

그 이후에는 조금 더 수익성을 위해 티스토리를 개설하였고 애드센스를 적용하게되면서 월 xx만원 정도하는 애드센스 수익을 창출하기 시작했다.

위 두개의 공통점은 모두 네이버나, 다음(카카오)의 지배를 받는 다는 점이고 그 만큼 위험(저품질, 검색누락 등)이 아주 큰 단점을 가진다.

그래서 생각해낸 방법이 직접 서버를 파서 운영하던가 워드프레스 같은 서비스를 이용하는 것인데, 웬지 접근하기도 쉽지 않았고 공부하기도 사실 귀찮았다.

그러다가 회사에서 깃허브를 자주 사용하면서 부터 갑자기 구글링할 때 github 블로그들이 많이 눈에 들어왔고, 어쩌다가 이렇게 만들게 되었는데 생각보다 재미있어서 거의 퇴근을 하고 12시 까지 만들정도로 몰입했다.

### 티스토리에서 깃허브 블로그로 갈아탄 이유
내가 티스토리 블로그에서 깃허브 블로그를 운영하게 된 가장 큰 이유 3가지는 이렇다.
1. 먼저 당연히 깃허브 블로그에서도 애드센스를 달 수 있다는 점이다. 이는 단순히 재미로 글만 써도 돈을 벌 가능성이 생긴다는 뜻이다. (애드센스를 달 수 없다면 아마 안했을 것이다.)
2. 두 번째는 개인 도메인 호스팅이 가능하다는 점이다. 사실 깃허브 블로그의 기본 주소는 **[사용자명].github.io**이다. 그런데 개인 도메인을 구매해서 호스팅을 한다면 **".com"**, **".co.kr"** 등의 주소로 운영이 가능하다. 이는 확장시 유리하다.
3. 세 번째는 네이버, 카카오 다음 등에 구애받지 않고 자유롭게 이용할 수 있다는 점이다. 기존에는 다른 ip주소로 접속, 잦은 글 수정 등 나는 분명 정직하게 한 것인데 로직상 문제가 되면 블로그가 나락으로 가는 문제가 발생했다. 나는 편히 글만 쓰고 싶은데 플랫폼 눈치를 봐야하는 것이 너무 싫었다.

위 3가지가 아무래도 가장 큰 이유들이고 그것을 해결할 수 있을 것 같은 플랫폼이 바로 Jekyll(지킬)과 깃허브를 이용한 블로그 운영이었다.

사실 아직 애드센스 승인도 안되었고 각 포털사에 노출도 안되고 있기 때문에 수익성을 보장할 수 없지만, 그래도 최종적으로 구글에 포스트를 노출시키는 것이 목표이므로 깃헙 블로그를 운영하는 것은 큰 매리트가 있다.

## 깃허브 블로그 시작하기 (Start GitHub Blog)
GitHub라고 해서 그렇게 어렵거나 특별하지는 않다. 깃허브는 프로젝트마다 저장소(레퍼지토리)를 생성할 수 있는데 이는 인터넷 상에 있는 내 USB라고 생각하면 쉽다.

인터넷에 있기 때문에 내 컴퓨터를 꺼 놓아도 USB에 있는 내용이 저장되어있고, 이를 인터넷 접속만 되면 확인할 수 있는 것이다. 즉, 깃허브를 서버로 하여 블로그를 운영하는 것이다.

사실 이번 기회에 깃허브를 알아둔다면, 코드는 물론이고 파일관리, 사진첩 관리 등도 쉽게할 수 있을 것이다. 이는 나중에 차차 자연스럽게 알게될 것이다.

### 1. 깃허브 가입
깃허브를 통해서 블로그를 운영할 것이기 때문에 당연히 깃허브 아이디가 필요하다. 없는 분들은 [GitHub 홈페이지](https://github.com/){: target="_blank"}로 이동해서 Sign up을 진행하고 오시면 된다.

{% include gallery id="gallery1" caption="깃허브 회원가입 하기" %}

이메일만 있으면 가입할 수 있는 추세이므로 쉽게 가입이 가능하다.

### 2. 새 저장소 생성
가입 후 로그인을 하면 우상단에 +버튼을 누르면 New repository로 새 저장소를 생성할 수 있다. 눌러서 새 저장소를 만들어주자.

{% include gallery id="gallery2" %}

이때 이름을 **[유저명].github.io**로 지어주어야 해당 주소로 접속했을 때 블로그 페이지가 뜨게 되니 사진을 참고해서 유의해서 설정하기 바란다.

일단 이름을 제외한 나머지 설정들은 위 이미지에 있는 대로 그대로 두고 생성하면 된다. 

이후에 생성이 되면 아직 저장소 할당이 안되어 있는데 이는 테마를 고르고 이어서 설명할 테니 일단 그대로 두고 다음으로 넘어가자.

### 3. 원하는 테마 고르기 (추천 테마)
내가 현재 쓰고 있는 테마는 minimal mistakes 테마로 가장 심플하고 좋다. 사실 더 멋있는 것도 많고 화려한 것도 있지만, 가볍고 빠른 것이 최고의 속도를 내고 수익도 좋다.

방문자는 페이지 로딩이 2~3초 이상만 소요되더라도 바로 뒤로가기 버튼을 누른다. 그러니 필요한 기능을 최소한으로 가진 테마를 고르는 것이 좋다.

{% include gallery id="gallery3" %}

- Jekyll 테마 모음 사이트
  1. <http://jekyllthemes.org/>{: target="_blank"}
  2. <http://themes.jekyllrc.org/>{: target="_blank"}
  3. <https://jekyllthemes.io/free>{: target="_blank"}
  4. <https://github.com/topics/jekyll-theme>{: target="_blank"}

사실 유료 테마도 많이 존재하지만, 무료 테마 라고 뒤쳐지지 않고 오히려 업데이트가 더 활발해서 무료 테마가 더 좋을 수 있다.

그런 점에서 인기가 많은 [minimal mistakes](https://github.com/mmistakes/minimal-mistakes){: target="_blank"} 테마를 추천한다. 이 테마는 많은 깃헙 블로거들이 사용중이기도 하다.

### 4. 고른 테마 가져오기 (clone)

테마를 골랐으면 아까 생성해둔 저장소 Quick setup 부분으로 다시 넘어가서 맨 아래 **Import code**를 눌러주자. 이는 고른 테마를 복사해오기 위함이다.

그리고 Your old repository's clone URL 부분에 복사한 테마의 github 주소를 붙여넣는다. 이 글은 minimal mistakes 테마를 추천하므로 이를 기본으로 사용하겠다.

{% include gallery id="gallery4" %}

주소를 붙여 넣었으면 Begin import 버튼을 눌러서 import를 시작하자. 이런식으로 여러 테마들을 자유 자제로 복사해서 쓸 수 있다. 아주 편리하지 않은가?

복사 시에는 몇 분 정도 소요될 수 있으니 다 복사가 될 때까지 기다리기 바란다.

### 5. _config.yml 알맞게 수정하기

복사가 완료되었다면 jekyll을 운영하는데 필요한 여러 파일들이 생성되어 있을 것이다. 우리는 _config.yml을 알맞게 수정해서 기본적인 블로그 모습을 보이도록 해볼 것이다.

{% include gallery id="gallery5" %}

_config.yml을 눌르면 해당 코드를 볼 수 있고 위에 연필 처럼 생긴 아이콘을 눌르면 직접 수정이 가능하다.

위 이미지 중 3번째 이미지를 참고해서 본인에게 알맞게 수정하면된다. 이때 url 부분은 해당 블로그 기반 주소가 될 부분이므로 [유저명].github.io 가 기본이지만, 만약 자신이 **구매한 도메인**을 사용하려면 해당 도멘인을 입력하면 된다.

참고로 해당 _config.yml 코드는 아래 github 저장소를 참고했다.

> [7271kim님의 github.io config yml](http://github.com/7271kim/7271kim.github.com/blob/master/_config.yml)

### 6. GitHub Pages 설정하기

자, 이제 마지막 단계다. 저장소 메뉴중에 Settings에 들어가서 깃허브 페이지 설정만 해주면 깃허브 블로그 개설이 완료된다.

{% include gallery id="gallery6" %}

Settings에 GitHub Pages란에 소스를 root로 설정하고 Save 한다. 만약 개인 도메인을 사용하고 싶다면 Custom domain에 설정하고 Save 하면된다. 하지 않으면 기본적으로 [유저명].github.io로 접속하면 접속이 가능하다.

{% include gallery id="gallery7" %}

## 간과된 것들
사실 위 내용을 진행하면 간단하게 블로그를 생성하고 접속이 가능하다. 하지만 깃허브 내에서 수정하는 불편함(이는 로컬에서 remote하는 방법으로 해결 가능)이 있다.

그리고 이제 블로그를 만들었으니 글을 쓰면 되겠다 라고 생각할 수 있지만 어딜 봐도 글 쓰기 부분이 없다. 포스팅을 하려면 _post 폴더를 생성하고 그 안에 markdown 파일을 생성해서 git commit & push를 해주어야 한다.

또 markdown으로 포스팅을 할 때 사진 첨부나 글 꾸미기 등이 기존 블로그 에디터 보다 훨신 직관성이 떨어져서 쉬운일이 아니다.

그래도 깃허브 블로그에 접속하는 것 까지는 완료했으므로, 여기까지 했을 때 재미가 있거나 흥미로웠다면 추가로 알아보면서 작업한다면 위에 있는 간과된 내용은 쉽게 해결이 가능하다.

하지만 어렵거나, 재미가 느껴지지 않는 분들이라면 깃허브 블로그를 정말 운영할 수 있을지 하고싶은지를 다시 생각해서 이후 방향을 잡기를 바란다.