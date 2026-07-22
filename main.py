"""
Hamilton Hotel Tashkent — Flask ilovasi (v3, Ultra 360deg Redesign)
Ishga tushirish: pip install flask --break-system-packages && python main.py
"""

from flask import Flask, redirect

app = Flask(__name__)

INDEX_HTML = """<!DOCTYPE html>
<html lang="uz" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Hamilton Hotel Tashkent — Premium Stay</title>

  <!-- Google Fonts & Tailwind CSS CDN -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome Icons & GSAP -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #080A0F;
      color: #F3F4F6;
    }
    h1, h2, h3, .font-heading {
      font-family: 'Space Grotesk', sans-serif;
    }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #080A0F; }
    ::-webkit-scrollbar-thumb { background: #DC2626; border-radius: 3px; }

    .glass-card {
      background: rgba(17, 24, 39, 0.6);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .glass-card-hover {
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card-hover:hover {
      transform: translateY(-4px);
      border-color: rgba(220, 38, 38, 0.4);
      box-shadow: 0 20px 40px -15px rgba(220, 38, 38, 0.2);
    }
    .neon-glow {
      box-shadow: 0 0 50px -10px rgba(220, 38, 38, 0.3);
    }
  </style>
</head>
<body class="overflow-x-hidden selection:bg-red-600 selection:text-white">

  <!-- SCROLL PROGRESS -->
  <div id="progress" class="fixed top-0 left-0 h-1 bg-gradient-to-r from-red-600 to-rose-500 z-50 transition-all duration-150" style="width: 0%"></div>

  <!-- NAVIGATION -->
  <header class="fixed top-0 left-0 right-0 z-40 px-4 sm:px-8 py-4">
    <nav class="max-w-7xl mx-auto glass-card rounded-2xl px-6 py-3.5 flex items-center justify-between shadow-2xl">
      <a href="#top" class="flex items-center gap-3 group">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-red-600 to-rose-500 flex items-center justify-center text-white font-black text-xl shadow-lg shadow-red-600/30 group-hover:scale-105 transition-transform">
          H
        </div>
        <span class="font-heading font-bold text-xl tracking-wider text-white">HAMILTON<span class="text-red-500">.</span></span>
      </a>

      <ul class="hidden md:flex items-center gap-8 text-sm font-semibold text-gray-300">
        <li><a href="#about" class="hover:text-red-500 transition-colors">Biz Haqimizda</a></li>
        <li><a href="#rooms" class="hover:text-red-500 transition-colors">Narxlar</a></li>
        <li><a href="#location" class="hover:text-red-500 transition-colors">Manzil</a></li>
        <li><a href="#reviews" class="hover:text-red-500 transition-colors">Fikrlar</a></li>
        <li><a href="#faq" class="hover:text-red-500 transition-colors">FAQ</a></li>
      </ul>

      <a href="#book" class="bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-bold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-lg shadow-red-600/25 hover:shadow-red-600/40 transition-all transform hover:-translate-y-0.5">
        Bron Qilish
      </a>
    </nav>
  </header>

  <!-- HERO SECTION -->
  <section id="top" class="min-h-screen relative flex items-center justify-center pt-28 pb-16 px-4 sm:px-8 overflow-hidden">
    <!-- Ambient Lights -->
    <div class="absolute top-1/4 -left-32 w-96 h-96 bg-red-600/20 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-1/4 -right-32 w-96 h-96 bg-rose-600/15 rounded-full blur-[120px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto w-full grid lg:grid-cols-12 gap-12 items-center relative z-10">
      <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-card text-red-400 text-xs font-semibold tracking-wider uppercase border border-red-500/20">
          <i class="fa-solid fa-location-dot"></i>
          <span>Toshkent · Qoraqum 1-tor koʻchasi, 42</span>
        </div>

        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight leading-none text-white font-heading">
          Shinam va Tinch <br>
          <span class="bg-gradient-to-r from-red-500 via-rose-400 to-amber-400 bg-clip-text text-transparent">
            Hamilton Hotel
          </span>
        </h1>

        <p class="text-gray-400 text-base sm:text-lg max-w-xl mx-auto lg:mx-0 font-light leading-relaxed">
          Toʻqimachilik institutiga yaqin, tinch koʻchada joylashgan shinam mehmonxona. Samimiy xodimlar va 24/7 oliy darajadagi xizmat.
        </p>

        <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-4">
          <a href="#rooms" class="bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-bold px-7 py-3.5 rounded-xl shadow-xl shadow-red-600/30 transition-all transform hover:-translate-y-1">
            Narxlarni Ko'rish
          </a>
          <a href="tel:+998955151517" class="glass-card hover:bg-white/10 text-white font-semibold px-7 py-3.5 rounded-xl transition-all border border-white/10">
            <i class="fa-solid fa-phone mr-2 text-red-500"></i>Qoʻngʻiroq Qilish
          </a>
        </div>
      </div>

      <!-- Rating Badge Card -->
      <div class="lg:col-span-5 flex justify-center">
        <div class="glass-card p-8 rounded-3xl neon-glow border border-white/10 w-full max-w-md text-center space-y-6">
          <div class="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-tr from-red-600/20 to-rose-500/20 border border-red-500/30 text-red-500 text-3xl font-black">
            4.7
          </div>
          <div>
            <div class="text-yellow-400 text-lg space-x-1 mb-1">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <h3 class="text-xl font-bold text-white">A'lo Darajadagi Reyting</h3>
            <p class="text-gray-400 text-sm mt-1">189 ta real mehmonlar fikri asosida</p>
          </div>
          <div class="grid grid-cols-2 gap-4 pt-4 border-t border-white/10 text-left">
            <div>
              <span class="text-xs text-gray-500 block uppercase">Xizmat Ko'rsatish</span>
              <span class="text-sm font-bold text-red-400">81% Musbat</span>
            </div>
            <div>
              <span class="text-xs text-gray-500 block uppercase">Umumiy Muhit</span>
              <span class="text-sm font-bold text-red-400">92% Musbat</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MARQUEE STRIP -->
  <div class="bg-gradient-to-r from-red-700 via-red-600 to-rose-700 py-3 overflow-hidden shadow-lg">
    <div class="flex space-x-12 whitespace-nowrap animate-marquee text-white font-bold text-sm tracking-wider uppercase">
      <span><i class="fa-solid fa-square-parking mr-2"></i> Bepul Avtoturargoh</span>
      <span><i class="fa-solid fa-snowflake mr-2"></i> Konditsioner</span>
      <span><i class="fa-solid fa-star mr-2"></i> 4.7 Reyting</span>
      <span><i class="fa-solid fa-clock mr-2"></i> 24/7 Qabul</span>
      <span><i class="fa-solid fa-heart mr-2"></i> Do‘stona Xodimlar</span>
      <span><i class="fa-solid fa-square-parking mr-2"></i> Bepul Avtoturargoh</span>
      <span><i class="fa-solid fa-snowflake mr-2"></i> Konditsioner</span>
      <span><i class="fa-solid fa-star mr-2"></i> 4.7 Reyting</span>
    </div>
  </div>

  <!-- ABOUT SECTION -->
  <section id="about" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="space-y-6">
        <span class="text-red-500 font-semibold text-xs tracking-widest uppercase">Biz Haqimizda</span>
        <h2 class="text-3xl sm:text-5xl font-bold font-heading leading-tight">Tinch Koʻchada, <br>Samimiy Xizmat</h2>
        <p class="text-gray-400 leading-relaxed font-light">
          Hamilton Hotel — Toʻqimachilik institutiga piyoda masofada, tinch koʻchada joylashgan 3 yulduzli mehmonxona. Mehmonlarimiz xodimlarning samimiyligi va yordamga tayyorligini alohida ta’kidlashadi.
        </p>

        <div class="grid grid-cols-3 gap-4 pt-4">
          <div class="glass-card p-4 rounded-2xl text-center">
            <span class="text-2xl sm:text-3xl font-extrabold text-red-500 font-heading">4.7</span>
            <span class="block text-xs text-gray-400 uppercase mt-1">Reyting</span>
          </div>
          <div class="glass-card p-4 rounded-2xl text-center">
            <span class="text-2xl sm:text-3xl font-extrabold text-red-500 font-heading">3★</span>
            <span class="block text-xs text-gray-400 uppercase mt-1">Toifa</span>
          </div>
          <div class="glass-card p-4 rounded-2xl text-center">
            <span class="text-2xl sm:text-3xl font-extrabold text-red-500 font-heading">24/7</span>
            <span class="block text-xs text-gray-400 uppercase mt-1">Servis</span>
          </div>
        </div>
      </div>

      <div class="grid sm:grid-cols-2 gap-4">
        <div class="glass-card glass-card-hover p-6 rounded-2xl space-y-3">
          <i class="fa-solid fa-clock-rotate-left text-3xl text-red-500"></i>
          <h3 class="font-bold text-lg">Kun-u Tun Ishlaydi</h3>
          <p class="text-xs text-gray-400">Istalgan vaqtda cheklovsiz kirish va chiqish imkoniyati.</p>
        </div>
        <div class="glass-card glass-card-hover p-6 rounded-2xl space-y-3">
          <i class="fa-solid fa-square-parking text-3xl text-red-500"></i>
          <h3 class="font-bold text-lg">Avtoturargoh</h3>
          <p class="text-xs text-gray-400">Avtomobilingiz uchun xavfsiz va bepul joylar.</p>
        </div>
        <div class="glass-card glass-card-hover p-6 rounded-2xl space-y-3">
          <i class="fa-solid fa-wind text-3xl text-red-500"></i>
          <h3 class="font-bold text-lg">Konditsioner</h3>
          <p class="text-xs text-gray-400">Har bir xonada zamonaviy iqlim nazorati tizimi.</p>
        </div>
        <div class="glass-card glass-card-hover p-6 rounded-2xl space-y-3">
          <i class="fa-solid fa-graduation-cap text-3xl text-red-500"></i>
          <h3 class="font-bold text-lg">Institutga 93 m</h3>
          <p class="text-xs text-gray-400">Toʻqimachilik institutidan bir necha qadam masofada.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ROOMS & PRICING -->
  <section id="rooms" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
    <div class="text-center space-y-4 mb-12">
      <span class="text-red-500 font-semibold text-xs tracking-widest uppercase">Xonalar & Narxlar</span>
      <h2 class="text-3xl sm:text-5xl font-bold font-heading">Har Xil Byudjetga Mos Xonalar</h2>
    </div>

    <!-- TABS BUTTONS -->
    <div class="flex justify-center gap-3 mb-8">
      <button onclick="switchTab('standard')" id="btn-standard" class="tab-btn bg-red-600 text-white font-bold px-6 py-2.5 rounded-xl text-sm transition-all shadow-lg">Standard</button>
      <button onclick="switchTab('comfort')" id="btn-comfort" class="tab-btn glass-card text-gray-400 hover:text-white font-bold px-6 py-2.5 rounded-xl text-sm transition-all">Comfort</button>
      <button onclick="switchTab('lux')" id="btn-lux" class="tab-btn glass-card text-gray-400 hover:text-white font-bold px-6 py-2.5 rounded-xl text-sm transition-all">Lux</button>
    </div>

    <!-- TAB PANELS -->
    <div class="max-w-3xl mx-auto">
      <div id="panel-standard" class="tab-panel glass-card p-8 rounded-3xl border border-white/10 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
          <div>
            <span class="text-xs text-gray-400 uppercase tracking-wider">Kechasi uchun</span>
            <div class="text-3xl font-extrabold text-red-400 font-heading">300 000 – 450 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
          </div>
          <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-bold px-6 py-3 rounded-xl text-sm text-center transition-all">
            Narxni Aniqlashtirish
          </a>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed">Ixcham va qulay xona — yakka yoki juftlik uchun ideal tanlov. Konditsioner va tinch koʻchaga qaragan derazalar bilan ta'minlangan.</p>
      </div>

      <div id="panel-comfort" class="tab-panel hidden glass-card p-8 rounded-3xl border border-white/10 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
          <div>
            <span class="text-xs text-gray-400 uppercase tracking-wider">Kechasi uchun</span>
            <div class="text-3xl font-extrabold text-red-400 font-heading">450 000 – 650 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
          </div>
          <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-bold px-6 py-3 rounded-xl text-sm text-center transition-all">
            Narxni Aniqlashtirish
          </a>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed">Kengroq xona, qo‘shimcha qulayliklar va yumshoq mebellar bilan — oilaviy yoki xizmat safari bilan kelganlar uchun.</p>
      </div>

      <div id="panel-lux" class="tab-panel hidden glass-card p-8 rounded-3xl border border-white/10 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-6">
          <div>
            <span class="text-xs text-gray-400 uppercase tracking-wider">Kechasi uchun</span>
            <div class="text-3xl font-extrabold text-red-400 font-heading">650 000 – 800 000 <span class="text-sm font-normal text-gray-400">so'm</span></div>
          </div>
          <a href="https://t.me/+998955151517" target="_blank" class="bg-red-600 hover:bg-red-500 text-white font-bold px-6 py-3 rounded-xl text-sm text-center transition-all">
            Narxni Aniqlashtirish
          </a>
        </div>
        <p class="text-gray-300 text-sm leading-relaxed">Eng yuqori toifadagi premium xona — maksimal kenglik, yuqori sifatli qulayliklar va premium interyer.</p>
      </div>

      <p class="text-center text-xs text-gray-500 mt-4">* Aniq narx va bo‘sh xonalar uchun Telegram orqali so‘rov yuborishingiz mumkin.</p>
    </div>
  </section>

  <!-- LOCATION & MAP -->
  <section id="location" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
    <div class="grid lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-5 space-y-6">
        <span class="text-red-500 font-semibold text-xs tracking-widest uppercase">Joylashuv</span>
        <h2 class="text-3xl sm:text-5xl font-bold font-heading">Metro va Markazga Yaqin</h2>

        <div class="space-y-4">
          <div class="flex items-center gap-4 glass-card p-4 rounded-xl">
            <i class="fa-solid fa-person-walking text-2xl text-red-500"></i>
            <div>
              <span class="font-bold text-sm block">Toʻqimachilik Instituti Bekati</span>
              <span class="text-xs text-gray-400">Atigi 93 metr masofada</span>
            </div>
          </div>
          <div class="flex items-center gap-4 glass-card p-4 rounded-xl">
            <i class="fa-solid fa-train-subway text-2xl text-red-500"></i>
            <div>
              <span class="font-bold text-sm block">Novza Metro Bekati</span>
              <span class="text-xs text-gray-400">2,17 km uzoqlikda</span>
            </div>
          </div>
          <div class="flex items-center gap-4 glass-card p-4 rounded-xl">
            <i class="fa-solid fa-plane-departure text-2xl text-red-500"></i>
            <div>
              <span class="font-bold text-sm block">Toshkent Aeroporti</span>
              <span class="text-xs text-gray-400">Taqriban ~3 km masofa</span>
            </div>
          </div>
        </div>

        <a href="https://yandex.uz/maps/-/CTVHRWyV" target="_blank" class="inline-block bg-gradient-to-r from-red-600 to-rose-600 text-white font-bold px-6 py-3 rounded-xl text-sm shadow-lg shadow-red-600/20">
          <i class="fa-solid fa-map-location-dot mr-2"></i> Yandex Xaritada O'tish
        </a>
      </div>

      <div class="lg:col-span-7 glass-card p-2 rounded-3xl border border-white/10 overflow-hidden shadow-2xl">
        <iframe src="https://maps.google.com/maps?q=41.281,69.242&z=15&output=embed" class="w-full h-80 sm:h-96 rounded-2xl filter grayscale contrast-125 opacity-80 hover:opacity-100 transition-opacity"></iframe>
      </div>
    </div>
  </section>

  <!-- REVIEWS SLIDER -->
  <section id="reviews" class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-white/5">
    <div class="text-center space-y-4 mb-12">
      <span class="text-red-500 font-semibold text-xs tracking-widest uppercase">Sharhlar</span>
      <h2 class="text-3xl sm:text-5xl font-bold font-heading">Mehmonlarimiz Fikri</h2>
    </div>

    <div class="max-w-3xl mx-auto glass-card p-8 sm:p-12 rounded-3xl border border-white/10 relative text-center">
      <div id="review-slider" class="min-h-[160px] flex items-center justify-center">
        <div class="review-item space-y-4">
          <div class="text-yellow-400"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
          <p class="text-gray-200 text-base sm:text-lg italic">“Yoqimli va e’tiborli xodimlar. Ro‘yxatdan o‘tishda va kundalik masalalarda yordam berishdi. Keng oynalar, baland shift, tinch koʻchaga qaragan.”</p>
          <span class="block text-xs font-bold text-red-400 uppercase tracking-wider">Anastasia D. · 19-may</span>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ ACCORDION -->
  <section id="faq" class="py-24 px-4 sm:px-8 max-w-4xl mx-auto border-t border-white/5">
    <div class="text-center space-y-4 mb-12">
      <span class="text-red-500 font-semibold text-xs tracking-widest uppercase">FAQ</span>
      <h2 class="text-3xl sm:text-5xl font-bold font-heading">Ko'p So'raladigan Savollar</h2>
    </div>

    <div class="space-y-4">
      <div class="glass-card rounded-2xl p-6 border border-white/10 cursor-pointer" onclick="toggleFaq(this)">
        <div class="flex justify-between items-center">
          <h3 class="font-bold text-lg">Mehmonxona necha soat ishlaydi?</h3>
          <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
        </div>
        <p class="text-gray-400 text-sm mt-3 hidden">Hamilton Hotel kun-u tun (24/7) ishlaydi — istalgan vaqtda kirish va chiqish mumkin, qabul xizmati doim faol.</p>
      </div>

      <div class="glass-card rounded-2xl p-6 border border-white/10 cursor-pointer" onclick="toggleFaq(this)">
        <div class="flex justify-between items-center">
          <h3 class="font-bold text-lg">Avtoturargoh bormi?</h3>
          <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
        </div>
        <p class="text-gray-400 text-sm mt-3 hidden">Ha, mehmonlarimiz uchun xavfsiz va bepul avtoturargoh mavjud.</p>
      </div>

      <div class="glass-card rounded-2xl p-6 border border-white/10 cursor-pointer" onclick="toggleFaq(this)">
        <div class="flex justify-between items-center">
          <h3 class="font-bold text-lg">Qanday bron qilsam bo‘ladi?</h3>
          <i class="fa-solid fa-chevron-down text-red-500 transition-transform"></i>
        </div>
        <p class="text-gray-400 text-sm mt-3 hidden">Telefon orqali qo‘ng‘iroq qiling yoki Telegram orqali yozing — xodimlarimiz 24/7 javob berishga tayyor.</p>
      </div>
    </div>
  </section>

  <!-- BOOKING CALL TO ACTION -->
  <section id="book" class="py-24 px-4 sm:px-8 max-w-5xl mx-auto text-center">
    <div class="glass-card p-12 rounded-3xl neon-glow border border-red-500/30 space-y-6">
      <h2 class="text-3xl sm:text-5xl font-extrabold font-heading text-white">Xonangizni Hoziroq Band Qiling</h2>
      <p class="text-gray-300 max-w-xl mx-auto text-sm sm:text-base">
        Savollaringiz bormi yoki joy bron qilmoqchimisiz? Biz bilan bog'laning!
      </p>

      <div class="flex flex-wrap justify-center gap-4 pt-4">
        <a href="https://t.me/+998955151517" target="_blank" class="bg-gradient-to-r from-red-600 to-rose-600 text-white font-bold px-8 py-4 rounded-xl shadow-xl shadow-red-600/30 hover:scale-105 transition-transform">
          <i class="fa-brands fa-telegram mr-2"></i> Telegram Orqali Bron
        </a>
        <a href="tel:+998955151517" class="glass-card text-white font-bold px-8 py-4 rounded-xl border border-white/10 hover:bg-white/10 transition-all">
          <i class="fa-solid fa-phone mr-2 text-red-500"></i> +998 95 515 15 17
        </a>
      </div>
    </div>
  </section>

  <!-- FLOATING TELEGRAM BUTTON -->
  <a href="https://t.me/+998955151517" target="_blank" class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-gradient-to-tr from-red-600 to-rose-500 rounded-full flex items-center justify-center text-white text-2xl shadow-xl shadow-red-600/40 hover:scale-110 transition-transform">
    <i class="fa-brands fa-telegram"></i>
  </a>

  <!-- FOOTER -->
  <footer class="border-t border-white/5 py-8 text-center text-xs text-gray-500">
    <p>© Hamilton Hotel — Qoraqum 1-tor koʻchasi, 42, Toshkent. Redesigned Next-Gen Interface.</p>
  </footer>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // Scroll progress bar
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const pct = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
      document.getElementById('progress').style.width = pct + '%';
    });

    // Room Tabs Switcher
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

    // FAQ Accordion
    function toggleFaq(element) {
      const p = element.querySelector('p');
      const icon = element.querySelector('i');
      p.classList.toggle('hidden');
      icon.classList.toggle('rotate-180');
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
