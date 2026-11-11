# 쿠키인터랙티브 웹 페이지 (ckii-website)

법인 사이트 cookieinteractive.com 의 소스입니다. 법인 코드는 `ckii` 입니다.
이 문서는 Claude Code가 작업을 이어받을 때 읽는 안내입니다. 2026-11-11 기준입니다.

## 구조

    docs/                 배포 대상. GitHub Pages가 이 폴더를 서비스합니다.
      index.html, q-flow/, company/, notice/     한국어 4쪽
      en/index.html, en/q-flow/, en/company/     영문 3쪽 (공고는 한국어만)
      assets/style.css                           공통 스타일
      assets/headerbox-fea.svg                   헤더박스 구조해석 개념도 (직접 그린 설명용 그림)
      assets/fonts/                              Pretendard 공식 배포 파일 (SIL OFL 1.1)
      CNAME                                      cookieinteractive.com
    tools/build_site.py   docs/ 의 HTML 7개를 만드는 생성기. 머리, 바닥, 문구가 여기 있습니다.
    README.md             사람을 위한 안내

## 저장소와 주소

| 용도 | 저장소 | 주소 |
|---|---|---|
| 운영 (소스의 원본) | `cookieinteractive/cookieinteractive` 의 `main`, 배포는 `docs/` | https://cookieinteractive.com |
| 확인용 | `seasaintfromsnowingsea/seasaintfromsnowingsea.github.io` 의 `main` 루트 | https://seasaintfromsnowingsea.github.io/ (평소에는 비워 둠) |

2026-11-11 에 새 사이트를 운영 저장소 `main` 에 합쳐 공개했습니다.
소스의 원본은 운영 저장소입니다. 인계에 썼던 확인용 저장소의 `source` 브랜치는 지웠습니다.
확인용 주소는 공개 뒤 비웠습니다 (2026-11-11). 지금 확인용 저장소 `main` 에는 `.nojekyll`, `logo.png`, `trans01.png` 만 있습니다.
공개 전에 웹 화면으로 확인할 일이 있을 때만 올리고, 확인이 끝나면 다시 비웁니다.

공개 뒤 확인한 것 (2026-11-11): Pages 배포 소스는 `main` 의 `docs/`, HTTPS 강제가 켜져 있음,
http 와 www 주소가 https://cookieinteractive.com 으로 넘어감.

## 만드는 명령

    # 운영용: docs/ 의 HTML 을 다시 만듭니다
    python3 tools/build_site.py docs

    # 확인용: 검색 제외 표시(noindex)가 들어간 HTML 을 다른 폴더에 만듭니다
    python3 tools/build_site.py /tmp/staging --staging

문구는 `tools/build_site.py` 에서 고치고 다시 만듭니다. HTML 을 직접 고치면 다음에 생성기를 돌릴 때 덮어쓰입니다.

## 올리는 절차

운영 저장소:

1. 운영 저장소를 받아 새 브랜치를 만듭니다. `main` 에 바로 올리지 않습니다.
2. `tools/build_site.py` 를 고치고 `python3 tools/build_site.py docs` 로 다시 만듭니다. `docs/CNAME` 은 그대로 둡니다.
3. 브랜치를 올리고 사용자에게 알립니다.
4. 사용자가 승인한 뒤에만 `main` 에 합칩니다. 합치면 1분쯤 뒤 공개됩니다.
5. 공개 뒤 바뀐 페이지가 https://cookieinteractive.com 에서 보이는지 확인하고, 다 쓴 브랜치는 지웁니다.

확인용 저장소 (`main`), 웹 화면으로 먼저 확인할 때만:

1. `--staging` 으로 만든 HTML 과 `docs/assets/` 를 저장소 루트에 둡니다.
2. `CNAME` 을 넣지 않습니다. 넣으면 운영 도메인과 충돌합니다.
3. 루트의 `.nojekyll`, `logo.png`, `trans01.png` 는 그대로 둡니다.
4. 확인이 끝나면 올린 HTML 과 `assets/` 를 다시 지웁니다. 위 3번의 파일은 남깁니다.

## 지킬 것

- 회사에 관한 사실(상호, 설립일, 사업자등록번호, 실적, 확인서, 대표자)은 사용자가 관리하는
  법인 정보 저장소(corp-info)의 값만 씁니다. 근거 없는 숫자, 고객사, 사례를 만들어 넣지 않습니다.
- 실적에는 고객사 이름을 적지 않고 업종만 적습니다. 근무지처럼 고객을 짐작하게 하는 표현도 뺍니다.
- Q-Flow 는 "개발 중"으로 적습니다. "데모 요청" 같은 표현을 쓰지 않습니다.
- 주어는 회사입니다. 개인의 경험이나 경력으로 읽히는 표현을 쓰지 않습니다.
- 개념도에는 설명용 그림이라는 표기를 유지합니다. 실제 해석 결과처럼 보이게 하지 않습니다.
- 한국어를 고치면 영문도 함께 고칩니다.
- 공고 영역은 첫 화면에서 바로 찾을 수 있어야 합니다. 없애거나 아래로 내리지 않습니다.
- 대표 주소는 https://cookieinteractive.com (www 없음) 입니다. canonical 과 hreflang 을 여기에 맞춥니다.
- 글꼴 파일은 제작자가 배포한 그대로 씁니다. 직접 줄이거나 고치지 않습니다 (글꼴 이름이 예약되어 있습니다).
- 외부 서버의 글꼴이나 스크립트를 불러오지 않습니다.
- 운영 `main` 에 반영하기, 공고 올리기처럼 공개되는 변경은 사용자 승인을 받고 합니다.

## 남은 일 (2026-11-11 기준)

1. Q-Flow 페이지의 기능 서술을 사용자가 확인 (지금은 그대로 두기로 함)
2. 소재지는 시 단위까지만 적혀 있음. 주소가 확정되면 사용자가 알려 주는 값으로 고치기

끝낸 일 (2026-11-11): 확인용 주소에서 내용 확인, 운영 저장소 `main` 에 합쳐 공개,
Pages 설정과 주소 넘어감 확인, 확인용 주소 비우기, `source` 브랜치 지우기.

## 결정과 기록

결정 기록(0001~0013), 작업 일지, 운영 절차는 사용자의 위키 `claude:projects:ckii-website:start` 에 있습니다.
위키를 읽을 수 없으면 사용자에게 해당 내용을 요청합니다. 이 저장소는 공개 저장소이므로
회사 내부 사정이나 결정의 배경을 여기에 옮겨 적지 않습니다.
