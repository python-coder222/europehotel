"""
Hamilton Hotel Tashkent — Flask ilovasi (v2, 360deg redesign)
Bitta app.py fayl ichida: routelar va sahifa (HTML/CSS/JS).
Ishga tushirish: pip install flask --break-system-packages && python app.py
"""

from flask import Flask, redirect

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Asosiy sahifa — hero, narxlar (tab), joylashuv, fikr-mulohaza slider,
# FAQ, bron qilish. Barcha "narxni aniqlashtirish" tugmalari Telegram'ga
# (https://t.me/+998955151517) olib boradi.
# ---------------------------------------------------------------------------
INDEX_HTML = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hamilton Hotel Tashkent</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;700;900&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#F3F1EC; --card:#FFFFFF; --ink:#181614; --ink-soft:#5B5750;
    --red:#B3231A; --red-2:#8B1912;
    --line: rgba(24,22,20,0.13);
    --shadow: 0 26px 60px rgba(20,16,12,0.16);
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{ background:var(--bg); color:var(--ink); font-family:'Inter',sans-serif; line-height:1.65; -webkit-font-smoothing:antialiased; overflow-x:hidden; cursor:default; }
  ::selection{ background:var(--red); color:#fff; }
  h1,h2,h3{ font-family:'Big Shoulders Display',sans-serif; font-weight:800; letter-spacing:-0.01em; line-height:0.95; text-transform:uppercase; }
  .wrap{ max-width:1220px; margin:0 auto; padding:0 32px; }
  section{ padding:120px 0; position:relative; }
  @media (max-width:720px){ section{ padding:66px 0; } .wrap{ padding:0 20px; } }

  .eyebrow{ font-family:'IBM Plex Mono',monospace; font-size:0.72rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--red); display:flex; align-items:center; gap:10px; font-weight:600; }
  .eyebrow::before{ content:''; width:28px; height:2px; background:var(--red); display:inline-block; }
  .eyebrow.on-dark{ color:#E8A79C; }
  .eyebrow.on-dark::before{ background:#E8A79C; }

  .reveal{ opacity:0; transform:translateY(40px); transition:opacity .8s cubic-bezier(.16,.9,.2,1), transform .8s cubic-bezier(.16,.9,.2,1); }
  .reveal.in{ opacity:1; transform:translateY(0); }

  #progress{ position:fixed; top:0; left:0; height:3px; background:var(--red); z-index:120; width:0%; }

  /* cursor spotlight */
  .spot{ position:relative; }
  .spot::before{ content:''; position:absolute; inset:0; pointer-events:none; z-index:1; background:radial-gradient(460px circle at var(--sx,50%) var(--sy,50%), rgba(179,35,26,0.16), transparent 70%); }

  /* side dot nav */
  .dotnav{ position:fixed; right:26px; top:50%; transform:translateY(-50%); z-index:70; display:flex; flex-direction:column; gap:14px; }
  .dotnav a{ width:10px; height:10px; border-radius:50%; border:1.5px solid var(--ink); display:block; transition:background .25s, transform .25s; }
  .dotnav a.active{ background:var(--red); border-color:var(--red); transform:scale(1.3); }
  @media (max-width:900px){ .dotnav{ display:none; } }

  .btn{ font-family:'Inter'; font-weight:700; font-size:0.9rem; padding:16px 30px; border-radius:2px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; border:1.5px solid var(--ink); cursor:pointer; transition:transform .25s, background .25s, color .25s; }
  .btn-red{ background:var(--red); color:#fff; border-color:var(--red); }
  .btn-red:hover{ transform:translateY(-3px); background:var(--red-2); }
  .btn-outline{ background:transparent; color:var(--ink); }
  .btn-outline:hover{ transform:translateY(-3px); background:var(--ink); color:#fff; }
  .btn-outline.on-hero{ color:#fff; border-color:rgba(255,255,255,0.5); }
  .btn-outline.on-hero:hover{ background:#fff; color:var(--ink); }
  .nav-book{ padding:10px 20px; font-size:0.78rem; }

  /* ===== NAV ===== */
  nav{ position:fixed; top:0; left:0; right:0; z-index:80; display:flex; align-items:center; justify-content:space-between; padding:24px 40px; mix-blend-mode:difference; }
  .brand{ color:#fff; font-family:'Big Shoulders Display'; font-weight:900; font-size:1.6rem; text-decoration:none; text-transform:uppercase; }
  .nav-links{ display:flex; gap:26px; list-style:none; }
  .nav-links a{ color:#fff; text-decoration:none; font-size:0.82rem; font-weight:600; text-transform:uppercase; letter-spacing:0.03em; }
  @media (max-width:900px){ .nav-links{ display:none; } nav{ padding:16px 20px; } }

  /* ===== HERO ===== */
  .hero{ min-height:100vh; position:relative; display:flex; align-items:flex-end; padding-top:120px; color:#fff; overflow:hidden; background:var(--ink); }
  .hero-grid-bg{ position:absolute; inset:0; opacity:0.5; background-image: linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px); background-size:64px 64px; mask-image:radial-gradient(circle at 30% 30%, black, transparent 75%); }
  .hero-glow{ position:absolute; width:900px; height:900px; border-radius:50%; background:radial-gradient(circle, rgba(179,35,26,0.35), transparent 70%); top:-300px; right:-300px; filter:blur(40px); }
  .hero-inner{ position:relative; z-index:2; width:100%; padding-bottom:80px; }
  .hero .eyebrow{ color:#E8A79C; }
  .hero .eyebrow::before{ background:#E8A79C; }
  .hero h1{ font-size:clamp(4rem,13vw,10.5rem); margin-top:10px; }
  .hero h1 .out{ -webkit-text-stroke:2px #fff; color:transparent; }
  .hero-bottom{ display:flex; justify-content:space-between; align-items:flex-end; gap:30px; margin-top:40px; flex-wrap:wrap; }
  .hero p.lead{ max-width:440px; font-size:1.05rem; color:rgba(243,241,236,0.78); font-family:'Inter'; text-transform:none; }
  .hero-actions{ display:flex; gap:14px; }
  .rating-badge{ display:flex; align-items:center; gap:14px; border:1px solid rgba(232,167,156,0.4); padding:14px 20px; border-radius:2px; }
  .rating-badge .num{ font-family:'Big Shoulders Display'; font-weight:800; font-size:2rem; color:#E8A79C; }
  .rating-badge .lbl{ font-family:'IBM Plex Mono'; font-size:0.64rem; letter-spacing:0.08em; text-transform:uppercase; color:rgba(243,241,236,0.55); }

  /* ===== MARQUEE ===== */
  .marquee-strip{ background:var(--red); padding:18px 0; overflow:hidden; white-space:nowrap; }
  .marquee-track{ display:inline-flex; gap:44px; animation:marquee 20s linear infinite; }
  .marquee-track span{ font-family:'Big Shoulders Display'; font-weight:700; font-size:1.3rem; color:#fff; text-transform:uppercase; display:flex; align-items:center; gap:44px; }
  .marquee-track span::after{ content:'✦'; font-size:0.7rem; margin-left:44px; }
  @keyframes marquee{ from{ transform:translateX(0); } to{ transform:translateX(-50%); } }

  /* ===== ABOUT ===== */
  .about-grid{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:70px; align-items:center; }
  @media (max-width:880px){ .about-grid{ grid-template-columns:1fr; gap:36px; } }
  .about h2{ font-size:clamp(2.4rem,5vw,3.6rem); margin:16px 0 20px; }
  .about p{ color:var(--ink-soft); max-width:54ch; font-size:1.03rem; }
  .amenity-list{ display:flex; flex-direction:column; }
  .amenity{ display:flex; align-items:center; gap:16px; padding:20px 0; border-bottom:1px solid var(--line); }
  .amenity:first-child{ border-top:1px solid var(--line); }
  .amenity .ic{ width:26px; height:26px; color:var(--red); flex-shrink:0; }
  .amenity .name{ font-family:'Big Shoulders Display'; font-weight:700; font-size:1.1rem; text-transform:uppercase; }
  .stat-row{ display:flex; gap:0; margin-top:40px; border-top:1px solid var(--line); }
  .stat-row .stat{ flex:1; padding:20px 20px 0 0; border-right:1px solid var(--line); }
  .stat-row .stat:last-child{ border-right:none; }
  .stat-row .num{ font-family:'Big Shoulders Display'; font-weight:800; font-size:2.4rem; color:var(--red); }
  .stat-row .lbl{ font-family:'IBM Plex Mono'; font-size:0.62rem; letter-spacing:0.08em; text-transform:uppercase; color:var(--ink-soft); margin-top:4px; }

  /* ===== PRICE TABS ===== */
  .rooms{ background:var(--ink); color:#fff; }
  .rooms h2{ color:#fff; font-size:clamp(2.4rem,5vw,3.6rem); margin:16px 0 46px; max-width:16ch; }
  .tabs{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:34px; }
  .tab-btn{ font-family:'Big Shoulders Display'; font-weight:700; text-transform:uppercase; font-size:1rem; letter-spacing:0.02em; background:transparent; border:1.5px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.6); padding:12px 24px; border-radius:2px; cursor:pointer; transition:all .25s; }
  .tab-btn.active{ background:var(--red); border-color:var(--red); color:#fff; }
  .tab-panel{ display:none; background:#221E1B; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:44px; }
  .tab-panel.active{ display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center; }
  @media (max-width:700px){ .tab-panel.active{ grid-template-columns:1fr; text-align:center; } }
  .tab-panel .range{ font-family:'Big Shoulders Display'; font-weight:800; font-size:clamp(2.2rem,5.4vw,3.4rem); color:#E8A79C; }
  .tab-panel .range small{ font-family:'Inter'; font-size:0.85rem; color:rgba(243,241,236,0.55); display:block; margin-top:6px; text-transform:none; font-weight:400; }
  .tab-panel .desc{ color:rgba(243,241,236,0.68); margin-top:14px; max-width:44ch; font-size:0.95rem; }
  .price-disclaimer{ margin-top:24px; font-family:'IBM Plex Mono'; font-size:0.72rem; color:rgba(243,241,236,0.4); }

  .feature-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:20px; margin-top:50px; }
  @media (max-width:760px){ .feature-grid{ grid-template-columns:1fr; } }
  .feature-card{ border:1px solid rgba(255,255,255,0.12); border-radius:6px; padding:26px; }
  .feature-card .ic{ width:30px; height:30px; color:#E8A79C; margin-bottom:14px; }
  .feature-card h3{ font-size:1.05rem; color:#fff; margin-bottom:8px; text-transform:uppercase; }
  .feature-card p{ color:rgba(243,241,236,0.6); font-size:0.88rem; font-family:'Inter'; text-transform:none; font-weight:400; }

  /* ===== LOCATION ===== */
  .location{ background:var(--bg); }
  .loc-grid{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:70px; align-items:start; }
  @media (max-width:880px){ .loc-grid{ grid-template-columns:1fr; gap:40px; } }
  .loc-list{ margin-top:24px; }
  .loc-item{ display:flex; gap:18px; padding:18px 0; border-bottom:1px solid var(--line); align-items:flex-start; }
  .loc-item:first-child{ border-top:1px solid var(--line); }
  .loc-dist{ font-family:'IBM Plex Mono'; font-size:0.78rem; color:var(--red); min-width:80px; font-weight:600; }
  .loc-name{ font-family:'Big Shoulders Display'; font-weight:700; font-size:1.1rem; text-transform:uppercase; }
  .addr-block{ background:var(--ink); color:#fff; border-radius:8px; padding:38px; box-shadow:var(--shadow); }
  .addr-block h3{ color:#fff; font-size:1.5rem; margin:14px 0 6px; }
  .addr-block p{ color:rgba(243,241,236,0.72); font-family:'Inter'; text-transform:none; font-weight:400; }
  .addr-block a{ color:#E8A79C; text-decoration:none; }
  .addr-block .map-btn{ margin-top:24px; }
  .map-card{ border-radius:8px; overflow:hidden; box-shadow:var(--shadow); margin-top:26px; }
  .map-card iframe{ width:100%; height:280px; border:0; filter:grayscale(0.4) contrast(1.05); }

  /* ===== REVIEWS SLIDER ===== */
  .reviews{ background:#221E1B; color:#fff; overflow:hidden; }
  .reviews h2{ color:#fff; font-size:clamp(2.4rem,5vw,3.6rem); margin:16px 0 24px; }
  .sentiment-row{ display:flex; flex-wrap:wrap; gap:12px; margin-bottom:50px; }
  .sentiment-chip{ font-family:'IBM Plex Mono'; font-size:0.72rem; padding:9px 16px; border-radius:2px; border:1px solid rgba(232,167,156,0.35); color:rgba(243,241,236,0.85); }
  .sentiment-chip b{ color:#E8A79C; }
  .slider{ position:relative; max-width:760px; margin:0 auto; }
  .slide-track{ position:relative; height:230px; }
  .review-card{ position:absolute; inset:0; background:var(--ink); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:34px; opacity:0; transform:translateX(30px); transition:opacity .5s, transform .5s; pointer-events:none; }
  .review-card.active{ opacity:1; transform:translateX(0); pointer-events:auto; }
  .review-card .stars{ color:var(--red); font-size:0.9rem; letter-spacing:2px; }
  .review-card p{ margin:16px 0 20px; color:rgba(243,241,236,0.85); font-size:0.98rem; font-family:'Inter'; text-transform:none; font-weight:400; }
  .review-card .who{ font-family:'IBM Plex Mono'; font-size:0.68rem; text-transform:uppercase; letter-spacing:0.06em; color:rgba(243,241,236,0.45); }
  .slider-dots{ display:flex; justify-content:center; gap:10px; margin-top:26px; }
  .slider-dots button{ width:9px; height:9px; border-radius:50%; border:none; background:rgba(255,255,255,0.25); cursor:pointer; padding:0; }
  .slider-dots button.active{ background:var(--red); }

  /* ===== FAQ ===== */
  .faq{ background:var(--bg); }
  .faq h2{ font-size:clamp(2.4rem,5vw,3.6rem); margin:16px 0 46px; }
  .faq-item{ border-top:1px solid var(--line); }
  .faq-item:last-child{ border-bottom:1px solid var(--line); }
  .faq-q{ width:100%; text-align:left; background:none; border:none; padding:26px 0; display:flex; justify-content:space-between; align-items:center; cursor:pointer; font-family:'Big Shoulders Display'; font-weight:700; font-size:1.2rem; text-transform:uppercase; color:var(--ink); }
  .faq-q .plus{ font-size:1.6rem; color:var(--red); transition:transform .3s; flex-shrink:0; margin-left:20px; }
  .faq-item.open .faq-q .plus{ transform:rotate(45deg); }
  .faq-a{ max-height:0; overflow:hidden; transition:max-height .35s ease; }
  .faq-a p{ padding-bottom:24px; color:var(--ink-soft); max-width:60ch; }

  /* ===== BOOK ===== */
  .book{ background:var(--ink); color:#fff; text-align:center; }
  .book h2{ color:#fff; font-size:clamp(2.6rem,7vw,5rem); margin:18px 0 18px; }
  .book p{ color:rgba(243,241,236,0.68); max-width:48ch; margin:0 auto; font-family:'Inter'; text-transform:none; font-weight:400; }
  .book-actions{ display:flex; gap:16px; justify-content:center; margin-top:36px; flex-wrap:wrap; }
  .contact-strip{ display:flex; justify-content:center; gap:40px; margin-top:44px; flex-wrap:wrap; }
  .contact-item{ text-align:left; }
  .contact-item .k{ font-family:'IBM Plex Mono'; font-size:0.62rem; letter-spacing:0.1em; text-transform:uppercase; color:#E8A79C; }
  .contact-item a{ display:block; font-family:'Big Shoulders Display'; font-weight:700; font-size:1.1rem; color:#fff; text-decoration:none; margin-top:6px; text-transform:uppercase; }
  .contact-item a:hover{ color:#E8A79C; }

  footer{ background:#0F0D0C; color:rgba(243,241,236,0.5); padding:32px 0; font-size:0.8rem; display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; }
  footer a{ color:rgba(243,241,236,0.75); text-decoration:none; }
  footer a:hover{ color:#E8A79C; }

  /* ===== FLOATING TELEGRAM BUBBLE ===== */
  .tg-float{ position:fixed; bottom:26px; right:26px; z-index:90; width:60px; height:60px; border-radius:50%; background:var(--red); display:flex; align-items:center; justify-content:center; box-shadow:0 12px 30px rgba(179,35,26,0.45); text-decoration:none; }
  .tg-float svg{ width:28px; height:28px; fill:#fff; }
  .tg-float::before{ content:''; position:absolute; inset:0; border-radius:50%; border:2px solid var(--red); animation:pulse-ring 2s ease-out infinite; }
  @keyframes pulse-ring{ 0%{ transform:scale(1); opacity:0.7; } 100%{ transform:scale(1.6); opacity:0; } }

  @media (prefers-reduced-motion: reduce){
    .reveal{ transition:none; opacity:1; transform:none; }
    .marquee-track{ animation:none; }
    .tg-float::before{ animation:none; }
    html{ scroll-behavior:auto; }
  }
</style>
</head>
<body>
<div id="progress"></div>

<div class="dotnav" id="dotnav">
  <a href="#top" class="active" data-sec="top"></a>
  <a href="#about" data-sec="about"></a>
  <a href="#rooms" data-sec="rooms"></a>
  <a href="#location" data-sec="location"></a>
  <a href="#reviews" data-sec="reviews"></a>
  <a href="#faq" data-sec="faq"></a>
  <a href="#book" data-sec="book"></a>
</div>

<nav id="nav">
  <a class="brand" href="#top">Hamilton</a>
  <ul class="nav-links">
    <li><a href="#about">Biz haqimizda</a></li>
    <li><a href="#rooms">Narxlar</a></li>
    <li><a href="#location">Manzil</a></li>
    <li><a href="#reviews">Fikrlar</a></li>
    <li><a href="#faq">Savollar</a></li>
  </ul>
  <a class="btn btn-red nav-book" href="#book">Bron qilish</a>
</nav>

<header class="hero" id="top">
  <div class="hero-grid-bg"></div>
  <div class="hero-glow"></div>
  <div class="wrap hero-inner">
    <div class="eyebrow reveal">Toshkent · Qoraqum 1-tor koʻchasi, 42</div>
    <h1 class="reveal">Hamilton<br><span class="out">Hotel</span></h1>
    <div class="hero-bottom reveal">
      <p class="lead">Toʻqimachilik institutiga yaqin, tinch koʻchada joylashgan mehmonxona — do‘stona xodimlar va yoqimli muhit bilan.</p>
      <div class="hero-actions">
        <a class="btn btn-red" href="#rooms">Narxlarni koʻrish</a>
        <a class="btn btn-outline on-hero" href="tel:+998955151517">Qoʻngʻiroq qilish</a>
      </div>
    </div>
    <div class="rating-badge reveal" style="margin-top:40px;">
      <div class="num">4.7</div>
      <div>
        <div class="lbl">189 ta baho</div>
        <div class="lbl" style="color:#E8A79C">★★★★★</div>
      </div>
    </div>
  </div>
</header>

<div class="marquee-strip">
  <div class="marquee-track">
    <span>Bepul avtoturargoh</span><span>Xonada konditsioner</span><span>4.7 reyting</span><span>Kun-u tun qabul</span><span>Do‘stona xodimlar</span><span>Bepul avtoturargoh</span><span>Xonada konditsioner</span><span>4.7 reyting</span><span>Kun-u tun qabul</span><span>Do‘stona xodimlar</span>
  </div>
</div>

<section class="about spot" id="about">
  <div class="wrap about-grid">
    <div class="reveal">
      <div class="eyebrow">Biz haqimizda</div>
      <h2>Tinch koʻchada,<br>samimiy xizmat</h2>
      <p>Hamilton Hotel — Toʻqimachilik institutiga piyoda masofada, tinch koʻchada joylashgan 3 yulduzli mehmonxona. Mehmonlar xodimlarning samimiyligi va yordamga tayyorligini alohida ta’kidlashadi — ayniqsa ro‘yxatdan o‘tish va kundalik ehtiyojlarda. Xonalar keng, balandligi baland, deraz oynalari tinch koʻchaga qaraydi.</p>
      <div class="stat-row">
        <div class="stat"><div class="num"><span class="counter" data-target="4.7" data-decimals="1">0</span></div><div class="lbl">Reyting</div></div>
        <div class="stat"><div class="num">3★</div><div class="lbl">Toifa</div></div>
        <div class="stat"><div class="num">24/7</div><div class="lbl">Qabul xizmati</div></div>
      </div>
    </div>
    <div class="reveal">
      <div class="amenity-list">
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 10l9-7 9 7"/><path d="M5 9v11h14V9"/></svg><span class="name">Kun-u tun ishlaydi</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="7" width="18" height="12" rx="2"/><circle cx="8" cy="13" r="1.5"/></svg><span class="name">Avtoturargoh mavjud</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M10 4v16"/></svg><span class="name">Xonada konditsioner</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 3v18M5 8l7-5 7 5M5 8v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8"/></svg><span class="name">Institutga 93 m</span></div>
      </div>
    </div>
  </div>
</section>

<section class="rooms spot" id="rooms">
  <div class="wrap">
    <div class="eyebrow on-dark reveal">Narxlar</div>
    <h2 class="reveal">Har xil byudjetga<br>mos xonalar</h2>

    <div class="tabs reveal">
      <button class="tab-btn active" data-tab="standard">Standard</button>
      <button class="tab-btn" data-tab="comfort">Comfort</button>
      <button class="tab-btn" data-tab="lux">Lux</button>
    </div>

    <div class="tab-panel active" id="panel-standard">
      <div>
        <div class="range">300 000 – 450 000<small>so‘m / kecha</small></div>
        <p class="desc">Ixcham va qulay xona — yakka yoki juftlik uchun. Konditsioner, tinch koʻchaga qaragan deraz.</p>
      </div>
      <a class="btn btn-red" href="https://t.me/+998955151517" target="_blank" rel="noopener">Narxlarni aniqlashtirish</a>
    </div>
    <div class="tab-panel" id="panel-comfort">
      <div>
        <div class="range">450 000 – 650 000<small>so‘m / kecha</small></div>
        <p class="desc">Kengroq xona, qo‘shimcha qulayliklar bilan — oila yoki hamkasblar bilan sayohat uchun.</p>
      </div>
      <a class="btn btn-red" href="https://t.me/+998955151517" target="_blank" rel="noopener">Narxlarni aniqlashtirish</a>
    </div>
    <div class="tab-panel" id="panel-lux">
      <div>
        <div class="range">650 000 – 800 000<small>so‘m / kecha</small></div>
        <p class="desc">Eng yuqori toifadagi xona — maksimal joy va qulaylik.</p>
      </div>
      <a class="btn btn-red" href="https://t.me/+998955151517" target="_blank" rel="noopener">Narxlarni aniqlashtirish</a>
    </div>
    <div class="price-disclaimer reveal">* Narxlar taxminiy oraliqda koʻrsatilgan — aniq narx va boʻsh joylar uchun Telegram orqali soʻrang.</div>

    <div class="feature-grid">
      <div class="feature-card reveal">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="3" y="7" width="18" height="12" rx="2"/><circle cx="8" cy="13" r="1.5"/></svg>
        <h3>Avtoturargoh</h3>
        <p>Mehmonlar uchun bepul avtoturargoh joyi mavjud.</p>
      </div>
      <div class="feature-card reveal">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M10 4v16"/></svg>
        <h3>Konditsioner</h3>
        <p>Barcha xonalarda konditsioner o‘rnatilgan.</p>
      </div>
      <div class="feature-card reveal">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
        <h3>Kun-u tun qabul</h3>
        <p>Istalgan vaqtda kirish/chiqish — qabul xizmati doim ishlaydi.</p>
      </div>
    </div>
  </div>
</section>

<section class="location spot" id="location">
  <div class="wrap loc-grid">
    <div class="reveal">
      <div class="eyebrow">Joylashuv</div>
      <h2 style="font-size:clamp(2.4rem,5vw,3.6rem); margin:16px 0 6px;">Metro va markazga<br>yaqin</h2>
      <div class="loc-list">
        <div class="loc-item"><span class="loc-dist">93 m</span><span class="loc-name">Toʻqimachilik instituti bekati</span></div>
        <div class="loc-item"><span class="loc-dist">2,17 km</span><span class="loc-name">Novza bekati</span></div>
        <div class="loc-item"><span class="loc-dist">~3 km</span><span class="loc-name">Toshkent xalqaro aeroporti</span></div>
      </div>
      <div class="map-card">
        <iframe src="https://maps.google.com/maps?q=41.281,69.242&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
    <div class="addr-block reveal">
      <div class="eyebrow on-dark">Manzil</div>
      <h3>Qoraqum 1-tor<br>koʻchasi, 42</h3>
      <p>Toshkent shahri</p>
      <p style="margin-top:18px;">☎ <a href="tel:+998955151517">+998 95 515 15 17</a></p>
      <p>💬 <a href="https://t.me/+998955151517" target="_blank" rel="noopener">Telegram orqali yozish</a></p>
      <a class="btn btn-red map-btn" href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" rel="noopener">Yandex Xaritada koʻrish</a>
    </div>
  </div>
</section>

<section class="reviews" id="reviews">
  <div class="wrap">
    <div class="eyebrow on-dark reveal">Mehmonlar fikri</div>
    <h2 class="reveal">189 ta bahoga<br>asoslangan — 4.7</h2>
    <div class="sentiment-row reveal">
      <div class="sentiment-chip">Xodimlar xizmati — <b>81% musbat</b></div>
      <div class="sentiment-chip">Muhit — <b>92% musbat</b></div>
      <div class="sentiment-chip">Tozalik — <b>41% musbat</b></div>
    </div>
    <div class="slider reveal">
      <div class="slide-track" id="slideTrack">
        <div class="review-card active">
          <div class="stars">★★★★★</div>
          <p>“Yoqimli va e’tiborli xodimlar. Ro‘yxatdan o‘tishda va kundalik masalalarda yordam berishdi. Keng oynalar, baland shift, tinch koʻchaga qaragan.”</p>
          <div class="who">Anastasia D. · 19-may</div>
        </div>
        <div class="review-card">
          <div class="stars">★★★★★</div>
          <p>“10 kun dam oldik — toza, qulay. Resepshndagi Alisher alohida yordamga tayyor edi. Nonushtalar xilma-xil, xonalarda tinch. Yana kelamiz.”</p>
          <div class="who">Rezeda G. · 2-iyun</div>
        </div>
        <div class="review-card">
          <div class="stars">★★★★☆</div>
          <p>“Umuman yaxshi mehmonxona, yotoq qulay, choyshablar toza va tabiiy matodan. Joylashuvi va xodimlarning muomalasi ijobiy taassurot qoldirdi.”</p>
          <div class="who">Anastasiya L. · 19-aprel</div>
        </div>
      </div>
      <div class="slider-dots" id="sliderDots"></div>
    </div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="wrap">
    <div class="eyebrow reveal">Savol-javob</div>
    <h2 class="reveal">Tez-tez soʻraladigan<br>savollar</h2>
    <div id="faqList">
      <div class="faq-item">
        <button class="faq-q">Mehmonxona necha soat ishlaydi?<span class="plus">+</span></button>
        <div class="faq-a"><p>Hamilton Hotel kun-u tun (24/7) ishlaydi — istalgan vaqtda kirish va chiqish mumkin, qabul xizmati doim faol.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Avtoturargoh bormi?<span class="plus">+</span></button>
        <div class="faq-a"><p>Ha, mehmonlar uchun avtoturargoh joyi mavjud.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Xona narxi qanday belgilanadi?<span class="plus">+</span></button>
        <div class="faq-a"><p>Narx xona toifasiga qarab 300 000 dan 800 000 so‘mgacha o‘zgaradi. Aniq narx va bo‘sh joylar uchun Telegram yoki telefon orqali bog‘laning.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Metro yoki jamoat transportiga yaqinmi?<span class="plus">+</span></button>
        <div class="faq-a"><p>Ha — Toʻqimachilik instituti bekati atigi 93 metr uzoqlikda, Novza bekati esa 2,17 km.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Qanday bron qilsam bo‘ladi?<span class="plus">+</span></button>
        <div class="faq-a"><p>Telefon orqali qo‘ng‘iroq qiling yoki Telegram orqali yozing — xodimlar kun-u tun javob berishga tayyor.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="book" id="book">
  <div class="wrap">
    <div class="eyebrow" style="justify-content:center">Bron qilish</div>
    <h2>Joyingizni<br>band qiling</h2>
    <p>Bron qilish yoki savollaringiz uchun telefon orqali qo‘ng‘iroq qiling yoki Telegram orqali yozing — xodimlarimiz kun-u tun javob berishga tayyor.</p>
    <div class="book-actions">
      <a class="btn btn-red" href="https://t.me/+998955151517" target="_blank" rel="noopener">💬 Telegram orqali bron qilish</a>
      <a class="btn btn-outline on-hero" href="tel:+998955151517">📞 +998 95 515 15 17</a>
    </div>
    <div class="contact-strip">
      <div class="contact-item"><div class="k">Manzil</div><a href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" rel="noopener">Qoraqum 1-tor koʻchasi, 42</a></div>
      <div class="contact-item"><div class="k">Ish vaqti</div><a href="#">Kun-u tun</a></div>
      <div class="contact-item"><div class="k">Narx</div><a href="#rooms">300 000 – 800 000 so‘m</a></div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap" style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px;">
    <span>© Hamilton Hotel — Qoraqum 1-tor koʻchasi, 42, Toshkent</span>
    <a href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" rel="noopener">Yandex Maps’da ko‘rish</a>
  </div>
</footer>

<a class="tg-float" href="https://t.me/+998955151517" target="_blank" rel="noopener" aria-label="Telegram">
  <svg viewBox="0 0 24 24"><path d="M21.9 3.2 2.7 10.7c-1.3.5-1.3 1.2-.2 1.6l4.9 1.5 1.9 5.9c.2.6.4.9.9.9.4 0 .6-.2.9-.5l2.2-2.1 4.6 3.4c.8.5 1.4.2 1.6-.8l3-14.1c.3-1.2-.4-1.8-1.6-1.3zM8.6 13.6l9.3-5.9c.5-.3.9-.1.6.2l-7.9 7.2-.3 3.1-1.7-4.6z"/></svg>
</a>

<script>
  /* nav scroll blend */
  const nav = document.getElementById('nav');

  /* progress bar */
  const progress = document.getElementById('progress');
  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const pct = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
    progress.style.width = pct + '%';
  });

  /* reveal */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* counters */
  function animateCounter(el){
    const target = parseFloat(el.dataset.target);
    const decimals = parseInt(el.dataset.decimals || '0');
    const dur = 1300; const start = performance.now();
    function step(now){
      const p = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  const counterIo = new IntersectionObserver((entries) => {
    entries.forEach(e => { if(e.isIntersecting){ animateCounter(e.target); counterIo.unobserve(e.target); } });
  }, { threshold: 0.6 });
  document.querySelectorAll('.counter').forEach(el => counterIo.observe(el));

  /* cursor spotlight */
  document.querySelectorAll('.spot').forEach(sec => {
    sec.addEventListener('mousemove', (e) => {
      const r = sec.getBoundingClientRect();
      sec.style.setProperty('--sx', ((e.clientX - r.left) / r.width * 100) + '%');
      sec.style.setProperty('--sy', ((e.clientY - r.top) / r.height * 100) + '%');
    });
  });

  /* side dot nav active state */
  const sections = ['top','about','rooms','location','reviews','faq','book'].map(id => document.getElementById(id));
  const dots = document.querySelectorAll('.dotnav a');
  const secIo = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting){
        const id = e.target.id;
        dots.forEach(d => d.classList.toggle('active', d.dataset.sec === id));
      }
    });
  }, { threshold: 0.5 });
  sections.forEach(s => s && secIo.observe(s));

  /* price tabs */
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('panel-' + btn.dataset.tab).classList.add('active');
    });
  });

  /* testimonial slider */
  const cards = document.querySelectorAll('.review-card');
  const dotsWrap = document.getElementById('sliderDots');
  cards.forEach((c, i) => {
    const b = document.createElement('button');
    if (i === 0) b.classList.add('active');
    b.addEventListener('click', () => showSlide(i));
    dotsWrap.appendChild(b);
  });
  let slideIndex = 0;
  function showSlide(i){
    cards[slideIndex].classList.remove('active');
    dotsWrap.children[slideIndex].classList.remove('active');
    slideIndex = i;
    cards[slideIndex].classList.add('active');
    dotsWrap.children[slideIndex].classList.add('active');
  }
  setInterval(() => { showSlide((slideIndex + 1) % cards.length); }, 5000);

  /* FAQ accordion */
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => { i.classList.remove('open'); i.querySelector('.faq-a').style.maxHeight = null; });
      if (!isOpen){
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return INDEX_HTML


@app.route("/about")
def about():
    return redirect("/#about")


@app.route("/rooms")
def rooms():
    return redirect("/#rooms")


@app.route("/location")
def location():
    return redirect("/#location")


@app.route("/reviews")
def reviews():
    return redirect("/#reviews")


@app.route("/faq")
def faq():
    return redirect("/#faq")


@app.route("/book")
def book():
    return redirect("/#book")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
