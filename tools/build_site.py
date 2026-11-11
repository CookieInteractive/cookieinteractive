#!/usr/bin/env python3
"""쿠키인터랙티브 사이트 생성기. 머리와 바닥을 한 곳에서 관리하고 한국어·영문 정적 HTML을 만듭니다.
사용: python3 build_site.py <docs 폴더>"""
import sys, os

OUT = sys.argv[1]
STAGING = "--staging" in sys.argv   # 확인용 사이트: 검색 제외 표시를 넣습니다
MAIL = "contact@cookieinteractive.com"
BASE = "https://cookieinteractive.com"

T = {
    "ko": dict(
        skip="본문으로 건너뛰기", brand="쿠키인터랙티브", nav_label="주 메뉴",
        nav=["솔루션", "Q-Flow", "회사 소개", "공고"], contact="문의하기",
        other_lang="English", other_code="en",
        cta_h="자동화할 해석 작업이나 업무가 있다면 알려 주세요",
        cta_p="외주 개발과 Q-Flow에 관한 문의를 이메일로 받습니다.",
        who_name="쿠키인터랙티브 주식회사",
        who_lines=['<span lang="en">Cookie Interactive Inc.</span>', "대표 전봉태", "사업자등록번호 620-87-00732", "경상남도 창원시"],
        f_sol="솔루션", f_sols=["엔지니어링 해석 자동화", "업무 자동화", "맞춤형 소프트웨어 개발", "시스템 통합과 컨설팅"],
        f_prod="제품", f_co="회사", f_co_links=["회사 소개", "수행 실적", "공고"],
        fig_alt="노즐 두 개가 달린 헤더박스를 요소망으로 나누고 응력 크기를 색으로 나타낸 그림",
        fig_cap="헤더박스 구조해석 개념도 (설명용 그림)", low="응력 낮음", high="높음",
    ),
    "en": dict(
        skip="Skip to content", brand="Cookie Interactive", nav_label="Main",
        nav=["Solutions", "Q-Flow", "Company", "Notices"], contact="Contact us",
        other_lang="한국어", other_code="ko",
        cta_h="Tell us about the analysis or office work you want to automate",
        cta_p="We take inquiries about contract development and Q-Flow by email.",
        who_name="Cookie Interactive Inc.",
        who_lines=['<span lang="ko">쿠키인터랙티브 주식회사</span>', "Representative: Bongtae Jeon", "Business registration no. 620-87-00732", "Changwon, Gyeongsangnam-do, Republic of Korea"],
        f_sol="Solutions", f_sols=["Engineering analysis automation", "Work automation", "Custom software development", "System integration and consulting"],
        f_prod="Product", f_co="Company", f_co_links=["Company", "Track record", "Notices (in Korean)"],
        fig_alt="A header box with two nozzles divided into a mesh, with stress levels shown in color",
        fig_cap="Header box structural analysis, conceptual illustration", low="Stress low", high="high",
    ),
}


def head(lang, title, desc, path, root, current, alt_path):
    """path: 이 페이지의 주소. root: 사이트 맨 위까지의 상대 경로. alt_path: 다른 언어의 같은 페이지 주소(없으면 그 언어의 첫 화면)."""
    t = T[lang]
    home = root if lang == "ko" else root + "en/"
    ko_path = path if lang == "ko" else alt_path
    en_path = alt_path if lang == "ko" else path
    alt_href = root + alt_path.lstrip("/")
    notice = root + "notice/"
    def cur(key):
        return ' aria-current="page"' if key == current else ''
    hreflang = ""
    if current != "notice":
        hreflang = f'\n<link rel="alternate" hreflang="ko" href="{BASE}{ko_path}">\n<link rel="alternate" hreflang="en" href="{BASE}{en_path}">'
    small = '<small lang="en">Cookie Interactive Inc.</small>' if lang == "ko" else '<small lang="ko">쿠키인터랙티브 주식회사</small>'
    notice_attr = '' if lang == "ko" else ' hreflang="ko"'
    robots = '\n<meta name="robots" content="noindex, nofollow">' if STAGING else ''
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="canonical" href="{BASE}{path}">{hreflang}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<link rel="icon" type="image/png" href="{root}assets/favicon.png">
<link rel="stylesheet" href="{root}assets/fonts/pretendardvariable-dynamic-subset.css">
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{home or './'}">
      <img src="{root}assets/mark.png" alt="" width="38" height="38">
      <span>{t['brand']}{small}</span>
    </a>
    <nav class="site-nav" aria-label="{t['nav_label']}">
      <ul>
        <li><a href="{home}#solutions">{t['nav'][0]}</a></li>
        <li><a href="{home}q-flow/"{cur('q-flow')}>{t['nav'][1]}</a></li>
        <li><a href="{home}company/"{cur('company')}>{t['nav'][2]}</a></li>
        <li><a href="{notice}"{cur('notice')}{notice_attr}>{t['nav'][3]}</a></li>
        <li class="lang"><a href="{alt_href or './'}" lang="{t['other_code']}" hreflang="{t['other_code']}">{t['other_lang']}</a></li>
        <li><a class="btn btn-primary" href="mailto:{MAIL}">{t['contact']}</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="main">
"""


def foot(lang, root):
    t = T[lang]
    home = root if lang == "ko" else root + "en/"
    notice = root + "notice/"
    who = "<br>\n          ".join(t["who_lines"])
    sols = "\n".join(f'          <li><a href="{home}#solutions">{s}</a></li>' for s in t["f_sols"])
    return f"""
  <section class="cta" aria-labelledby="cta-title">
    <div class="wrap">
      <div>
        <h2 id="cta-title">{t['cta_h']}</h2>
        <p>{t['cta_p']}</p>
      </div>
      <a class="btn btn-light" href="mailto:{MAIL}">{MAIL}</a>
    </div>
  </section>

</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="cols">
      <div class="who">
        <strong>{t['who_name']}</strong>
        <p>
          {who}<br>
          <a href="mailto:{MAIL}">{MAIL}</a>
        </p>
      </div>
      <div>
        <h2>{t['f_sol']}</h2>
        <ul>
{sols}
        </ul>
      </div>
      <div>
        <h2>{t['f_prod']}</h2>
        <ul>
          <li><a href="{home}q-flow/">Q-Flow</a></li>
        </ul>
      </div>
      <div>
        <h2>{t['f_co']}</h2>
        <ul>
          <li><a href="{home}company/">{t['f_co_links'][0]}</a></li>
          <li><a href="{home}company/#records">{t['f_co_links'][1]}</a></li>
          <li><a href="{notice}">{t['f_co_links'][2]}</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <p lang="en">© 2026 Cookie Interactive Inc.</p>
    </div>
  </div>
</footer>

</body>
</html>
"""


def figure(lang, root):
    t = T[lang]
    return f"""<figure class="figure">
        <img src="{root}assets/headerbox-fea.svg" width="2676" height="2061" alt="{t['fig_alt']}">
        <figcaption>
          <span>{t['fig_cap']}</span>
          <span class="legend">{t['low']} <i aria-hidden="true"></i> {t['high']}</span>
        </figcaption>
      </figure>"""


def steps(items):
    return "\n".join(f"""        <li>
          <h3>{h}</h3>
          <p>{p}</p>
        </li>""" for h, p in items)


def rows(items):
    return "\n".join(f'            <tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in items)


pages = {}

# ═════════════════════════ 한국어 ═════════════════════════

pages["index.html"] = head("ko",
    "쿠키인터랙티브 주식회사 | 엔지니어링 해석과 업무 자동화 소프트웨어",
    "쿠키인터랙티브는 구조해석(FEA) 자동화와 업무 자동화, 맞춤형 소프트웨어 개발을 하는 경남 창원의 소프트웨어 회사입니다.",
    "/", "", "home", "/en/") + f"""
  <section class="hero">
    <div class="wrap">
      <div>
        <h1>반복되는 엔지니어링 해석과 업무를 소프트웨어로 자동화합니다</h1>
        <p class="lead">쿠키인터랙티브는 구조해석(FEA) 자동화와 업무 자동화, 맞춤형 소프트웨어 개발을 하는 회사입니다. 설계와 해석 업무에 맞춘 소프트웨어로 작업 시간과 비용을 줄입니다.</p>
        <div class="actions">
          <a class="btn btn-light" href="mailto:{MAIL}">프로젝트 문의</a>
          <a class="btn btn-ghost" href="q-flow/">Q-Flow 알아보기</a>
        </div>
      </div>
      {figure("ko", "")}
    </div>
  </section>

  <section class="facts" aria-label="회사 기본 정보">
    <div class="wrap">
      <dl>
        <div><dt>설립</dt><dd>2017년</dd></div>
        <div><dt>소재지</dt><dd>경남 창원</dd></div>
        <div><dt>기업 규모</dt><dd>소기업 (중소기업 확인서)</dd></div>
        <div><dt>사업자등록번호</dt><dd>620-87-00732</dd></div>
      </dl>
    </div>
  </section>

  <section class="notice-strip" id="notice" aria-labelledby="notice-title">
    <div class="wrap">
      <h2 id="notice-title">공고</h2>
      <p>게시 중인 공고가 없습니다.</p>
      <a href="notice/">공고 전체 보기</a>
    </div>
  </section>

  <section class="band" id="solutions">
    <div class="wrap">
      <div class="band-head">
        <h2>솔루션</h2>
        <p>사람이 손으로 되풀이하던 해석과 업무를 소프트웨어가 처리하도록 만듭니다.</p>
      </div>
      <div class="grid-2">
        <article class="cell">
          <h3>엔지니어링 해석 자동화</h3>
          <p>3D 모델 생성부터 유한요소해석, 보고서 작성까지 이어지는 작업을 하나의 흐름으로 자동화합니다. 하중조합을 하나씩 돌리고 결과를 손으로 옮기던 일을 줄입니다.</p>
        </article>
        <article class="cell">
          <h3>업무 자동화</h3>
          <p>엑셀, 문서, 웹 시스템을 오가는 반복 업무를 Python 기반 자동화(RPA)로 바꿉니다.</p>
        </article>
        <article class="cell">
          <h3>맞춤형 소프트웨어 개발</h3>
          <p>사내 시스템, 데이터 파이프라인, 업무 도구를 요구사항에 맞춰 개발하고 공급합니다.</p>
        </article>
        <article class="cell">
          <h3>시스템 통합과 컨설팅</h3>
          <p>컴퓨터시스템 통합에 관한 자문과 구축, 소프트웨어 개발과 자동화에 관한 교육·컨설팅을 제공합니다.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="band mist" id="q-flow">
    <div class="wrap split">
      <div>
        <p class="status-line"><span class="status">개발 중</span></p>
        <h2>자체 제품 Q-Flow</h2>
        <p class="lead">API 661 공랭식 열교환기(ACHE) 헤더박스의 구조해석을 형상 입력부터 보고서까지 자동화하는 엔지니어링 소프트웨어입니다.</p>
        <a class="btn btn-line" href="q-flow/">Q-Flow 자세히 보기</a>
      </div>
      <ol class="steps">
{steps([("3D 모델링", "헤더박스와 노즐의 치수를 입력받아 해석용 3D 형상을 만듭니다."),
        ("유한요소해석", "해석 입력 파일을 만들고 솔버를 실행해 하중조합을 모두 계산합니다."),
        ("보고서 생성", "해석 결과를 표준 양식의 보고서로 정리합니다.")])}
      </ol>
    </div>
  </section>

  <section class="band" id="why">
    <div class="wrap">
      <div class="band-head">
        <h2>설계와 해석을 아는 소프트웨어 회사</h2>
        <p>요구사항을 엔지니어의 언어로 듣고 소프트웨어로 옮깁니다.</p>
      </div>
      <div class="grid-3">
        <div class="point">
          <h3>엔지니어링 실무에서 출발합니다</h3>
          <p>3D CAD 모델링과 구조해석(FEA)의 절차, 판정 기준, 보고서 양식에 맞춰 소프트웨어를 설계합니다. 결과물이 엔지니어의 검토 과정에 그대로 쓰이도록 만듭니다.</p>
        </div>
        <div class="point">
          <h3>Python으로 처음부터 끝까지 연결합니다</h3>
          <p>모델 생성, 해석 실행, 결과 정리, 문서 작성을 Python으로 이어 붙여 사람이 개입하는 단계를 줄입니다.</p>
        </div>
        <div class="point">
          <h3>대기업 현장에서 수행했습니다</h3>
          <p>2023년부터 국내 대기업(전자 제조) 현장에서 소프트웨어 개발 프로젝트를 수행해 왔습니다.</p>
        </div>
      </div>
    </div>
  </section>
""" + foot("ko", "")

pages["q-flow/index.html"] = head("ko",
    "Q-Flow | 쿠키인터랙티브 주식회사",
    "Q-Flow는 API 661 공랭식 열교환기 헤더박스의 3D 모델링, 유한요소해석, 보고서 작성을 자동화하는 엔지니어링 소프트웨어입니다. 현재 개발 중입니다.",
    "/q-flow/", "../", "q-flow", "/en/q-flow/") + f"""
  <section class="hero">
    <div class="wrap">
      <div>
        <p class="status-line"><span class="status">개발 중</span></p>
        <h1>Q-Flow</h1>
        <p class="lead">API 661 공랭식 열교환기(ACHE) 헤더박스의 구조해석을 형상 입력부터 보고서까지 자동화하는 엔지니어링 소프트웨어입니다.</p>
        <div class="actions">
          <a class="btn btn-light" href="mailto:{MAIL}">제품 문의</a>
        </div>
      </div>
      {figure("ko", "../")}
    </div>
  </section>

  <section class="band">
    <div class="wrap split">
      <div>
        <h2>손으로 하던 해석 절차를 하나의 흐름으로</h2>
        <p class="lead">엔지니어가 요소망을 다듬고 하중조합을 하나씩 돌리던 작업을 자동화된 절차로 바꿉니다. 시간과 비용 때문에 생략하기 쉬운 하중조합까지 같은 절차로 모두 계산합니다.</p>
      </div>
      <ol class="steps">
{steps([("3D 모델링", "헤더박스와 노즐의 형상을 입력받아 해석용 3D 형상을 자동으로 만듭니다."),
        ("유한요소해석", "Python으로 해석 입력 파일을 만들고 CalculiX 솔버로 실행해 하중조합을 모두 계산합니다."),
        ("보고서 생성", "SCL(Stress Classification Line) 결과를 포함한 표준 양식의 해석 보고서를 작성합니다.")])}
      </ol>
    </div>
  </section>

  <section class="band mist">
    <div class="wrap split">
      <div>
        <h2>기본 하중조합 8가지</h2>
        <p class="lead">최대허용사용압력(MAWP)에 풍하중과 지진하중을 방향별로 조합한 8가지를 기본으로 계산합니다.</p>
      </div>
      <table class="table">
        <thead>
          <tr><th scope="col">하중</th><th scope="col">방향</th></tr>
        </thead>
        <tbody>
{rows([("MAWP + 풍하중", "+X, −X, +Y, −Y"), ("MAWP + 지진하중", "+X, −X, +Y, −Y")])}
        </tbody>
      </table>
    </div>
  </section>

  <section class="band">
    <div class="wrap split">
      <div>
        <h2>제품 개요</h2>
        <p class="lead">여러 제작사의 도면을 검토하는 EPC 엔지니어링팀이 쓰기에 맞도록 만들고 있습니다.</p>
      </div>
      <div>
        <table class="table">
          <tbody>
{rows([("대상 설비", "API 661 공랭식 열교환기 (ACHE)"), ("해석 범위", "헤더박스와 노즐"), ("솔버", "CalculiX"),
       ("자동화", "Python"), ("결과물", "SCL 결과를 포함한 해석 보고서"), ("상태", "개발 중 (출시 전)")])}
          </tbody>
        </table>
        <p class="note">개발 중인 제품이어서 내용이 바뀔 수 있습니다.</p>
      </div>
    </div>
  </section>
""" + foot("ko", "../")

pages["company/index.html"] = head("ko",
    "회사 소개 | 쿠키인터랙티브 주식회사",
    "쿠키인터랙티브 주식회사의 회사 개요, 사업 목적, 수행 실적, 확인서를 안내합니다.",
    "/company/", "../", "company", "/en/company/") + f"""
  <section class="page-head">
    <div class="wrap">
      <h1>회사 소개</h1>
      <p>쿠키인터랙티브 주식회사는 2017년에 설립한 경남 창원의 소프트웨어 회사입니다. 엔지니어링 해석과 업무의 반복 작업을 소프트웨어로 자동화합니다.</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap stack">

      <div class="split" id="profile">
        <h2 class="section-title">회사 개요</h2>
        <table class="table">
          <tbody>
{rows([("상호", '쿠키인터랙티브 주식회사<span class="sub" lang="en">Cookie Interactive Inc.</span>'), ("대표자", "전봉태"), ("설립", "2017년 5월 26일"),
       ("소재지", "경상남도 창원시"), ("사업자등록번호", "620-87-00732"), ("기업 규모", '소기업<span class="sub">중소기업 확인서 보유</span>')])}
          </tbody>
        </table>
      </div>

      <div class="split" id="business">
        <div>
          <h2 class="section-title">사업 목적</h2>
          <p class="note tight">정관에 정한 사업 목적 가운데 주요 항목입니다.</p>
        </div>
        <ul class="plain-list">
          <li>온라인, 모바일, 컴퓨터 프로그램의 개발, 임대 및 공급업</li>
          <li>시스템 및 응용 소프트웨어 개발 및 공급업</li>
          <li>컴퓨터시스템 통합 자문 및 구축 서비스업</li>
          <li>정보처리 및 기타 컴퓨터 운용 관련업</li>
          <li>데이터베이스 및 온라인 정보 제공업</li>
          <li>기타 엔지니어링 서비스업</li>
          <li>교육 및 컨설팅업</li>
        </ul>
      </div>

      <div class="split" id="capabilities">
        <h2 class="section-title">기술 역량</h2>
        <table class="table">
          <thead>
            <tr><th scope="col">영역</th><th scope="col">다루는 기술</th></tr>
          </thead>
          <tbody>
{rows([("소프트웨어 개발", "Python"), ("업무 자동화", "RPA, Python, AutoHotKey"), ("설계", "3D CAD (Inventor, CATIA)"), ("구조해석", "유한요소해석 (Ansys, CalculiX)")])}
          </tbody>
        </table>
      </div>

      <div class="split" id="records">
        <div>
          <h2 class="section-title">수행 실적</h2>
          <p class="note tight">고객사 이름은 적지 않았습니다.</p>
        </div>
        <table class="table wide">
          <thead>
            <tr><th scope="col">기간</th><th scope="col">내용</th><th scope="col">기술</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">2024년 1월 – 2026년 11월</th><td>국내 대기업(전자 제조) 현장 상주 소프트웨어 개발</td><td>Python</td></tr>
            <tr><th scope="row">2023년 3월 – 2023년 10월</th><td>국내 대기업(전자 제조) 현장 상주 소프트웨어 개발</td><td>Python</td></tr>
          </tbody>
        </table>
      </div>

      <div class="split" id="certificates">
        <h2 class="section-title">확인서</h2>
        <table class="table wide">
          <thead>
            <tr><th scope="col">이름</th><th scope="col">내용</th><th scope="col">발급</th><th scope="col">유효기간</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">중소기업 확인서</th><td>소기업(소상공인)</td><td>중소벤처기업부</td><td class="nowrap">2026-04-01 ~ 2027-03-31</td></tr>
          </tbody>
        </table>
      </div>

      <div class="split" id="notice-method">
        <h2 class="section-title">공고 방법</h2>
        <div class="prose">
          <p>쿠키인터랙티브 주식회사의 공고는 정관에 따라 이 홈페이지에 게재합니다. 전산장애나 그 밖의 부득이한 사유로 홈페이지에 게재할 수 없을 때에는 경남도민일보에 게재합니다.</p>
          <p><a href="../notice/">공고 보기</a></p>
        </div>
      </div>

    </div>
  </section>
""" + foot("ko", "../")

pages["notice/index.html"] = head("ko",
    "공고 | 쿠키인터랙티브 주식회사",
    "쿠키인터랙티브 주식회사의 공고를 게재하는 곳입니다.",
    "/notice/", "../", "notice", "/en/") + """
  <section class="page-head">
    <div class="wrap">
      <h1>공고</h1>
      <p>쿠키인터랙티브 주식회사의 공고는 정관에 따라 이 홈페이지에 게재합니다. 전산장애나 그 밖의 부득이한 사유로 홈페이지에 게재할 수 없을 때에는 경남도민일보에 게재합니다.</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap stack">

      <div class="split">
        <h2 class="section-title">게시 중인 공고</h2>
        <ul class="notice-list">
          <li><span class="empty">게시 중인 공고가 없습니다.</span></li>
          <!--
            공고를 올릴 때: 위의 "게시 중인 공고가 없습니다" 줄을 지우고 아래 형식으로 한 줄씩 추가합니다.
            최신 공고를 맨 위에 둡니다. 첫 화면(index.html)과 영문 첫 화면(en/index.html)의 공고 줄도 함께 고칩니다.

            <li>
              <a href="2026-12-01-notice.html">공고 제목</a>
              <time datetime="2026-12-01">2026-12-01 게시</time>
            </li>
          -->
        </ul>
      </div>

      <div class="split">
        <h2 class="section-title">게시 기간이 지난 공고</h2>
        <ul class="notice-list">
          <li><span class="empty">아직 없습니다.</span></li>
        </ul>
      </div>

    </div>
  </section>
""" + foot("ko", "../")

# ═════════════════════════ English ═════════════════════════

pages["en/index.html"] = head("en",
    "Cookie Interactive Inc. | Software for engineering analysis and work automation",
    "Cookie Interactive is a software company in Changwon, South Korea that develops FEA automation, work automation, and custom software.",
    "/en/", "../", "home", "/") + f"""
  <section class="hero">
    <div class="wrap">
      <div>
        <h1>We automate repetitive engineering analysis and office work with software</h1>
        <p class="lead">Cookie Interactive develops FEA automation, work automation, and custom software. Software built around design and analysis work cuts working time and cost.</p>
        <div class="actions">
          <a class="btn btn-light" href="mailto:{MAIL}">Discuss a project</a>
          <a class="btn btn-ghost" href="q-flow/">About Q-Flow</a>
        </div>
      </div>
      {figure("en", "../")}
    </div>
  </section>

  <section class="facts" aria-label="Company facts">
    <div class="wrap">
      <dl>
        <div><dt>Established</dt><dd>2017</dd></div>
        <div><dt>Location</dt><dd>Changwon, South Korea</dd></div>
        <div><dt>Company size</dt><dd>Small enterprise (SME certified)</dd></div>
        <div><dt>Business registration no.</dt><dd>620-87-00732</dd></div>
      </dl>
    </div>
  </section>

  <section class="notice-strip" id="notice" aria-labelledby="notice-title">
    <div class="wrap">
      <h2 id="notice-title">Notices</h2>
      <p>There are no notices at the moment.</p>
      <a href="../notice/" hreflang="ko">View all notices (in Korean)</a>
    </div>
  </section>

  <section class="band" id="solutions">
    <div class="wrap">
      <div class="band-head">
        <h2>Solutions</h2>
        <p>We make software do the analysis and office work that people used to repeat by hand.</p>
      </div>
      <div class="grid-2">
        <article class="cell">
          <h3>Engineering analysis automation</h3>
          <p>We automate the work that runs from 3D model generation through finite element analysis to report writing as a single flow. It reduces the work of running load combinations one at a time and copying results by hand.</p>
        </article>
        <article class="cell">
          <h3>Work automation</h3>
          <p>We replace repetitive tasks that move between spreadsheets, documents, and web systems with Python-based automation (RPA).</p>
        </article>
        <article class="cell">
          <h3>Custom software development</h3>
          <p>We develop and supply in-house systems, data pipelines, and work tools built to your requirements.</p>
        </article>
        <article class="cell">
          <h3>System integration and consulting</h3>
          <p>We provide consulting and implementation for computer system integration, and training and consulting on software development and automation.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="band mist" id="q-flow">
    <div class="wrap split">
      <div>
        <p class="status-line"><span class="status">In development</span></p>
        <h2>Our product: Q-Flow</h2>
        <p class="lead">Engineering software that automates the structural analysis of API 661 air-cooled heat exchanger (ACHE) header boxes, from geometry input to report.</p>
        <a class="btn btn-line" href="q-flow/">More about Q-Flow</a>
      </div>
      <ol class="steps">
{steps([("3D modeling", "Takes header box and nozzle dimensions and builds the 3D geometry for analysis."),
        ("Finite element analysis", "Generates the analysis input files, runs the solver, and calculates every load combination."),
        ("Report generation", "Puts the analysis results into a report in a standard format.")])}
      </ol>
    </div>
  </section>

  <section class="band" id="why">
    <div class="wrap">
      <div class="band-head">
        <h2>A software company that understands design and analysis</h2>
        <p>We listen to requirements in the engineer's language and turn them into software.</p>
      </div>
      <div class="grid-3">
        <div class="point">
          <h3>We start from engineering practice</h3>
          <p>We design software around the procedures, acceptance criteria, and report formats of 3D CAD modeling and structural analysis (FEA), so the output can go straight into an engineer's review.</p>
        </div>
        <div class="point">
          <h3>We connect it end to end in Python</h3>
          <p>Model generation, analysis runs, result processing, and documentation are linked in Python to reduce the steps that need a person.</p>
        </div>
        <div class="point">
          <h3>We have delivered on site at a large enterprise</h3>
          <p>Since 2023 we have carried out software development projects on site at a major Korean electronics manufacturer.</p>
        </div>
      </div>
    </div>
  </section>
""" + foot("en", "../")

pages["en/q-flow/index.html"] = head("en",
    "Q-Flow | Cookie Interactive Inc.",
    "Q-Flow is engineering software that automates 3D modeling, finite element analysis, and report writing for API 661 air-cooled heat exchanger header boxes. It is in development.",
    "/en/q-flow/", "../../", "q-flow", "/q-flow/") + f"""
  <section class="hero">
    <div class="wrap">
      <div>
        <p class="status-line"><span class="status">In development</span></p>
        <h1>Q-Flow</h1>
        <p class="lead">Engineering software that automates the structural analysis of API 661 air-cooled heat exchanger (ACHE) header boxes, from geometry input to report.</p>
        <div class="actions">
          <a class="btn btn-light" href="mailto:{MAIL}">Ask about the product</a>
        </div>
      </div>
      {figure("en", "../../")}
    </div>
  </section>

  <section class="band">
    <div class="wrap split">
      <div>
        <h2>From manual analysis steps to a single flow</h2>
        <p class="lead">Q-Flow replaces the work of refining meshes and running load combinations one at a time with an automated procedure. Load combinations that are easy to skip because of time and cost are all calculated by the same procedure.</p>
      </div>
      <ol class="steps">
{steps([("3D modeling", "Takes the header box and nozzle geometry as input and automatically builds the 3D geometry for analysis."),
        ("Finite element analysis", "Generates analysis input files in Python, runs them on the CalculiX solver, and calculates every load combination."),
        ("Report generation", "Writes an analysis report in a standard format, including SCL (stress classification line) results.")])}
      </ol>
    </div>
  </section>

  <section class="band mist">
    <div class="wrap split">
      <div>
        <h2>Eight default load combinations</h2>
        <p class="lead">By default Q-Flow calculates eight combinations of maximum allowable working pressure (MAWP) with wind and seismic loads in each direction.</p>
      </div>
      <table class="table">
        <thead>
          <tr><th scope="col">Load</th><th scope="col">Direction</th></tr>
        </thead>
        <tbody>
{rows([("MAWP + wind", "+X, −X, +Y, −Y"), ("MAWP + seismic", "+X, −X, +Y, −Y")])}
        </tbody>
      </table>
    </div>
  </section>

  <section class="band">
    <div class="wrap split">
      <div>
        <h2>Product overview</h2>
        <p class="lead">We are building Q-Flow for EPC engineering teams that review drawings from many vendors.</p>
      </div>
      <div>
        <table class="table">
          <tbody>
{rows([("Target equipment", "API 661 air-cooled heat exchangers (ACHE)"), ("Analysis scope", "Header box and nozzles"), ("Solver", "CalculiX"),
       ("Automation", "Python"), ("Output", "Analysis report including SCL results"), ("Status", "In development (not yet released)")])}
          </tbody>
        </table>
        <p class="note">Q-Flow is in development, so details may change.</p>
      </div>
    </div>
  </section>
""" + foot("en", "../../")

pages["en/company/index.html"] = head("en",
    "Company | Cookie Interactive Inc.",
    "Company profile, business purposes, track record, and certificates of Cookie Interactive Inc.",
    "/en/company/", "../../", "company", "/company/") + f"""
  <section class="page-head">
    <div class="wrap">
      <h1>Company</h1>
      <p>Cookie Interactive Inc. is a software company established in 2017 and based in Changwon, South Korea. We automate repetitive engineering analysis and office work with software.</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap stack">

      <div class="split" id="profile">
        <h2 class="section-title">Company profile</h2>
        <table class="table">
          <tbody>
{rows([("Company name", 'Cookie Interactive Inc.<span class="sub" lang="ko">쿠키인터랙티브 주식회사</span>'), ("Representative", "Bongtae Jeon"), ("Established", "26 May 2017"),
       ("Location", "Changwon, Gyeongsangnam-do, Republic of Korea"), ("Business registration no.", "620-87-00732"),
       ("Company size", 'Small enterprise<span class="sub">Holds a Korean SME Certificate</span>')])}
          </tbody>
        </table>
      </div>

      <div class="split" id="business">
        <div>
          <h2 class="section-title">Business purposes</h2>
          <p class="note tight">Main items from the business purposes in the articles of incorporation.</p>
        </div>
        <ul class="plain-list">
          <li>Development, rental, and supply of online, mobile, and computer programs</li>
          <li>Development and supply of system and application software</li>
          <li>Computer system integration consulting and implementation services</li>
          <li>Data processing and other computer operation services</li>
          <li>Database and online information services</li>
          <li>Other engineering services</li>
          <li>Training and consulting</li>
        </ul>
      </div>

      <div class="split" id="capabilities">
        <h2 class="section-title">Capabilities</h2>
        <table class="table">
          <thead>
            <tr><th scope="col">Area</th><th scope="col">Technologies</th></tr>
          </thead>
          <tbody>
{rows([("Software development", "Python"), ("Work automation", "RPA, Python, AutoHotKey"), ("Design", "3D CAD (Inventor, CATIA)"), ("Structural analysis", "Finite element analysis (Ansys, CalculiX)")])}
          </tbody>
        </table>
      </div>

      <div class="split" id="records">
        <div>
          <h2 class="section-title">Track record</h2>
          <p class="note tight">Client names are not listed.</p>
        </div>
        <table class="table wide">
          <thead>
            <tr><th scope="col">Period</th><th scope="col">Work</th><th scope="col">Technology</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Jan 2024 – Nov 2026</th><td>On-site software development for a major Korean electronics manufacturer</td><td>Python</td></tr>
            <tr><th scope="row">Mar 2023 – Oct 2023</th><td>On-site software development for a major Korean electronics manufacturer</td><td>Python</td></tr>
          </tbody>
        </table>
      </div>

      <div class="split" id="certificates">
        <h2 class="section-title">Certificates</h2>
        <table class="table wide">
          <thead>
            <tr><th scope="col">Name</th><th scope="col">Classification</th><th scope="col">Issued by</th><th scope="col">Valid</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">SME Certificate</th><td>Small enterprise</td><td>Ministry of SMEs and Startups, Republic of Korea</td><td class="nowrap">2026-04-01 to 2027-03-31</td></tr>
          </tbody>
        </table>
      </div>

      <div class="split" id="notice-method">
        <h2 class="section-title">Company notices</h2>
        <div class="prose">
          <p>Under its articles of incorporation, Cookie Interactive Inc. publishes its company notices on this website, in Korean. If a notice cannot be published here because of a system failure or another unavoidable reason, it is published in the Gyeongnam Domin Ilbo newspaper.</p>
          <p><a href="../../notice/" hreflang="ko">View notices (in Korean)</a></p>
        </div>
      </div>

    </div>
  </section>
""" + foot("en", "../../")

for rel, html in pages.items():
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote", rel, len(html))
