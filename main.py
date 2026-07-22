"""
Hamilton Hotel Tashkent — Flask App (v4, Ultimate 360° Redesign)
Ishga tushirish: pip install flask --break-system-packages && python main.py
"""

from flask import Flask, redirect

app = Flask(__name__)

INDEX_HTML = """<!DOCTYPE html>
<html lang="uz" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Hamilton Hotel Tashkent — Ultimate Cyber-Luxury</title>

  <!-- Google Fonts & Tailwind CSS CDN -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Three.js (3D WebGL Background) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <!-- GSAP & ScrollTrigger -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <!-- Vanilla Tilt (3D Card Effect) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.0/vanilla-tilt.min.js"></script>

  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #030508;
      color: #F3F4F6;
      overflow-x: hidden;
    }
    h1, h2, h3, .font-heading {
      font-family: 'Space Grotesk', sans-serif;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #030508; }
    ::-webkit-scrollbar-thumb { background: #B3231A; border-radius: 3px; }

    /* Custom Kinetic Cursor (Faqat PC da ishlaydi) */
    @media (min-width: 1024px) {
      body { cursor: none; }
      #custom-cursor {
        pointer-events: none;
        position: fixed;
        top: 0; left: 0;
        z-index: 9999;
        transition: transform 0.1s ease-out;
      }
    }
    @media (max-width: 1023px) {
      #custom-cursor { display: none !important; }
      body { cursor: auto !important; }
    }

    /* Cyber Glassmorphism */
    .glass-box {
      background: rgba(12, 16, 24, 0.6);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }
    .glass-box-red {
      background: rgba(179, 35, 26, 0.08);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(179, 35, 26, 0.3);
      box-shadow: 0 0 30px rgba(179, 35, 26, 0.2);
    }
    .neon-text-red {
      text-shadow: 0 0 25px rgba(179, 35, 26, 0.7);
    }
    .glow-border:hover {
      border-color: rgba(179, 35, 26, 0.6);
      box-shadow: 0 0 30px rgba(179, 35, 26, 0.3);
    }
  </style>
</head>
<body class="selection:bg-red-600 selection:text-white">

  <!-- CUSTOM CURSOR -->
  <div id="custom-cursor" class="w-8 h-8 rounded-full border border-red-500/80 flex items-center justify-center -translate-x-1/2 -translate-y-1/2">
    <div class="w-1.5 h-1.5 bg-red-500 rounded-full"></div>
  </div>

  <!-- THREE.JS CANVAS BACKGROUND -->
  <canvas id="webgl-canvas" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"></canvas>

  <!-- SCROLL PROGRESS BAR -->
  <div id="progress" class="fixed top-0 left-0 h-1 bg-gradient-to-r from-red-600 via-rose-500 to-amber-500 z-50 transition-all duration-150" style="width: 0%"></div>

  <!-- MAIN WRAPPER -->
  <div class="relative z-10">

    <!-- NAVBAR -->
    <header class="fixed top-0 left-0 right-0 z-40 px-4 sm:px-8 py-4">
      <nav class="max-w-7xl mx-auto glass-box rounded-2xl px-6 py-3.5 flex items-center justify-between">
        <a href="#top" class="flex items-center gap-3 group">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-red-600 via-rose-600 to-amber-500 flex items-center justify-center text-white font-black text-xl shadow-lg shadow-red-600/30 group-hover:scale-105 transition-transform">
            H
          </div>
          <span class="font-heading font-black text-xl tracking-widest text-white">HAMILTON<span class="text-red-500">.</span></span>
        </a>

        <ul class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-gray-300">
          <li><a href="#about" class="hover:text-red-500 transition-colors">Biz Haqimizda</a></li>
          <li><a href="#rooms" class="hover:text-red-500 transition-colors">Narxlar</a></li>
          <li><a href="#location" class="hover:text-red-500 transition-colors">Manzil</a></li>
          <li><a href="#reviews" class="hover:text-red-500 transition-colors">Sharhlar</a></li>
          <li><a href="#faq" class="hover:text-red-500 transition-colors">FAQ</a></li>
        </ul>

        <a href="#book" class="bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-lg shadow-red-600/30 transition-all transform hover:-translate-y-0.5 uppercase tracking-wider">
          Bron Qilish
        </a>
      </nav>
    </header>

    <!-- HERO SECTION -->
    <section id="top" class="min-h-screen relative flex items-center justify-center pt-28 pb-16 px-4 sm:px-8">
      <div class="max-w-7xl mx-auto w-full grid lg:grid-cols-12 gap-12 items-center hero-content">
        
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-box-red text-red-400 text-xs font-bold tracking-widest uppercase">
            <i class="fa-solid fa-crown text-amber-400"></i>
            <span>Toshkent · Qoraqum 1-tor koʻchasi, 42</span>
          </div>

          <h1 class="text-4xl sm:text-6xl lg:text-8xl font-black tracking-tight leading-none font-heading">
            Sokinlik va <br>
            <span class="bg-gradient-to-r from-red-500 via-rose-300 to-amber-400 bg-clip-text text-transparent neon-text-red">
              Lüks Hordiq
            </span>
          </h1>

          <p class="text-gray-400 text-base sm:text-lg max-w-xl mx-auto lg:mx-0 font-light leading-relaxed">
            Toʻqimachilik institutiga yaqin, shinam va tinch hududda joylashgan mehmonxona. Oliy darajadagi xizmat hamda samimiy xodimlardan bahramand bo'ling.
          </p>

          <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-4">
            <a href="#rooms" class="bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-extrabold px-8 py-4 rounded-xl shadow-xl shadow-red-600/30 transition-all transform hover:-translate-y-1 text-sm tracking-wider uppercase">
              Narxlarni Ko'rish
            </a>
            <a href="tel:+998955151517" class="glass-box hover:bg-white/10 text-white font-bold px-8 py-4 rounded-xl transition-all text-sm uppercase tracking-wider">
              <i class="fa-solid fa-phone mr-2 text-red-500"></i>+998 95 515 15 17
            </a>
          </div>
        </div>

        <!-- Floating Glass Rating Card -->
        <div class="lg:col-span-5 flex justify-center">
          <div class="glass-box p-8 rounded-3xl border border-white/10 w-full max-w-md text-center space-y-6 glow-border" data-tilt>
            <div class="inline-flex items-center justify-center w-24 h-24 rounded-3xl bg-gradient-to-tr from-red-600/30 to-amber-500/20 border border-red-500/40 text-red-400 text-4xl font-black font-heading shadow-xl shadow-red-600/20">
              4.7
            </div>
            <div>
              <div class="text-amber-400 text-xl space-x-1 mb-2">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
              </div>
              <h3 class="text-2xl font-black text-white font-heading">Yuqori Reytingli Mehmonxona</h3>
              <p class="text-gray-400 text-xs mt-1 uppercase tracking-wider">189 ta tasdiqlangan baholar asosida</p>
            </div>
            <div class="grid grid-cols-2 gap-4 pt-6 border-t border-white/10 text-left">
              <div>
                <span class="text-[10px] text-gray-400 block uppercase tracking-widest">Xizmat Sifati</span>
                <span class="text-base font-extrabold text-red-400">81% Musbat</span>
              </div>
              <div>
                <span class="text-[10px] text-gray-400 block uppercase tracking-widest">Atmosfera</span>
                <span class="text-base font-extrabold text-amber-400">92% Musbat</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- MARQUEE STRIP -->
    <div class="bg-gradient-to-r from-red-700 via-rose-700 to-red-800 py-3.5 overflow-hidden shadow-2xl border-y border-white/10">
      <div class="flex space-x-12 whitespace-nowrap animate-marquee text-white font-black text-xs tracking-widest uppercase">
        <span><i class="fa-solid fa-square-parking text-amber-400 mr-2"></i> Bepul Avtoturargoh</span>
        <span><i class="fa-solid fa-snowflake text-amber-400 mr-2"></i> Xonalarda Konditsioner</span>
        <span><i class="fa-solid fa-star text-amber-400 mr-2"></i> 4.7 Reyting</span>
        <span><i class="fa-solid fa-clock text-amber-400 mr-2"></i> 24/7 Qabul Xizmati</span>
        <span><i class="fa-solid fa-heart text-amber-400 mr-2"></i> Samimiy Xodimlar</span>
        <span><i class="fa-solid fa-square-parking text-amber-400 mr-2"></i> Bepul Avtoturargoh</span>
        <span><i class="fa-solid fa-snowflake text-amber-400 mr-2"></i> Xonalarda Konditsioner</span>
      </div>
    </div>

    <!-- ABOUT SECTION -->
    <section id="about" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <span class="text-red-500 font-extrabold text-xs tracking-widest uppercase">Biz Haqimizda</span>
          <h2 class="text-3xl sm:text-5xl font-black font-heading leading-tight">Tinch Koʻchada, <br>Oliy Xizmat</h2>
          <p class="text-gray-400 leading-relaxed font-light text-sm sm:text-base">
            Hamilton Hotel — Toʻqimachilik institutiga atigi bir necha qadam masofada joylashgan 3 yulduzli zamonaviy mehmonxona. Mehmonlarimiz ro‘yxatdan o‘tish va kundalik qulayliklardagi e’tiborimizni yuqori baholashadi.
          </p>

          <div class="grid grid-cols-3 gap-4 pt-4">
            <div class="glass-box p-5 rounded-2xl text-center glow-border" data-tilt>
              <span class="text-3xl font-black text-red-500 font-heading">4.7</span>
              <span class="block text-[10px] text-gray-400 uppercase mt-1 tracking-wider">Yandex Reyting</span>
            </div>
            <div class="glass-box p-5 rounded-2xl text-center glow-border" data-tilt>
              <span class="text-3xl font-black text-amber-400 font-heading">3★</span>
              <span class="block text-[10px] text-gray-400 uppercase mt-1 tracking-wider">Toifa</span>
            </div>
            <div class="glass-box p-5 rounded-2xl text-center glow-border" data-tilt>
              <span class="text-3xl font-black text-emerald-400 font-heading">24/7</span>
              <span class="block text-[10px] text-gray-400 uppercase mt-1 tracking-wider">Rejim</span>
            </div>
          </div>
        </div>

        <div class="grid sm:grid-cols-2 gap-4">
          <div class="glass-box p-6 rounded-3xl space-y-3 glow-border" data-tilt>
            <i class="fa-solid fa-clock-rotate-left text-3xl text-red-500"></i>
            <h3 class="font-bold text-lg font-heading">24/7 Qabul</h3>
            <p class="text-xs text-gray-400 leading-relaxed">Istalgan vaqtda kirish va chiqish qulayligi.</p>
          </div>
          <div class="glass-box p-6 rounded-3xl space-y-3 glow-border" data-tilt>
            <i class="fa-solid fa-square-parking text-3xl text-red-500"></i>
            <h3 class="font-bold text-lg font-heading">Avtoturargoh</h3>
            <p class="text-xs text-gray-400 leading-relaxed">Avtomobilingiz uchun xavfsiz va bepul hudud.</p>
          </div>
          <div class="glass-box p-6 rounded-3xl space-y-3 glow-border" data-tilt>
            <i class="fa-solid fa-wind text-3xl text-red-500"></i>
            <h3 class="font-bold text-lg font-heading">Konditsioner</h3>
            <p class="text-xs text-gray-400 leading-relaxed">Barcha xonalarda iqlim nazorati tizimi.</p>
          </div>
          <div class="glass-box p-6 rounded-3xl space-y-3 glow-border" data-tilt>
            <i class="fa-solid fa-graduation-cap text-3xl text-red-500"></i>
            <h3 class="font-bold text-lg font-heading">Institutga 93 m</h3>
            <p class="text-xs text-gray-400 leading-relaxed">Toʻqimachilik institutiga eng yaqin joylashuv.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ROOMS & PRICING -->
    <section id="rooms" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
      <div class="text-center space-y-4 mb-12">
        <span class="text-red-500 font-extrabold text-xs tracking-widest uppercase">Xonalar & Narxlar</span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading">Sizga Mos Keluvchi Toifalar</h2>
      </div>

      <!-- TABS BUTTONS -->
      <div class="flex justify-center gap-3 mb-8">
        <button onclick="switchTab('standard')" id="btn-standard" class="tab-btn bg-red-600 text-white font-extrabold px-7 py-3 rounded-xl text-xs uppercase tracking-wider transition-all shadow-lg">Standard</button>
        <button onclick="switchTab('comfort')" id="btn-comfort" class="tab-btn glass-card text-gray-400 hover:text-white font-extrabold px-7 py-3 rounded-xl text-xs uppercase tracking-wider transition-all">Comfort</button>
        <button onclick="switchTab('lux')" id="btn-lux" class="tab-btn glass-card text-gray-400 hover:text-white font-extrabold px-7 py-3 rounded-xl text-xs uppercase tracking-wider transition-all">Lux</button>
      </div>

      <!-- TAB PANELS -->
      <div class="max-w-3xl mx-auto">
        <div id="panel-standard" class="tab-panel glass-box p-8 sm:p-10 rounded-3xl border border-white/10 space-y-6 glow-border" data-tilt>
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
            <div>
              <span class="text-[10px] text-gray-400 uppercase tracking-widest">Kechasi uchun</span>
              <div class="text-3xl sm:text-4xl font-black text-red-400 font-heading">300 000 – 450 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
            </div>
            <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-extrabold px-6 py-3.5 rounded-xl text-xs text-center uppercase tracking-wider transition-all shadow-lg shadow-red-600/30">
              Narxni Aniqlashtirish
            </a>
          </div>
          <p class="text-gray-300 text-sm leading-relaxed">Ixcham va nihoyatda qulay xona — yakka yoki juftlik uchun ideal. Konditsioner va tinch koʻchaga qaragan derazalar bilan jihozlangan.</p>
        </div>

        <div id="panel-comfort" class="tab-panel hidden glass-box p-8 sm:p-10 rounded-3xl border border-white/10 space-y-6 glow-border" data-tilt>
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
            <div>
              <span class="text-[10px] text-gray-400 uppercase tracking-widest">Kechasi uchun</span>
              <div class="text-3xl sm:text-4xl font-black text-red-400 font-heading">450 000 – 650 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
            </div>
            <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-extrabold px-6 py-3.5 rounded-xl text-xs text-center uppercase tracking-wider transition-all shadow-lg shadow-red-600/30">
              Narxni Aniqlashtirish
            </a>
          </div>
          <p class="text-gray-300 text-sm leading-relaxed">Kengroq shinam xona, qo‘shimcha qulayliklar bilan — oilaviy dam olish yoki hamkasblar bilan tashrif buyurish uchun.</p>
        </div>

        <div id="panel-lux" class="tab-panel hidden glass-box p-8 sm:p-10 rounded-3xl border border-white/10 space-y-6 glow-border" data-tilt>
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
            <div>
              <span class="text-[10px] text-gray-400 uppercase tracking-widest">Kechasi uchun</span>
              <div class="text-3xl sm:text-4xl font-black text-red-400 font-heading">650 000 – 800 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
            </div>
            <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-extrabold px-6 py-3.5 rounded-xl text-xs text-center uppercase tracking-wider transition-all shadow-lg shadow-red-600/30">
              Narxni Aniqlashtirish
            </a>
          </div>
          <p class="text-gray-300 text-sm leading-relaxed">Eng yuqori premium toifadagi xona — maksimal darajadagi kenglik, hashamatli dizayn va eksklyuziv sharoitlar.</p>
        </div>

        <p class="text-center text-[11px] text-gray-500 mt-4 uppercase tracking-wider">* Narxlar oraliq ko'rinishida berilgan — aniq narxlar va bo'sh xonalarni Telegram orqali biling.</p>
      </div>
    </section>

    <!-- LOCATION & MAP -->
    <section id="location" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-5 space-y-6">
          <span class="text-red-500 font-extrabold text-xs tracking-widest uppercase">Joylashuv</span>
          <h2 class="text-3xl sm:text-5xl font-black font-heading">Metro va Aeroportga Yaqin</h2>

          <div class="space-y-4">
            <div class="flex items-center gap-4 glass-box p-4 rounded-2xl glow-border">
              <i class="fa-solid fa-person-walking text-2xl text-red-500"></i>
              <div>
                <span class="font-extrabold text-sm block">Toʻqimachilik Instituti Bekati</span>
                <span class="text-xs text-gray-400">Atigi 93 metr masofada</span>
              </div>
            </div>
            <div class="flex items-center gap-4 glass-box p-4 rounded-2xl glow-border">
              <i class="fa-solid fa-train-subway text-2xl text-red-500"></i>
              <div>
                <span class="font-extrabold text-sm block">Novza Metro Bekati</span>
                <span class="text-xs text-gray-400">2,17 km uzoqlikda</span>
              </div>
            </div>
            <div class="flex items-center gap-4 glass-box p-4 rounded-2xl glow-border">
              <i class="fa-solid fa-plane-departure text-2xl text-red-500"></i>
              <div>
                <span class="font-extrabold text-sm block">Toshkent Aeroporti</span>
                <span class="text-xs text-gray-400">Taqriban ~3 km masofada</span>
              </div>
            </div>
          </div>

          <a href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" class="inline-block bg-gradient-to-r from-red-600 to-rose-600 text-white font-extrabold px-8 py-4 rounded-xl text-xs uppercase tracking-wider shadow-lg shadow-red-600/30">
            <i class="fa-solid fa-map-location-dot mr-2"></i> Yandex Xaritada O'tish
          </a>
        </div>

        <div class="lg:col-span-7 glass-box p-2 rounded-3xl border border-white/10 overflow-hidden glow-border" data-tilt>
          <iframe src="https://maps.google.com/maps?q=41.281,69.242&z=15&output=embed" class="w-full h-80 sm:h-96 rounded-2xl filter grayscale contrast-125 opacity-80 hover:opacity-100 transition-opacity"></iframe>
        </div>
      </div>
    </section>

    <!-- REVIEWS SLIDER -->
    <section id="reviews" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
      <div class="text-center space-y-4 mb-12">
        <span class="text-red-500 font-extrabold text-xs tracking-widest uppercase">Sharhlar</span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading">Mehmonlarimiz Fikri</h2>
      </div>

      <div class="max-w-3xl mx-auto glass-box p-8 sm:p-12 rounded-3xl border border-white/10 text-center glow-border" data-tilt>
        <div id="review-slider" class="min-h-[140px] flex items-center justify-center">
          <div class="review-item space-y-4">
            <div class="text-amber-400"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
            <p class="text-gray-200 text-base sm:text-lg italic leading-relaxed">“Yoqimli va e’tiborli xodimlar. Ro‘yxatdan o‘tishda va kundalik masalalarda yordam berishdi. Keng oynalar, baland shift, tinch koʻchaga qaragan.”</p>
            <span class="block text-xs font-black text-red-400 uppercase tracking-widest">Anastasia D. · 19-may</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ ACCORDION -->
    <section id="faq" class="py-24 px-4 sm:px-8 max-w-4xl mx-auto border-t border-white/5">
      <div class="text-center space-y-4 mb-12">
        <span class="text-red-500 font-extrabold text-xs tracking-widest uppercase">FAQ</span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading">Savollaringiz Bormi?</h2>
      </div>

      <div class="space-y-4">
        <div class="glass-box rounded-2xl p-6 border border-white/10 cursor-pointer glow-border" onclick="toggleFaq(this)">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-base sm:text-lg font-heading">Mehmonxona necha soat ishlaydi?</h3>
            <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
          </div>
          <p class="text-gray-400 text-xs sm:text-sm mt-3 hidden leading-relaxed">Hamilton Hotel kun-u tun (24/7) ishlaydi — istalgan vaqtda kirish va chiqish imkoniyati mavjud.</p>
        </div>

        <div class="glass-box rounded-2xl p-6 border border-white/10 cursor-pointer glow-border" onclick="toggleFaq(this)">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-base sm:text-lg font-heading">Avtoturargoh bormi?</h3>
            <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
          </div>
          <p class="text-gray-400 text-xs sm:text-sm mt-3 hidden leading-relaxed">Ha, mehmonlarimiz uchun xavfsiz va bepul avtoturargoh mavjud.</p>
        </div>

        <div class="glass-box rounded-2xl p-6 border border-white/10 cursor-pointer glow-border" onclick="toggleFaq(this)">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-base sm:text-lg font-heading">Qanday bron qilsam bo‘ladi?</h3>
            <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
          </div>
          <p class="text-gray-400 text-xs sm:text-sm mt-3 hidden leading-relaxed">Telefon orqali qo‘ng‘iroq qiling yoki Telegram orqali yozing — xodimlarimiz 24/7 javob berishadi.</p>
        </div>
      </div>
    </section>

    <!-- BOOKING CALL TO ACTION -->
    <section id="book" class="py-24 px-4 sm:px-8 max-w-5xl mx-auto text-center">
      <div class="glass-box p-10 sm:p-16 rounded-3xl border border-red-500/30 space-y-6 glow-border" data-tilt>
        <h2 class="text-3xl sm:text-6xl font-black font-heading text-white">Xonangizni Band Qiling</h2>
        <p class="text-gray-300 max-w-xl mx-auto text-xs sm:text-base leading-relaxed">
          Savollaringiz bormi yoki joy bron qilmoqchimisiz? Biz bilan hoziroq bog'laning!
        </p>

        <div class="flex flex-wrap justify-center gap-4 pt-4">
          <a href="https://t.me/+998955151517" target="_blank" class="bg-gradient-to-r from-red-600 to-rose-600 text-white font-extrabold px-8 py-4 rounded-xl shadow-xl shadow-red-600/30 hover:scale-105 transition-transform uppercase text-xs tracking-wider">
            <i class="fa-brands fa-telegram mr-2"></i> Telegram Orqali Bron
          </a>
          <a href="tel:+998955151517" class="glass-box text-white font-extrabold px-8 py-4 rounded-xl border border-white/10 hover:bg-white/10 transition-all uppercase text-xs tracking-wider">
            <i class="fa-solid fa-phone mr-2 text-red-500"></i> +998 95 515 15 17
          </a>
        </div>
      </div>
    </section>

    <!-- FLOATING TELEGRAM BUTTON -->
    <a href="https://t.me/+998955151517" target="_blank" class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-gradient-to-tr from-red-600 to-rose-500 rounded-full flex items-center justify-center text-white text-2xl shadow-xl shadow-red-600/50 hover:scale-110 transition-transform">
      <i class="fa-brands fa-telegram"></i>
    </a>

    <!-- FOOTER -->
    <footer class="border-t border-white/5 py-8 text-center text-[10px] uppercase tracking-widest text-gray-500">
      <p>© Hamilton Hotel — Qoraqum 1-tor koʻchasi, 42, Toshkent. Next-Gen 360° Redesign.</p>
    </footer>

  </div>

  <!-- JAVASCRIPT: THREE.JS + GSAP + TILT -->
  <script>
    // 1. KINETIC CURSOR (PC)
    const cursor = document.getElementById('custom-cursor');
    if (window.innerWidth >= 1024) {
      window.addEventListener('mousemove', (e) => {
        cursor.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0) translate(-50%, -50%)`;
      });
    }

    // 2. THREE.JS BACKGROUND
    const canvas = document.getElementById('webgl-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 30;

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Red Cyber Torus Mesh
    const geo = new THREE.TorusKnotGeometry(10, 3, 100, 16);
    const mat = new THREE.MeshBasicMaterial({ color: 0xb3231a, wireframe: true, transparent: true, opacity: 0.18 });
    const torusKnot = new THREE.Mesh(geo, mat);
    scene.add(torusKnot);

    // Particle Field
    const pGeo = new THREE.BufferGeometry();
    const pCount = window.innerWidth < 768 ? 300 : 800;
    const pPos = new Float32Array(pCount * 3);
    for(let i=0; i<pCount*3; i++) {
      pPos[i] = (Math.random() - 0.5) * 100;
    }
    pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
    const pMat = new THREE.PointsMaterial({ size: 0.2, color: 0xf59e0b, transparent: true, opacity: 0.5 });
    const particles = new THREE.Points(pGeo, pMat);
    scene.add(particles);

    // Render loop
    const clock = new THREE.Clock();
    function animate() {
      const t = clock.getElapsedTime();
      torusKnot.rotation.x = t * 0.1;
      torusKnot.rotation.y = t * 0.15;
      particles.rotation.y = -t * 0.05;
      renderer.render(scene, camera);
      requestAnimationFrame(animate);
    }
    animate();

    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // 3. GSAP SCROLLTRIGGER
    gsap.registerPlugin(ScrollTrigger);

    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const pct = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
      document.getElementById('progress').style.width = pct + '%';
    });

    gsap.from(".hero-content > *", {
      opacity: 0,
      y: 50,
      duration: 1.2,
      stagger: 0.15,
      ease: "power4.out"
    });

    // 4. ROOM TABS SWITCHER
    function switchTab(tabName) {
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.remove('bg-red-600', 'text-white', 'shadow-lg');
        b.classList.add('glass-card', 'text-gray-400');
      });

      document.getElementById('panel-' + tabName).classList.remove('hidden');
      const activeBtn = document.getElementById('btn-' + tabName);
      activeBtn.classList.add('bg-red-600', 'text-white', 'shadow-lg');
      activeBtn.classList.remove('glass-card', 'text-gray-400');
    }

    // 5. FAQ ACCORDION
    function toggleFaq(element) {
      const p = element.querySelector('p');
      const icon = element.querySelector('i');
      p.classList.toggle('hidden');
      icon.classList.toggle('rotate-180');
    }

    // 6. VANILLA TILT (Desktop Card Tilt)
    if (window.innerWidth >= 1024) {
      VanillaTilt.init(document.querySelectorAll("[data-tilt]"), {
        max: 10,
        speed: 400,
        glare: true,
        "max-glare": 0.15,
      });
    }
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
