"""
Hamilton Hotel Tashkent — Flask ilovasi
Bitta app.py fayl ichida: routelar va sahifa (HTML/CSS/JS).
Ishga tushirish: pip install flask --break-system-packages && python app.py
"""

from flask import Flask, redirect

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Asosiy sahifa — hero, narxlar, joylashuv, fikr-mulohazalar, bron qilish.
# ---------------------------------------------------------------------------
INDEX_HTML = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hamilton Hotel Tashkent</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --navy:#0F1C2E; --navy-2:#182B45; --navy-3:#0A1420;
    --gold:#C9A15A; --gold-soft:#E3C889;
    --bg:#F4F1EA; --ink:#15181D; --ink-soft:#4B5461;
    --line: rgba(15,28,46,0.12);
    --shadow: 0 26px 60px rgba(10,20,32,0.22);
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{ background:var(--bg); color:var(--ink); font-family:'Inter',sans-serif; line-height:1.65; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
  ::selection{ background:var(--gold); color:var(--navy); }
  h1,h2,h3{ font-family:'Space Grotesk',sans-serif; font-weight:700; letter-spacing:-0.02em; line-height:1.02; }
  .wrap{ max-width:1200px; margin:0 auto; padding:0 32px; }
  section{ padding:120px 0; position:relative; }
  @media (max-width:720px){ section{ padding:68px 0; } .wrap{ padding:0 20px; } }

  .eyebrow{ font-family:'IBM Plex Mono',monospace; font-size:0.72rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--gold); display:flex; align-items:center; gap:10px; font-weight:600; }
  .eyebrow::before{ content:''; width:28px; height:2px; background:var(--gold); display:inline-block; }
  .eyebrow.on-light{ color:#8A6B2E; }
  .eyebrow.on-light::before{ background:#8A6B2E; }

  .reveal{ opacity:0; transform:translateY(40px); transition:opacity .8s cubic-bezier(.16,.9,.2,1), transform .8s cubic-bezier(.16,.9,.2,1); }
  .reveal.in{ opacity:1; transform:translateY(0); }

  .btn{ font-family:'Inter'; font-weight:700; font-size:0.9rem; padding:16px 30px; border-radius:4px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; border:1.5px solid var(--navy); cursor:pointer; transition:transform .25s, background .25s, color .25s; }
  .btn-gold{ background:var(--gold); color:var(--navy); border-color:var(--gold); }
  .btn-gold:hover{ transform:translateY(-3px); background:var(--gold-soft); }
  .btn-outline{ background:transparent; color:var(--navy); }
  .btn-outline:hover{ transform:translateY(-3px); background:var(--navy); color:#fff; }
  .btn-dark.on-hero{ background:var(--gold); color:var(--navy); border-color:var(--gold); }
  .btn-dark.on-hero:hover{ transform:translateY(-3px); background:var(--gold-soft); }
  .btn-outline.on-hero{ color:#fff; border-color:rgba(255,255,255,0.5); }
  .btn-outline.on-hero:hover{ background:#fff; color:var(--navy); }

  /* ===== NAV ===== */
  nav{ position:fixed; top:0; left:0; right:0; z-index:80; display:flex; align-items:center; justify-content:space-between; padding:24px 40px; background:linear-gradient(to bottom, rgba(10,20,32,0.85), transparent); transition:background .3s, padding .3s; }
  nav.scrolled{ background:var(--navy-3); padding:14px 40px; box-shadow:0 8px 26px rgba(0,0,0,0.3); }
  .brand{ color:#fff; font-family:'Space Grotesk'; font-weight:700; font-size:1.35rem; text-decoration:none; letter-spacing:-0.02em; }
  .brand span{ color:var(--gold-soft); }
  .nav-right{ display:flex; align-items:center; gap:28px; }
  .nav-links{ display:flex; gap:28px; list-style:none; }
  .nav-links a{ color:rgba(255,255,255,0.85); text-decoration:none; font-size:0.84rem; font-weight:600; }
  .nav-links a:hover{ color:var(--gold-soft); }
  .nav-book{ padding:10px 20px; font-size:0.78rem; }
  @media (max-width:860px){ .nav-links{ display:none; } nav{ padding:16px 20px; } }

  /* ===== HERO ===== */
  .hero{ min-height:100vh; position:relative; display:flex; align-items:center; padding-top:100px; color:#fff; overflow:hidden;
    background:
      radial-gradient(1200px 700px at 15% -10%, rgba(201,161,90,0.14), transparent 55%),
      linear-gradient(160deg, var(--navy-3) 0%, var(--navy) 55%, var(--navy-2) 100%);
  }
  .hero-lines{ position:absolute; inset:0; pointer-events:none; opacity:0.5; background-image: repeating-linear-gradient(90deg, transparent 0 89px, rgba(201,161,90,0.15) 89px 90px); mask-image:linear-gradient(180deg, transparent, black 30%, black 70%, transparent); }
  .hero-inner{ position:relative; z-index:2; width:100%; }
  .hero-grid{ display:grid; grid-template-columns:1.25fr 0.75fr; gap:40px; align-items:center; }
  @media (max-width:900px){ .hero-grid{ grid-template-columns:1fr; } }
  .hero h1{ font-size:clamp(3rem,7.6vw,5.6rem); }
  .hero h1 span{ color:var(--gold-soft); }
  .hero p.lead{ max-width:500px; margin-top:22px; font-size:1.05rem; color:rgba(244,241,234,0.78); }
  .hero-actions{ display:flex; gap:14px; margin-top:38px; flex-wrap:wrap; }
  .rating-badge{ margin-top:42px; display:inline-flex; align-items:center; gap:14px; border:1px solid rgba(201,161,90,0.4); padding:14px 20px; border-radius:6px; backdrop-filter:blur(4px); }
  .rating-badge .num{ font-family:'Space Grotesk'; font-weight:700; font-size:1.6rem; color:var(--gold-soft); }
  .rating-badge .lbl{ font-family:'IBM Plex Mono'; font-size:0.66rem; letter-spacing:0.08em; text-transform:uppercase; color:rgba(244,241,234,0.55); }
  .hero-emblem{ display:flex; justify-content:center; align-items:center; }
  .hero-emblem svg{ width:100%; max-width:280px; opacity:0.9; }
  @media (max-width:900px){ .hero-emblem{ display:none; } }

  /* ===== MARQUEE ===== */
  .marquee-strip{ background:var(--navy-3); padding:20px 0; overflow:hidden; white-space:nowrap; border-top:1px solid rgba(201,161,90,0.25); border-bottom:1px solid rgba(201,161,90,0.25); }
  .marquee-track{ display:inline-flex; gap:50px; animation:marquee 24s linear infinite; }
  .marquee-track span{ font-family:'Space Grotesk'; font-weight:600; font-size:1.05rem; color:var(--gold-soft); display:flex; align-items:center; gap:50px; text-transform:uppercase; letter-spacing:0.02em; }
  .marquee-track span::after{ content:'◆'; font-size:0.6rem; color:var(--gold); margin-left:50px; }
  @keyframes marquee{ from{ transform:translateX(0); } to{ transform:translateX(-50%); } }

  /* ===== ABOUT ===== */
  .about-grid{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:70px; align-items:center; }
  @media (max-width:880px){ .about-grid{ grid-template-columns:1fr; gap:36px; } }
  .about h2{ font-size:clamp(2.1rem,4.4vw,3rem); margin:16px 0 20px; }
  .about p{ color:var(--ink-soft); max-width:54ch; }
  .amenity-list{ display:flex; flex-direction:column; }
  .amenity{ display:flex; align-items:center; gap:16px; padding:20px 0; border-bottom:1px solid var(--line); }
  .amenity:first-child{ border-top:1px solid var(--line); }
  .amenity .ic{ width:26px; height:26px; color:var(--gold); flex-shrink:0; }
  .amenity .name{ font-family:'Space Grotesk'; font-weight:600; font-size:1.02rem; }
  .stat-row{ display:flex; gap:0; margin-top:40px; border-top:1px solid var(--line); }
  .stat-row .stat{ flex:1; padding:20px 20px 0 0; border-right:1px solid var(--line); }
  .stat-row .stat:last-child{ border-right:none; }
  .stat-row .num{ font-family:'Space Grotesk'; font-weight:700; font-size:2rem; color:var(--navy); }
  .stat-row .lbl{ font-family:'IBM Plex Mono'; font-size:0.64rem; letter-spacing:0.08em; text-transform:uppercase; color:var(--ink-soft); margin-top:4px; }

  /* ===== ROOMS / PRICE ===== */
  .rooms{ background:var(--navy); color:#fff; }
  .rooms h2{ color:#fff; font-size:clamp(2.1rem,4.4vw,3rem); margin:16px 0 50px; max-width:16ch; }
  .price-card{ background:linear-gradient(135deg, var(--navy-2), var(--navy-3)); border:1px solid rgba(201,161,90,0.3); border-radius:12px; padding:44px; box-shadow:var(--shadow); display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center; }
  @media (max-width:700px){ .price-card{ grid-template-columns:1fr; text-align:center; } }
  .price-card .range{ font-family:'Space Grotesk'; font-weight:700; font-size:clamp(2rem,5vw,3.2rem); color:var(--gold-soft); }
  .price-card .range small{ font-family:'Inter'; font-size:0.9rem; color:rgba(244,241,234,0.6); display:block; margin-top:6px; font-weight:400; }
  .price-note{ color:rgba(244,241,234,0.7); margin-top:14px; max-width:44ch; }
  .feature-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:22px; margin-top:50px; }
  @media (max-width:760px){ .feature-grid{ grid-template-columns:1fr; } }
  .feature-card{ border:1px solid rgba(201,161,90,0.25); border-radius:10px; padding:28px; }
  .feature-card .ic{ width:32px; height:32px; color:var(--gold-soft); margin-bottom:16px; }
  .feature-card h3{ font-size:1.15rem; color:#fff; margin-bottom:8px; }
  .feature-card p{ color:rgba(244,241,234,0.65); font-size:0.9rem; }

  /* ===== LOCATION ===== */
  .location{ background:var(--bg); }
  .loc-grid{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:70px; align-items:start; }
  @media (max-width:880px){ .loc-grid{ grid-template-columns:1fr; gap:40px; } }
  .loc-list{ margin-top:24px; }
  .loc-item{ display:flex; gap:18px; padding:18px 0; border-bottom:1px solid var(--line); align-items:flex-start; }
  .loc-item:first-child{ border-top:1px solid var(--line); }
  .loc-dist{ font-family:'IBM Plex Mono'; font-size:0.78rem; color:var(--gold); min-width:80px; font-weight:600; }
  .loc-name{ font-family:'Space Grotesk'; font-weight:600; font-size:1.02rem; }
  .addr-block{ background:var(--navy); color:#fff; border-radius:12px; padding:38px; box-shadow:var(--shadow); }
  .addr-block h3{ color:#fff; font-size:1.4rem; margin:14px 0 6px; }
  .addr-block p{ color:rgba(244,241,234,0.72); }
  .addr-block a{ color:var(--gold-soft); text-decoration:none; }
  .addr-block .map-btn{ margin-top:24px; }
  .map-card{ border-radius:10px; overflow:hidden; box-shadow:var(--shadow); margin-top:26px; }
  .map-card iframe{ width:100%; height:280px; border:0; filter:grayscale(0.3) sepia(0.1); }

  /* ===== REVIEWS ===== */
  .reviews{ background:var(--navy-2); color:#fff; }
  .reviews h2{ color:#fff; font-size:clamp(2.1rem,4.4vw,3rem); margin:16px 0 24px; }
  .sentiment-row{ display:flex; flex-wrap:wrap; gap:12px; margin-bottom:50px; }
  .sentiment-chip{ font-family:'IBM Plex Mono'; font-size:0.72rem; padding:9px 16px; border-radius:100px; border:1px solid rgba(201,161,90,0.35); color:rgba(244,241,234,0.85); }
  .sentiment-chip b{ color:var(--gold-soft); }
  .review-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:24px; }
  @media (max-width:900px){ .review-grid{ grid-template-columns:1fr; } }
  .review-card{ background:var(--navy-3); border:1px solid rgba(201,161,90,0.2); border-radius:10px; padding:30px; }
  .review-card .stars{ color:var(--gold); font-size:0.9rem; letter-spacing:2px; }
  .review-card p{ margin:16px 0 20px; color:rgba(244,241,234,0.82); font-size:0.94rem; }
  .review-card .who{ font-family:'IBM Plex Mono'; font-size:0.68rem; text-transform:uppercase; letter-spacing:0.06em; color:rgba(244,241,234,0.45); }

  /* ===== BOOK / CONTACT ===== */
  .book{ background:var(--bg); text-align:center; }
  .book h2{ font-size:clamp(2.3rem,6vw,4rem); margin:18px 0 18px; }
  .book p{ color:var(--ink-soft); max-width:48ch; margin:0 auto; }
  .book-actions{ display:flex; gap:16px; justify-content:center; margin-top:36px; flex-wrap:wrap; }
  .contact-strip{ display:flex; justify-content:center; gap:40px; margin-top:44px; flex-wrap:wrap; }
  .contact-item{ text-align:left; }
  .contact-item .k{ font-family:'IBM Plex Mono'; font-size:0.65rem; letter-spacing:0.1em; text-transform:uppercase; color:#8A6B2E; }
  .contact-item a{ display:block; font-family:'Space Grotesk'; font-weight:600; font-size:1.05rem; color:var(--ink); text-decoration:none; margin-top:6px; }
  .contact-item a:hover{ color:var(--navy); }

  footer{ background:var(--navy-3); color:rgba(244,241,234,0.5); padding:32px 0; font-size:0.8rem; display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; }
  footer a{ color:rgba(244,241,234,0.75); text-decoration:none; }
  footer a:hover{ color:var(--gold-soft); }

  @media (prefers-reduced-motion: reduce){
    .reveal{ transition:none; opacity:1; transform:none; }
    .marquee-track{ animation:none; }
    html{ scroll-behavior:auto; }
  }
</style>
</head>
<body>

<nav id="nav">
  <a class="brand" href="#top">Hamilton <span>Hotel</span></a>
  <div class="nav-right">
    <ul class="nav-links">
      <li><a href="#about">Biz haqimizda</a></li>
      <li><a href="#rooms">Narxlar</a></li>
      <li><a href="#location">Manzil</a></li>
      <li><a href="#reviews">Fikrlar</a></li>
    </ul>
    <a class="btn btn-gold nav-book" href="#book">Bron qilish</a>
  </div>
</nav>

<header class="hero" id="top">
  <div class="hero-lines"></div>
  <div class="wrap hero-inner">
    <div class="hero-grid">
      <div>
        <div class="eyebrow reveal">Toshkent · Qoraqum 1-tor koʻchasi, 42</div>
        <h1 class="reveal">Hamilton <span>Hotel</span></h1>
        <p class="lead reveal">Toʻqimachilik institutiga yaqin, tinch koʻchada joylashgan mehmonxona — do‘stona xodimlar va yoqimli muhit bilan.</p>
        <div class="hero-actions reveal">
          <a class="btn btn-dark on-hero" href="#rooms">Narxlarni koʻrish</a>
          <a class="btn btn-outline on-hero" href="tel:+998955151517">📞 Qoʻngʻiroq qilish</a>
        </div>
        <div class="rating-badge reveal">
          <div class="num">4.7</div>
          <div>
            <div class="lbl">189 ta baho</div>
            <div class="lbl" style="color:var(--gold-soft)">★★★★★</div>
          </div>
        </div>
      </div>
      <div class="hero-emblem reveal">
        <svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="100" cy="100" r="94" stroke="#C9A15A" stroke-width="1"/>
          <circle cx="100" cy="100" r="74" stroke="#C9A15A" stroke-width="0.6" opacity="0.6"/>
          <path d="M60 130V70h14v24h32V70h14v60h-14v-24H74v24H60z" fill="#E3C889"/>
        </svg>
      </div>
    </div>
  </div>
</header>

<div class="marquee-strip">
  <div class="marquee-track">
    <span>Bepul avtoturargoh</span><span>Xonada konditsioner</span><span>4.7 reyting</span><span>Kun-u tun qabul</span><span>Do‘stona xodimlar</span><span>Bepul avtoturargoh</span><span>Xonada konditsioner</span><span>4.7 reyting</span><span>Kun-u tun qabul</span><span>Do‘stona xodimlar</span>
  </div>
</div>

<section class="about" id="about">
  <div class="wrap about-grid">
    <div class="reveal">
      <div class="eyebrow on-light">Biz haqimizda</div>
      <h2>Tinch koʻchada, samimiy xizmat</h2>
      <p>Hamilton Hotel — Toʻqimachilik institutiga piyoda masofada, tinch koʻchada joylashgan 3 yulduzli mehmonxona. Mehmonlar xodimlarning samimiyligi va yordamga tayyorligini alohida ta’kidlashadi — ayniqsa ro‘yxatdan o‘tish va kundalik ehtiyojlarda. Xonalar keng, balandligi baland, deraz oynalari tinch koʻchaga qaraydi.</p>
      <div class="stat-row">
        <div class="stat"><div class="num">4.7</div><div class="lbl">Reyting</div></div>
        <div class="stat"><div class="num">3★</div><div class="lbl">Toifa</div></div>
        <div class="stat"><div class="num">24/7</div><div class="lbl">Qabul xizmati</div></div>
      </div>
    </div>
    <div class="reveal">
      <div class="amenity-list">
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 10l9-7 9 7"/><path d="M5 9v11h14V9"/></svg><span class="name">Kun-u tun ishlaydi</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="7" width="18" height="12" rx="2"/><circle cx="8" cy="13" r="1.5"/></svg><span class="name">Avtoturargoh mavjud</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M10 4v16"/></svg><span class="name">Xonada konditsioner</span></div>
        <div class="amenity"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 3v18M5 8l7-5 7 5M5 8v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8"/></svg><span class="name">Toʻqimachilik institutiga 93 m</span></div>
      </div>
    </div>
  </div>
</section>

<section class="rooms" id="rooms">
  <div class="wrap">
    <div class="eyebrow reveal">Narxlar</div>
    <h2 class="reveal">Har xil byudjetga mos xonalar</h2>
    <div class="price-card reveal">
      <div>
        <div class="range">300 000 – 800 000<small>so‘m / kecha, xona toifasiga qarab</small></div>
        <p class="price-note">Aniq xona toifalari (Standard, Comfort, Lux) va bo‘sh joylar haqida eng so‘nggi ma’lumot uchun bevosita qo‘ng‘iroq qiling yoki Telegram orqali yozing.</p>
      </div>
      <a class="btn btn-gold" href="tel:+998955151517">Narxlarni aniqlashtirish</a>
    </div>
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

<section class="location" id="location">
  <div class="wrap loc-grid">
    <div class="reveal">
      <div class="eyebrow on-light">Joylashuv</div>
      <h2 style="font-size:clamp(2.1rem,4.4vw,3rem); margin:16px 0 6px;">Metro va markazga yaqin</h2>
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
      <div class="eyebrow">Manzil</div>
      <h3>Qoraqum 1-tor koʻchasi, 42</h3>
      <p>Toshkent shahri</p>
      <p style="margin-top:18px;">☎ <a href="tel:+998955151517">+998 95 515 15 17</a></p>
      <p>💬 <a href="https://t.me/+998955151517" target="_blank" rel="noopener">Telegram orqali yozish</a></p>
      <a class="btn btn-gold map-btn" href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" rel="noopener">Yandex Xaritada koʻrish</a>
    </div>
  </div>
</section>

<section class="reviews" id="reviews">
  <div class="wrap">
    <div class="eyebrow reveal">Mehmonlar fikri</div>
    <h2 class="reveal">189 ta bahoga asoslangan reyting — 4.7</h2>
    <div class="sentiment-row reveal">
      <div class="sentiment-chip">Xodimlar xizmati — <b>81% musbat</b></div>
      <div class="sentiment-chip">Muhit — <b>92% musbat</b></div>
      <div class="sentiment-chip">Tozalik — <b>41% musbat</b></div>
    </div>
    <div class="review-grid">
      <div class="review-card reveal">
        <div class="stars">★★★★★</div>
        <p>“Yoqimli va e’tiborli xodimlar. Ro‘yxatdan o‘tishda va kundalik masalalarda yordam berishdi. Kенг oynalar, baland shift, tinch koʻchaga qaragan.”</p>
        <div class="who">Anastasia D. · 19-may</div>
      </div>
      <div class="review-card reveal">
        <div class="stars">★★★★★</div>
        <p>“10 kun dam oldik — toza, qulay. Resepshndagi Alisher alohida yordamga tayyor edi. Nonushtalar xilma-xil, xonalarda tinch. Yana kelamiz.”</p>
        <div class="who">Rezeda G. · 2-iyun</div>
      </div>
      <div class="review-card reveal">
        <div class="stars">★★★★☆</div>
        <p>“Umuman yaxshi mehmonxona, yotoq qulay, choyshablar toza va tabiiy matodan. Joylashuvi va xodimlarning muomalasi ijobiy taassurot qoldirdi.”</p>
        <div class="who">Anastasiya L. · 19-aprel</div>
      </div>
    </div>
  </div>
</section>

<section class="book" id="book">
  <div class="wrap">
    <div class="eyebrow" style="justify-content:center">Bron qilish</div>
    <h2>Joyingizni band qiling</h2>
    <p>Bron qilish yoki savollaringiz uchun telefon orqali qo‘ng‘iroq qiling yoki Telegram orqali yozing — xodimlarimiz kun-u tun javob berishga tayyor.</p>
    <div class="book-actions">
      <a class="btn btn-gold" href="tel:+998955151517">📞 +998 95 515 15 17</a>
      <a class="btn btn-outline" href="https://t.me/+998955151517" target="_blank" rel="noopener">💬 Telegram</a>
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

<script>
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => nav.classList.toggle('scrolled', window.scrollY > 40));
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
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


@app.route("/book")
def book():
    return redirect("/#book")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
