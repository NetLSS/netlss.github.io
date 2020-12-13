---
title: "깃허브(GitHub) 블로그 폰트 바꾸는법 (otf, woff 파일 사용)"
excerpt: "깃허브 블로그 폰트 바꾸기 otf, woff, ttf 파일을 사용해서 리디바탕 및 웹폰트를 jekyll minimal mistakes 테마에 적용하는법"

categories:
    - Blog
tags:
    - Blog
last_modified_at: 2020-12-13T23:13:02+09:00
---

## 1. 깃허브 블로그 폰트 바꾸는 방법 소개
깃허브에서 jekyll을 사용해서 블로그를 개설하면 커스터마이징 할 수 있는 것들이 아주 많다. 자기멋대로 수정이 가능하다는 말이다.

필자의 블로그는 jekyll 테마중에서 가장 인기가 많은것 중에 하나인 minimal mistakes이며 대부분 이 테마로 시작하는 분들이 많을 것이다.

![깃허브 블로그에 리디바탕 폰트 적용한 모습](/assets/images/002-change-github-blog-font/Ridibatang_in_github_blog.png){: .center}

그래서 이 테마를 기준으로 설명하겠지만, 다른 지킬 테마를 쓰더라도 사실 특정 폴더내 파일을 수정하는 것이라서 별 다를 것이 없을것이기 때문에 다른 테마를 쓰더라도 이 글이 도움이 될 것이다.

### 1.1. 리디바탕체?

리디바탕체는 전자책(e-book)을 읽을 때 가시성을 좀더 좋게하여 선명하고 긴 글도 잘읽을 수 있도록 고안된 폰트다. 블로그도 책에 비유하면 몇 페이지는 안될지라도 가시성이 중요하기 때문에 이 폰트를 선택했다.

<center>
    <table style="border-collapse: collapse; width: 100%; margin:auto; text-align: center;" border="0">
        <tbody>
            <tr>
                <td style="width: 50%;"><img src="/assets/images/clipboard/%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%20%EC%86%8C%EA%B0%9C.png" alt="%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%20%EC%86%8C%EA%B0%9C"></td>
                <td style="width: 50%;"><img src="/assets/images/clipboard/%EA%B8%B4%EB%AC%B8%EC%9E%A5%EB%8F%84%20%EB%8D%94%20%EC%9E%98%EC%9D%BD%ED%9E%88%EB%8A%94%20%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%EC%B2%B4.png" alt="%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%20%EC%86%8C%EA%B0%9C"></td>
            </tr>
        </tbody>
    </table>
</center>

블로그를 운영한 경력이 꽤 되는 분들은 아마 다 알고있을 폰트라고 생각한다. 필자도 티스토리의 모든 블로그에 리디바탕 폰트를 적용하고 있고 확실히 가시성이 좋아졌다.

이 글도 사실 리디바탕체를 깃허브 블로그에 폰트로 적용할 수 있을까 하는 생각으로 시작해서 적용을 한 후 탄생하게 된 글이다. 구글링을 해봐도 웹폰트 적용하는 방법만 있고 폰트파일은 사용하는 것이 없어서도 이유 중 하나다.

## 2. 깃허브 블로그에 리디바탕 폰트 적용하기
### 2.1. 폰트 파일 구하기 (otf, woff 파일)

리디바탕체는 무료로 공개되어있어서 구글에 리디바탕만 검색해도 아래와 같이 공식 홈페이지에 들어가면 바로 다운로드가 가능하다. 그런데 기본은 otf라서 용량이 웹에서 로드해서 사용하기에는 클 수 있다.

<center>
    <table style="border-collapse: collapse; width: 100%; margin:auto; text-align: center;" border="0">
        <tbody>
            <tr>
                <td style="width: 50%;"><img src="/assets/images/clipboard/%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%EC%B2%B4-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.png" alt="%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%EC%B2%B4-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C"></td>
                <td style="width: 50%;"><img src="/assets/images/clipboard/%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%EC%B2%B4-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C2.png" alt="%EB%A6%AC%EB%94%94%EB%B0%94%ED%83%95%EC%B2%B4-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C2"></td>
            </tr>
        </tbody>
    </table>
</center>

그래서 웹폰트 형식인 woff 파일 형식으로 크기를 줄여놓은 것을 사용하는 것이 좋다. 리디바탕체를 적용하실 분은 아래에 첨부를 해 두겠으니 다운로드해서 사용하면 되겠습니다.

> [리디바탕체 웹폰트 다운로드](https://noonnu.cc/font_page/324)

### 2.2. 폰트파일을 assets 폴더로 복사
폰트파일(.otf, .woff)을 구했다면 /assets/fonts 경로로 복사해준다. (사실 아무대나 해도 되는데 assets로 통일하는 것이 좋다.)

![font-to-assets](/assets/images/clipboard/font-to-assets.png){: .center}

### 2.3. css 파일 수정 (assets/css)
다음으로는 jekyll에서 우리가 적용해줄 css 코드를 설정해주어야 한다. 경로는 assets/css/main.scss 내부에 아래 코드를 추가하면된다.
```css
@font-face {
    font-family: 'RIDIBatang';
    src: url('/assets/fonts/RIDIBatang.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
```
![css-file-edit-main-scss](/assets/images/clipboard/css-file-edit-main-scss.png)  

### 2.4. variables.scss 에서 폰트 적용
다음은 _sass폴더의 minimal-mistakes/_variables.scss 파일을 수정해야한다. 15라인 쯤에 system typefaces 주석 아래 부분 sans-serif란을 수정하면되는데, 자기 자신의 폰트명을 입력해준다.
```css
/* system typefaces */
$serif: Georgia, Times, serif !default;
$sans-serif: "RIDIBatang", -apple-system, BlinkMacSystemFont, "Roboto", "Segoe UI",
  "Helvetica Neue", "Lucida Grande", Arial, sans-serif !default;
$monospace: Monaco, Consolas, "Lucida Console", monospace !default;
```
![variables-scss-font](/assets/images/clipboard/variables-scss-font.png)  

### 2.5. commit & push 후 확인
이후 커밋 & 푸시 후 1~2분 정도 뒤에 확인해보면 정상적으로 폰트가 적용된 것을 확인할 수 있을 것이다.

![%EA%B9%83%ED%97%88%EB%B8%8C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%ED%8F%B0%ED%8A%B8%EB%B3%80%EA%B2%BD-%EC%A0%81%EC%9A%A9%EB%AA%A8%EC%8A%B5](/assets/images/clipboard/%EA%B9%83%ED%97%88%EB%B8%8C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%ED%8F%B0%ED%8A%B8%EB%B3%80%EA%B2%BD-%EC%A0%81%EC%9A%A9%EB%AA%A8%EC%8A%B5.png)

이로써 깃허브 블로그 폰트 변경을 성공적으로 마쳤다. 생각보다 너무 간단하지 않은가? 이것은 사실 시작에 불과하다. 이보다 더 많은 커스터마이징할 것이 남아있는데, 이건 앞으로 차차 올리도록 하겠다.