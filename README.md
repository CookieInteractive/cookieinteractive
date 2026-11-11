# 쿠키인터랙티브 웹 페이지 운영용 파일 (2026-11-11)

법인 코드 ckii. 결정과 경위는 위키 `claude:projects:ckii-website:start`에 있습니다.
시안 2의 방향(결정 0010)에 영문을 더한 판입니다.

## 들어 있는 것

    docs/
      index.html              첫 화면
      q-flow/index.html       자체 제품 Q-Flow
      company/index.html      회사 소개 (개요, 사업 목적, 기술 역량, 수행 실적, 확인서, 공고 방법)
      notice/index.html       공고 (한국어만)
      en/index.html           영문 첫 화면
      en/q-flow/index.html    영문 Q-Flow
      en/company/index.html   영문 회사 소개
      assets/style.css        공통 스타일
      assets/headerbox-fea.svg   헤더박스 구조해석 개념도 (직접 그린 설명용 그림, 실제 해석 결과 아님)
      assets/mark.png, favicon.png   로고 심볼
      assets/fonts/           Pretendard 글꼴 (제작자 공식 배포 파일 그대로, SIL OFL 1.1, 라이선스 문서 포함)
      CNAME                   cookieinteractive.com
    tools/build_site.py       위 HTML 7개를 만드는 생성기 (머리와 바닥을 한 곳에서 관리)

외부 서버에서 불러오는 글꼴이나 스크립트는 없습니다.
영문 페이지의 공고 링크는 한국어 공고 페이지로 갑니다.

## 내용을 고칠 때

HTML을 직접 고쳐도 되고, `tools/build_site.py`의 문구를 고친 뒤 `python3 tools/build_site.py docs`로 다시 만들어도 됩니다.
직접 고친 뒤에 생성기를 돌리면 직접 고친 내용이 덮어쓰이니 한쪽 방법만 쓰세요.

## 확인할 것 (공개 전에 적은 목록)

- 문의 이메일 contact@cookieinteractive.com 은 사용 중이라고 확인받았습니다 (사용자, 2026-11-11)
- Q-Flow 페이지의 기능 서술(3단계, 하중조합 8가지, CalculiX, SCL 보고서, EPC 대상): 기존 초안 문구에서 옮겼습니다. 개발 중인 제품이므로 지금 기준으로 맞는지
- 솔루션 네 항목과 "설계와 해석을 아는 소프트웨어 회사" 세 항목의 문구
- 영문 번역
- 개념도를 실제 해석 결과 화면으로 바꿀지
- 대표자 이름은 싣기로 했습니다 (결정 0011). 영문 표기 Bongtae Jeon
- 소재지는 주소 이전 예정이라 시 단위까지만 적음

## 확인용 사이트

2026-11-11에 https://cookieinteractive.com 으로 공개했습니다. 공개 전 확인에 쓰던 https://seasaintfromsnowingsea.github.io/ 는 공개 뒤 비웠습니다 (결정 0012).
공개 전에 웹 화면으로 확인할 일이 있으면 `python3 tools/build_site.py <폴더> --staging`으로 만들어 그곳에 잠시 올립니다.
검색 제외 표시가 들어가고 CNAME을 넣지 않습니다. 확인이 끝나면 다시 비웁니다.
이 저장소의 docs/는 운영용입니다 (검색 제외 표시 없음, CNAME 포함).
