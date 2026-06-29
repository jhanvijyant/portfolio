from flask import Flask, send_file
import io

app = Flask(__name__)

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jhanvi Jyant — Design Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ── TOKENS ── */
:root {
  --linen:     #F5EFE4;
  --linen-2:   #EDE4D5;
  --amber:     #C8763A;
  --amber-dk:  #9E5620;
  --sienna:    #7A3B1E;
  --rose:      #D4907A;
  --rose-lt:   #F0D8CC;
  --ink:       #2A1F17;
  --ink-2:     #5C4033;
  --mist:      #BFB0A0;
  --white:     #FDFAF6;
  --serif:     'Cormorant Garamond', Georgia, serif;
  --sans:      'DM Sans', system-ui, sans-serif;
  
  --shadow-sm: 0 4px 20px rgba(42, 31, 23, 0.03);
  --shadow-md: 0 12px 34px rgba(122, 59, 30, 0.06);
  --shadow-lg: 0 24px 60px rgba(122, 59, 30, 0.12);
  --transition-smooth: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-micro: all 0.25s cubic-bezier(0.25, 1, 0.5, 1);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--linen);
  color: var(--ink);
  font-family: var(--sans);
  font-size: 15px;
  line-height: 1.7;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}

@keyframes fadeInSlideUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes floatBackground {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(4%, 2%) scale(1.05); }
  100% { transform: translate(0, 0) scale(1); }
}

nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 1.5rem 4rem;
  background: rgba(253, 250, 246, 0.75);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(200,118,58,0.1);
  transition: var(--transition-smooth);
}
.nav-logo { 
  font-family: var(--serif); 
  font-size: 22px; 
  font-weight: 600; 
  color: var(--sienna); 
  letter-spacing: 0.02em;
  text-decoration: none;
}
.nav-links { display: flex; list-style: none; align-items: center; }
.nav-links li { margin-left: 2.5rem; }
.nav-links a {
  font-size: 12px; font-weight: 500; color: var(--ink-2); text-decoration: none;
  letter-spacing: 0.08em; text-transform: uppercase; position: relative; padding: 0.5rem 0;
  transition: var(--transition-micro);
}
.nav-links a::after {
  content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 1px;
  background: var(--amber); transform: scaleX(0); transform-origin: right;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.nav-links a:hover { color: var(--amber); }
.nav-links a:hover::after { transform: scaleX(1); transform-origin: left; }

.menu-toggle { display: none; background: none; border: none; cursor: pointer; padding: 0.5rem; z-index: 110; }
.menu-toggle span { display: block; width: 22px; height: 1.5px; background: var(--sienna); margin: 5px 0; transition: var(--transition-micro); }

.hero {
  min-height: 100vh; display: grid; grid-template-columns: 1.1fr 0.9fr; align-items: center;
  padding: 8rem 4rem 4rem; gap: 6rem; position: relative; overflow: hidden;
  animation: fadeInSlideUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.hero::before {
  content: ''; position: absolute; right: -5%; top: 5%; width: 600px; height: 600px;
  border-radius: 50%; background: radial-gradient(circle, var(--rose-lt) 0%, transparent 70%); 
  pointer-events: none; opacity: 0.7; animation: floatBackground 8s ease-in-out infinite;
}
.hero-left { position: relative; z-index: 2; }
.hero-eyebrow { 
  font-size: 11px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; 
  color: var(--amber); margin-bottom: 1.5rem; display: flex; align-items: center; gap: 8px;
}
.hero-eyebrow::before { content: ''; width: 24px; height: 1px; background: var(--amber); display: inline-block; }
.hero h1 { font-family: var(--serif); font-size: clamp(52px, 7vw, 86px); font-weight: 300; line-height: 1.02; color: var(--sienna); letter-spacing: -0.02em; }
.hero h1 em { font-style: italic; color: var(--amber); font-weight: 400; }
.hero-sub { font-size: 16px; color: var(--ink-2); margin-top: 2rem; max-width: 460px; line-height: 1.8; opacity: 0.9; }

.hero-cta { 
  display: inline-flex; align-items: center; gap: 12px; margin-top: 2.75rem; padding: 15px 34px; 
  background: var(--amber); color: var(--white); border-radius: 100px; font-size: 13px; font-weight: 500; 
  letter-spacing: 0.06em; text-decoration: none; box-shadow: var(--shadow-sm); transition: var(--transition-micro); 
}
.hero-cta:hover { background: var(--amber-dk); transform: translateY(-3px); box-shadow: 0 8px 24px rgba(200,118,58,0.25); }
.hero-cta svg { width: 16px; height: 16px; transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
.hero-cta:hover svg { transform: translateX(5px); }

.hero-right { position: relative; display: flex; flex-direction: column; gap: 1.2rem; z-index: 2; }
.stat-card { 
  background: var(--white); border: 1px solid rgba(237, 228, 213, 0.6); border-radius: 20px; 
  padding: 1.4rem 1.75rem; display: flex; align-items: center; gap: 1.25rem; 
  box-shadow: var(--shadow-sm); transition: var(--transition-smooth); 
}
.stat-card:hover { transform: translateY(-4px) translateX(4px); box-shadow: var(--shadow-md); border-color: var(--rose-lt); }
.stat-num { font-family: var(--serif); font-size: 28px; font-weight: 600; color: var(--sienna); line-height: 1; }
.stat-lbl { font-size: 12px; color: var(--ink-2); opacity: 0.6; margin-top: 4px; letter-spacing: 0.01em; }

section { padding: 8rem 4rem; position: relative; }
.sec-tag { 
  display: inline-block; font-size: 10px; font-weight: 500; letter-spacing: 0.2em; 
  text-transform: uppercase; color: var(--amber); border: 1px solid rgba(200,118,58,0.3); 
  border-radius: 100px; padding: 5px 16px; margin-bottom: 2rem; background: rgba(253,250,246,0.5);
}
.sec-title { font-family: var(--serif); font-size: clamp(36px, 4.5vw, 56px); font-weight: 300; line-height: 1.08; color: var(--sienna); letter-spacing: -0.01em; }
.sec-title em { font-style: italic; color: var(--amber); font-weight: 400; }
.sec-intro { font-size: 15.5px; color: var(--ink-2); max-width: 540px; margin-top: 1.5rem; line-height: 1.75; opacity: 0.85; }

.gallery { background: var(--white); }
.gal-block { margin-top: 5rem; }
.gal-label { font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--amber-dk); margin-bottom: 1.5rem; font-weight: 500; display: flex; align-items: center; gap: 10px; }
.gal-label::after { content: ''; flex: 1; height: 1px; background: var(--linen-2); }
.gal-row { display: flex; gap: 2rem; flex-wrap: wrap; align-items: stretch; }
.gal-row svg { border-radius: 16px; display: block; height: auto; box-shadow: var(--shadow-sm); transition: var(--transition-smooth); }
.gal-row svg:hover { transform: translateY(-6px); box-shadow: var(--shadow-md); }

.about { background: var(--linen); }
.about-grid { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 6rem; align-items: start; margin-top: 4.5rem; }
.about-quote { 
  font-family: var(--serif); font-size: 30px; font-style: italic; font-weight: 300; 
  line-height: 1.4; color: var(--sienna); padding-left: 2rem; border-left: 2px solid var(--amber); 
  position: sticky; top: 120px;
}
.about-body { font-size: 15.5px; color: var(--ink-2); line-height: 1.85; }
.about-body p + p { margin-top: 1.5rem; }
.about-contacts { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 2.5rem; }
.contact-pill { 
  display: inline-flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 500; 
  padding: 9px 20px; border-radius: 100px; background: var(--white); color: var(--ink-2); 
  text-decoration: none; border: 1px solid var(--linen-2); box-shadow: var(--shadow-sm); 
  transition: var(--transition-micro); 
}
.contact-pill:hover { background: var(--rose-lt); border-color: var(--rose); color: var(--sienna); transform: translateY(-2px); }

.skills { background: var(--white); }
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 4.5rem; }
.skill-tile { 
  background: var(--linen); border-radius: 24px; padding: 2.25rem; border: 1px solid rgba(237, 228, 213, 0.7); 
  transition: var(--transition-smooth); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between;
}
.skill-tile::after { 
  content: ''; position: absolute; bottom: 0; right: 0; width: 90px; height: 90px; 
  border-radius: 50%; background: var(--rose-lt); transform: translate(25%, 25%); 
  pointer-events: none; opacity: 0.4; transition: var(--transition-smooth); 
}
.skill-tile:hover { transform: translateY(-8px); box-shadow: var(--shadow-md); border-color: var(--rose); }
.skill-tile:hover::after { transform: translate(15%, 15%) scale(1.2); opacity: 0.6; }
.skill-tile-name { font-family: var(--serif); font-size: 22px; font-weight: 600; color: var(--sienna); margin-bottom: 1rem; }
.skill-list { display: flex; flex-wrap: wrap; gap: 8px; position: relative; z-index: 2; }
.sk { font-size: 11.5px; padding: 4px 12px; background: var(--white); color: var(--ink-2); border-radius: 100px; border: 1px solid rgba(237, 228, 213, 0.9); font-weight: 400; }

.projects { background: var(--sienna); position: relative; }
.projects .sec-tag { color: var(--rose-lt); border-color: rgba(240, 216, 204, 0.3); background: rgba(255,255,255,0.05); }
.projects .sec-title { color: var(--white); }
.projects .sec-title em { color: var(--rose); }
.projects .sec-intro { color: rgba(253, 250, 246, 0.7); }
.proj-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 2rem; margin-top: 4.5rem; }
.proj-card { 
  background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); 
  border-radius: 24px; overflow: hidden; display: flex; flex-direction: column; 
  transition: var(--transition-smooth); position: relative;
}
.proj-card:hover { transform: translateY(-10px); background: rgba(255, 255, 255, 0.08); border-color: rgba(255, 255, 255, 0.2); box-shadow: var(--shadow-lg); }

.proj-visual { 
  position: relative; 
  width: 100%; 
  aspect-ratio: 16 / 10;
  background: rgba(42, 31, 23, 0.2); 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  padding: 1.5rem;
  overflow: visible !important;
}
.proj-visual svg {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain;
}

.proj-body { padding: 2rem; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }
.proj-name { font-family: var(--serif); font-size: 24px; font-weight: 600; color: var(--white); letter-spacing: 0.01em; }
.proj-stack { font-size: 11px; color: var(--rose-lt); opacity: 0.5; margin-top: 4px; letter-spacing: 0.06em; text-transform: uppercase; }
.proj-desc { font-size: 13.5px; color: rgba(253, 250, 246, 0.75); margin-top: 12px; line-height: 1.75; }
.proj-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 18px; }
.ptag { font-size: 10px; font-weight: 500; padding: 4px 12px; border-radius: 100px; background: rgba(212,144,122,0.15); color: var(--rose-lt); border: 1px solid rgba(212,144,122,0.25); letter-spacing: 0.04em; }

.experience { background: var(--white); }
.exp-list { margin-top: 4.5rem; display: flex; flex-direction: column; }
.exp-item { 
  display: grid; grid-template-columns: 180px 1fr; gap: 3rem; padding: 2.5rem 0; 
  border-bottom: 1px solid var(--linen-2); transition: var(--transition-smooth);
}
.exp-item:first-child { padding-top: 0; }
.exp-item:last-child { border-bottom: none; padding-bottom: 0; }
.exp-item:hover { transform: translateX(10px); }
.exp-date { font-size: 13px; font-weight: 500; color: var(--ink-2); opacity: 0.5; letter-spacing: 0.04em; }
.exp-company { font-family: var(--serif); font-size: 18px; font-weight: 600; color: var(--amber); margin-top: 6px; }
.exp-role-title { font-family: var(--serif); font-size: 24px; font-weight: 300; color: var(--sienna); letter-spacing: -0.01em; }
.exp-bullets { margin-top: 1.25rem; list-style: none; display: flex; flex-direction: column; gap: 10px; }
.exp-bullets li { font-size: 14.5px; color: var(--ink-2); padding-left: 1.75rem; position: relative; line-height: 1.7; }
.exp-bullets li::before { content: '→'; position: absolute; left: 0; color: var(--rose); font-weight: bold; }

.certs { background: var(--linen); }
.certs-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 4.5rem; }
.cert-card { 
  background: var(--white); border: 1px solid rgba(237, 228, 213, 0.6); border-radius: 20px; 
  padding: 1.5rem; display: flex; align-items: center; gap: 1.25rem; 
  box-shadow: var(--shadow-sm); transition: var(--transition-smooth); 
}
.cert-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); border-color: var(--amber); }
.cert-badge { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
.cert-badge.ms { background: var(--rose-lt); }
.cert-badge.ibm { background: #DDE8F0; }
.cert-name { font-size: 14px; font-weight: 500; color: var(--ink); line-height: 1.4; }
.cert-issuer { font-size: 12px; color: var(--ink-2); opacity: 0.5; margin-top: 3px; }

.footer-cta { 
  background: var(--amber); padding: 9rem 4rem; text-align: center; position: relative; overflow: hidden; 
}
.footer-cta::before { 
  content: 'CANVA'; position: absolute; font-family: var(--serif); font-size: clamp(120px, 18vw, 260px); 
  font-weight: 600; color: rgba(253, 250, 246, 0.05); top: 50%; left: 50%; 
  transform: translate(-50%, -50%); white-space: nowrap; pointer-events: none; letter-spacing: -0.04em; 
}
.footer-cta h2 { font-family: var(--serif); font-size: clamp(38px, 5.5vw, 68px); font-weight: 300; color: var(--white); line-height: 1.06; position: relative; z-index: 2; letter-spacing: -0.01em; }
.footer-cta h2 em { font-style: italic; font-weight: 400; }
.footer-cta p { color: rgba(253, 250, 246, 0.8); margin-top: 1.5rem; font-size: 16px; position: relative; z-index: 2; max-width: 500px; margin-left: auto; margin-right: auto; }
.footer-links { display: flex; align-items: center; justify-content: center; gap: 1.5rem; margin-top: 3.5rem; flex-wrap: wrap; position: relative; z-index: 2; }
.f-link { 
  display: inline-flex; align-items: center; gap: 10px; padding: 14px 34px; border-radius: 100px; 
  font-size: 13px; font-weight: 500; text-decoration: none; letter-spacing: 0.04em; transition: var(--transition-micro); 
}
.f-link.primary { background: var(--white); color: var(--sienna); box-shadow: var(--shadow-sm); }
.f-link.primary:hover { background: var(--linen); transform: translateY(-3px); box-shadow: 0 8px 24px rgba(42,31,23,0.15); }
.f-link.secondary { background: transparent; color: var(--white); border: 1px solid rgba(253, 250, 246, 0.3); }
.f-link.secondary:hover { background: rgba(253, 250, 246, 0.08); border-color: var(--white); transform: translateY(-3px); }

.footer-bottom { 
  background: var(--ink); padding: 2rem 4rem; display: flex; align-items: center; 
  justify-content: space-between; font-size: 12px; color: rgba(253, 250, 246, 0.4); 
  border-top: 1px solid rgba(253, 250, 246, 0.05); letter-spacing: 0.02em;
}

@media (max-width: 1024px) {
  .hero { gap: 3rem; }
  .about-grid { gap: 3rem; }
}

@media (max-width: 900px) {
  .gal-row svg { width: 100% !important; height: auto !important; }
}

@media (max-width: 768px) {
  nav { padding: 1.25rem 2rem; }
  .menu-toggle { display: block; }
  .nav-links { 
    position: fixed; top: 0; right: 0; bottom: 0; width: 280px; 
    background: var(--white); box-shadow: var(--shadow-lg); padding: 6rem 2rem 2rem; 
    flex-direction: column; align-items: flex-start; transform: translateX(100%); 
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); z-index: 105;
  }
  .nav-links.active { transform: translateX(0); }
  .nav-links li { margin-left: 0; margin-bottom: 2rem; }
  .nav-links a { font-size: 14px; }
  .nav-links.active ~ .menu-toggle span:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
  .nav-links.active ~ .menu-toggle span:nth-child(2) { opacity: 0; }
  .nav-links.active ~ .menu-toggle span:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }

  .hero { grid-template-columns: 1fr; padding: 8rem 2rem 4rem; gap: 4rem; min-height: auto; }
  section { padding: 5rem 2rem; }
  .about-grid { grid-template-columns: 1fr; gap: 2.5rem; }
  .about-quote { position: static; padding-left: 1.5rem; font-size: 24px; }
  .exp-item { grid-template-columns: 1fr; gap: 0.75rem; }
  .footer-cta { padding: 6rem 2rem; }
  .footer-bottom { padding: 2rem; flex-direction: column; gap: 1rem; text-align: center; }
}

@media (prefers-reduced-motion: reduce){ 
  * { animation: none !important; transition: none !important; } 
}
a:focus-visible, button:focus-visible { outline: 2px solid var(--amber); outline-offset: 3px; }
</style>
</head>
<body>
<nav>
  <a href="#home" class="nav-logo">Jhanvi Jyant</a>
  <ul class="nav-links" id="navLinks">
    <li><a href="#gallery">Visual Work</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Case Studies</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <button class="menu-toggle" aria-label="Toggle Navigation Menu" id="menuToggle">
    <span></span>
    <span></span>
    <span></span>
  </button>
</nav>

<section class="hero" id="home">
  <div class="hero-left">
    <div class="hero-eyebrow">Graphic Designer</div>
    <h1>Design that<br>makes spaces<br><em>feel alive.</em></h1>
    <p class="hero-sub">I'm Jhanvi — a visual designer and CS undergraduate who believes every pixel should serve a feeling.</p>
    <a href="#gallery" class="hero-cta">
      See the visual work
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </a>
  </div>
  <div class="hero-right">
    <div class="stat-card">
      <div><div class="stat-num">3+</div><div class="stat-lbl">Brand & visual pieces designed</div></div>
    </div>
    <div class="stat-card">
      <div><div class="stat-num">35%</div><div class="stat-lbl">UX efficiency gain, StegaVision</div></div>
    </div>
    <div class="stat-card">
      <div><div class="stat-num">AI+</div><div class="stat-lbl">Prompt-engineered creative workflows</div></div>
    </div>
  </div>
</section>

<section class="gallery" id="gallery">
  <span class="sec-tag">Visual work</span>
  <h2 class="sec-title">Brand, social &<br><em>poster design.</em></h2>
  <p class="sec-intro">A personal brand system built and applied across formats — logo, identity board, social posts, a poster, and a real interface redesign.</p>
  
  <div class="gal-block">
    <div class="gal-label">Logo System</div>
    <div class="gal-row">
      <svg width="110" height="110" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="120" height="120" rx="24" fill="#7A3B1E"/>
        <g transform="translate(60,60)">
          <path d="M -8 -28 L 14 -28 L 14 18 Q 14 32 -2 32 Q -16 32 -16 18 L -16 12" stroke="#F5EFE4" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="14" cy="-28" r="5.5" fill="#D4907A"/>
        </g>
      </svg>
      <svg width="110" height="110" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="120" height="120" rx="24" fill="#FDFAF6" stroke="#EDE4D5" stroke-width="2"/>
        <g transform="translate(60,60)">
          <path d="M -8 -28 L 14 -28 L 14 18 Q 14 32 -2 32 Q -16 32 -16 18 L -16 12" stroke="#7A3B1E" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="14" cy="-28" r="5.5" fill="#C8763A"/>
        </g>
      </svg>
      <svg width="260" height="110" viewBox="0 0 260 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="260" height="110" rx="16" fill="#FDFAF6" stroke="#EDE4D5" stroke-width="2"/>
        <g transform="translate(46,55)">
          <path d="M -6 -22 L 11 -22 L 11 14 Q 11 25 -1 25 Q -13 25 -13 14 L -13 9" stroke="#7A3B1E" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="11" cy="-22" r="4.5" fill="#C8763A"/>
        </g>
        <text x="88" y="50" font-family="Georgia, serif" font-style="italic" font-weight="600" font-size="26" fill="#7A3B1E">Jhanvi</text>
        <text x="88" y="68" font-family="Arial, sans-serif" font-size="9" letter-spacing="2.5" fill="#C8763A">VISUAL DESIGNER</text>
      </svg>
    </div>
  </div>

  <div class="gal-block">
    <div class="gal-label">Brand Board</div>
    <div class="gal-row">
      <svg width="100%" height="280" viewBox="0 0 640 280" fill="none" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;">
        <rect width="640" height="280" fill="#FDFAF6"/>
        <text x="32" y="40" font-family="Arial" font-size="10" letter-spacing="3" fill="#9E5620">COLOR PALETTE</text>
        <g transform="translate(32,55)">
          <rect width="70" height="70" rx="10" fill="#C8763A"/><text x="0" y="86" font-family="Arial" font-size="9" fill="#5C4033">#C8763A</text>
          <rect x="84" width="70" height="70" rx="10" fill="#7A3B1E"/><text x="84" y="86" font-family="Arial" font-size="9" fill="#5C4033">#7A3B1E</text>
          <rect x="168" width="70" height="70" rx="10" fill="#D4907A"/><text x="168" y="86" font-family="Arial" font-size="9" fill="#5C4033">#D4907A</text>
          <rect x="252" width="70" height="70" rx="10" fill="#F0D8CC"/><text x="252" y="86" font-family="Arial" font-size="9" fill="#5C4033">#F0D8CC</text>
          <rect x="336" width="70" height="70" rx="10" fill="#F5EFE4" stroke="#EDE4D5" stroke-width="1.5"/><text x="336" y="86" font-family="Arial" font-size="9" fill="#5C4033">#F5EFE4</text>
        </g>
        <text x="32" y="175" font-family="Arial" font-size="10" letter-spacing="3" fill="#9E5620">TYPOGRAPHY</text>
        <text x="32" y="215" font-family="Georgia, serif" font-style="italic" font-size="34" fill="#7A3B1E">Cormorant Garamond</text>
        <text x="32" y="245" font-family="Arial" font-size="14" fill="#5C4033">DM Sans — for body copy, labels, and UI text</text>
        <line x1="420" y1="55" x2="420" y2="260" stroke="#EDE4D5" stroke-width="2"/>
        <text x="445" y="40" font-family="Arial" font-size="10" letter-spacing="3" fill="#9E5620">MARK</text>
        <g transform="translate(445,55)">
          <rect width="90" height="90" rx="18" fill="#7A3B1E"/>
          <g transform="translate(45,45)">
            <path d="M -6 -21 L 10.5 -21 L 10.5 13 Q 10.5 24 -1 24 Q -12 24 -12 13 L -12 9" stroke="#F5EFE4" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="10.5" cy="-21" r="4" fill="#D4907A"/>
          </g>
        </g>
        <text x="445" y="170" font-family="Arial" font-size="9" fill="#9E5620">Warm, intentional, handcrafted —</text>
        <text x="445" y="184" font-family="Arial" font-size="9" fill="#9E5620">a palette for spaces that feel lived-in.</text>
      </svg>
    </div>
  </div>

  <div class="gal-block">
    <div class="gal-label">Instagram Post Design — CyberSec Launch</div>
    <div class="gal-row">
      <svg width="280" height="280" viewBox="0 0 320 320" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="320" height="320" fill="#7A3B1E"/>
        <circle cx="280" cy="40" r="120" fill="#9E5620" opacity="0.4"/>
        <text x="32" y="60" font-family="Arial" font-size="10" letter-spacing="3" fill="#D4907A">PRODUCT LAUNCH</text>
        <text x="32" y="130" font-family="Georgia, serif" font-style="italic" font-weight="600" font-size="40" fill="#FDFAF6">Meet</text>
        <text x="32" y="172" font-family="Georgia, serif" font-style="italic" font-weight="600" font-size="40" fill="#C8763A">CyberSec.</text>
        <text x="32" y="210" font-family="Arial" font-size="13" fill="#F0D8CC">AI-powered security, made</text>
        <text x="32" y="228" font-family="Arial" font-size="13" fill="#F0D8CC">simple for everyone.</text>
        <rect x="32" y="250" width="140" height="34" rx="17" fill="#C8763A"/>
        <text x="102" y="271" font-family="Arial" font-size="11" fill="#FDFAF6" text-anchor="middle" font-weight="bold">Try it free →</text>
        <g transform="translate(255,270)">
          <path d="M -5 -18 L 9 -18 L 9 12 Q 9 20 -1 20 Q -10 20 -10 12 L -10 9" stroke="#F5EFE4" stroke-width="5.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="9" cy="-18" r="3.5" fill="#D4907A"/>
        </g>
      </svg>
      <svg width="280" height="280" viewBox="0 0 320 320" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="320" height="320" fill="#F5EFE4"/>
        <rect x="20" y="20" width="280" height="280" rx="20" fill="#FDFAF6" stroke="#EDE4D5" stroke-width="2"/>
        <text x="160" y="75" font-family="Arial" font-size="10" letter-spacing="3" fill="#C8763A" text-anchor="middle">STEGAVISION</text>
        <rect x="50" y="100" width="220" height="130" rx="12" fill="#2A1F17"/>
        <circle cx="70" cy="118" r="4" fill="#C8763A"/>
        <circle cx="84" cy="118" r="4" fill="#D4907A"/>
        <circle cx="98" cy="118" r="4" fill="#F0D8CC"/>
        <rect x="62" y="135" width="80" height="80" rx="6" fill="#3A2A1F"/>
        <rect x="150" y="135" width="105" height="14" rx="4" fill="#5C4033"/>
        <rect x="150" y="156" width="80" height="10" rx="3" fill="#7A3B1E"/>
        <rect x="150" y="174" width="95" height="10" rx="3" fill="#7A3B1E"/>
        <rect x="150" y="196" width="60" height="20" rx="10" fill="#C8763A"/>
        <text x="160" y="255" font-family="Georgia, serif" font-style="italic" font-size="20" fill="#7A3B1E" text-anchor="middle">Calm UI for complex tools.</text>
        <text x="160" y="278" font-family="Arial" font-size="11" fill="#9E5620" text-anchor="middle">35% faster task completion</text>
      </svg>
    </div>
  </div>

  <div class="gal-block">
    <div class="gal-label">Poster — AI Resume Analyser</div>
    <div class="gal-row">
      <svg width="240" height="370" viewBox="0 0 260 400" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="260" height="400" fill="#7A3B1E"/>
        <circle cx="40" cy="360" r="160" fill="#9E5620" opacity="0.35"/>
        <circle cx="230" cy="40" r="100" fill="#C8763A" opacity="0.25"/>
        <text x="30" y="60" font-family="Arial" font-size="9" letter-spacing="3" fill="#D4907A">CASE STUDY</text>
        <text x="30" y="115" font-family="Georgia, serif" font-style="italic" font-weight="600" font-size="34" fill="#FDFAF6">Resumes,</text>
        <text x="30" y="152" font-family="Georgia, serif" font-style="italic" font-weight="600" font-size="34" fill="#FDFAF6">decoded.</text>
        <line x1="30" y1="175" x2="90" y2="175" stroke="#C8763A" stroke-width="3"/>
        <text x="30" y="205" font-family="Arial" font-size="12" fill="#F0D8CC">From lo-fi wireframe to</text>
        <text x="30" y="223" font-family="Arial" font-size="12" fill="#F0D8CC">polished product UI —</text>
        <text x="30" y="241" font-family="Arial" font-size="12" fill="#F0D8CC">designed for clarity, not jargon.</text>
        <g transform="translate(30,275)">
          <rect width="58" height="13" rx="6.5" fill="#D4907A"/>
          <rect width="92" height="13" rx="6.5" y="22" fill="#C8763A"/>
          <rect width="38" height="13" rx="6.5" y="44" fill="#F0D8CC"/>
        </g>
        <line x1="30" y1="350" x2="230" y2="350" stroke="#9E5620" stroke-width="0.75" opacity="0.5"/>
        <text x="30" y="372" font-family="Arial" font-size="9" letter-spacing="1.5" fill="#D4907A">JHANVI JYANT</text>
        <text x="30" y="386" font-family="Arial" font-size="8" letter-spacing="1" fill="#C8763A">PRODUCT &amp; UI DESIGN</text>
      </svg>
    </div>
  </div>

  <div class="gal-block">
    <div class="gal-label">Before / After — Dashboard Redesign</div>
    <div class="gal-row">
      <svg width="100%" height="280" viewBox="0 0 640 280" fill="none" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;">
        <rect width="310" height="280" fill="#E5E5E5"/>
        <text x="20" y="28" font-family="Arial" font-size="10" letter-spacing="2" fill="#888">BEFORE</text>
        <rect x="20" y="45" width="270" height="36" fill="#CFCFCF"/>
        <rect x="20" y="90" width="130" height="80" fill="#D8D8D8"/>
        <rect x="160" y="90" width="130" height="80" fill="#D8D8D8"/>
        <rect x="20" y="178" width="270" height="14" fill="#C8C8C8"/>
        <rect x="20" y="198" width="220" height="14" fill="#C8C8C8"/>
        <rect x="20" y="218" width="250" height="14" fill="#C8C8C8"/>
        <rect x="20" y="245" width="90" height="22" fill="#B8B8B8"/>
        <text x="155" y="60" font-family="Arial" font-size="9" fill="#999" text-anchor="middle">cluttered nav, no hierarchy</text>
        <g transform="translate(330,0)">
          <rect width="310" height="280" fill="#FDFAF6"/>
          <text x="20" y="28" font-family="Arial" font-size="10" letter-spacing="2" fill="#9E5620">AFTER</text>
          <rect x="20" y="45" width="270" height="30" rx="8" fill="#F5EFE4"/>
          <circle cx="35" cy="60" r="6" fill="#C8763A"/>
          <rect x="50" y="56" width="60" height="8" rx="4" fill="#7A3B1E"/>
          <rect x="20" y="90" width="270" height="60" rx="12" fill="#7A3B1E"/>
          <text x="36" y="115" font-family="Georgia, serif" font-style="italic" font-size="16" fill="#FDFAF6">Score: 87</text>
          <rect x="36" y="125" width="180" height="8" rx="4" fill="#C8763A"/>
          <rect x="20" y="162" width="125" height="60" rx="12" fill="#F0D8CC"/>
          <rect x="155" y="162" width="135" height="60" rx="12" fill="#F0D8CC"/>
          <rect x="34" y="178" width="60" height="8" rx="4" fill="#9E5620"/>
          <rect x="34" y="194" width="90" height="8" rx="4" fill="#C8763A"/>
          <rect x="169" y="178" width="60" height="8" rx="4" fill="#9E5620"/>
          <rect x="169" y="194" width="100" height="8" rx="4" fill="#C8763A"/>
          <rect x="20" y="234" width="120" height="28" rx="14" fill="#C8763A"/>
          <text x="80" y="252" font-family="Arial" font-size="10" fill="#FDFAF6" text-anchor="middle" font-weight="bold">View report</text>
          <text x="155" y="250" font-family="Arial" font-size="9" fill="#9E5620">clear hierarchy, breathing room</text>
        </g>
        <line x1="330" y1="0" x2="330" y2="280" stroke="#7A3B1E" stroke-width="3"/>
      </svg>
    </div>
  </div>
</section>

<section class="about" id="about">
  <span class="sec-tag">About me</span>
  <h2 class="sec-title">Creative mind,<br><em>technical hands.</em></h2>
  <div class="about-grid">
    <div class="about-quote">"I don't just design screens — I design the feeling you get when you land on one."</div>
    <div class="about-body">
      <p>I'm a B.Tech Computer Science undergraduate at VIT Bhopal, specialising in Cybersecurity — but my heart has always lived in design. I fell in love with the way a single font choice or a deliberate colour palette can completely shift how something feels.</p>
      <p>I've spent the past two years building full-stack products where I owned both the code and the visual language — every layout, every motion, every micro-interaction was a deliberate decision. My technical background means I can actually build what I design, not just hand off mockups.</p>
      <p>Canva's philosophy — that great design shouldn't be gatekept, and should be accessible to everyone — is exactly why I want to be here. I want to help build the templates and systems that make that true at scale.</p>
      <div class="about-contacts">
        <a href="mailto:jhanvijyant15201@gmail.com" class="contact-pill">✉ jhanvijyant15201@gmail.com</a>
        <a href="https://linkedin.com/in/jhanvi-jyant" target="_blank" rel="noopener" class="contact-pill">in LinkedIn</a>
        <a href="https://github.com/jhanvijyant" target="_blank" rel="noopener" class="contact-pill">⌥ GitHub</a>
        <span class="contact-pill">Varanasi, India</span>
      </div>
    </div>
  </div>
</section>

<section class="skills" id="skills">
  <span class="sec-tag">What I bring</span>
  <h2 class="sec-title">Design skills &<br><em>creative tools.</em></h2>
  <div class="skills-grid">
    <div class="skill-tile">
      <div class="skill-tile-name">Visual Design</div>
      <div class="skill-list"><span class="sk">Typography</span><span class="sk">Color Theory</span><span class="sk">Layout</span><span class="sk">Mood-boarding</span><span class="sk">Brand Identity</span><span class="sk">Style Guides</span></div>
    </div>
    <div class="skill-tile">
      <div class="skill-tile-name">UI / UX</div>
      <div class="skill-list"><span class="sk">Figma</span><span class="sk">Wireframing</span><span class="sk">Prototyping</span><span class="sk">User Flows</span><span class="sk">Responsive Design</span></div>
    </div>
    <div class="skill-tile">
      <div class="skill-tile-name">Frontend</div>
      <div class="skill-list"><span class="sk">HTML/CSS</span><span class="sk">JavaScript</span><span class="sk">React</span><span class="sk">Bootstrap 5</span></div>
    </div>
    <div class="skill-tile">
      <div class="skill-tile-name">AI Creative</div>
      <div class="skill-list"><span class="sk">Gemini AI</span><span class="sk">Prompt Engineering</span><span class="sk">AI Image Gen</span></div>
    </div>
    <div class="skill-tile">
      <div class="skill-tile-name">Tools</div>
      <div class="skill-list"><span class="sk">Canva</span><span class="sk">Adobe Illustrator</span></div>
    </div>
  </div>
</section>

<section class="projects" id="projects">
  <span class="sec-tag">Case Studies</span>
  <h2 class="sec-title">Full-stack products,<br><em>end-to-end design.</em></h2>
  <p class="sec-intro">Three comprehensive projects where I served as the sole UI designer and frontend engineer, ensuring a seamless bridge between identity and execution.</p>

  <div class="proj-grid">
    <div class="proj-card">
      <div class="proj-visual">
        <svg width="100%" height="100%" viewBox="0 0 400 220" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <defs><linearGradient id="cyberGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#C8763A"/><stop offset="100%" stop-color="#7A3B1E"/></linearGradient></defs>
          <rect width="400" height="220" rx="16" fill="url(#cyberGrad)" opacity="0.15"/>
          <rect x="40" y="30" width="320" height="160" rx="16" fill="#2A1F17" stroke="rgba(212,144,122,0.3)" stroke-width="2"/>
          <rect x="40" y="30" width="320" height="35" rx="16" fill="#3A2A1F"/>
          <circle cx="65" cy="48" r="5" fill="#D4907A"/>
          <circle cx="80" cy="48" r="5" fill="#C8763A"/>
          <circle cx="95" cy="48" r="5" fill="#F0D8CC"/>
          <text x="200" y="52" font-family="Arial" font-size="11" fill="#F0D8CC" text-anchor="middle" letter-spacing="1">CYBERSEC CHAT</text>
          <rect x="60" y="85" width="180" height="32" rx="12" fill="#7A3B1E"/>
          <circle cx="82" cy="101" r="10" fill="#D4907A"/>
          <rect x="102" y="97" width="120" height="8" rx="4" fill="#FDFAF6"/>
          <rect x="160" y="132" width="180" height="32" rx="12" fill="#C8763A"/>
          <rect x="178" y="144" width="120" height="8" rx="4" fill="#FDFAF6"/>
          <circle cx="318" cy="148" r="10" fill="#F0D8CC"/>
        </svg>
      </div>
      <div class="proj-body">
        <div>
          <div class="proj-name">CyberSec Chatbot</div>
          <div class="proj-stack">UI Design · React · Gemini API</div>
          <p class="proj-desc">A conversational interface designed to explain complex network vulnerabilities in plain English. Transformed intimidating CLI outputs into friendly, human-readable visual layouts.</p>
        </div>
        <div class="proj-tags"><span class="ptag">AI Workflows</span><span class="ptag">Clean UI</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-visual">
        <svg width="100%" height="100%" viewBox="0 0 400 220" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <rect width="400" height="220" rx="16" fill="#FDFAF6" opacity="0.08"/>
          <rect x="50" y="25" width="300" height="170" rx="12" fill="#FDFAF6" stroke="#EDE4D5" stroke-width="2"/>
          <path d="M 50 65 L 350 65" stroke="#EDE4D5" stroke-width="1.5"/>
          <text x="75" y="48" font-family="Georgia, serif" font-style="italic" font-weight="bold" font-size="15" fill="#7A3B1E">StegaVision</text>
          <rect x="75" y="85" width="110" height="90" rx="8" fill="#F5EFE4" stroke="#C8763A" stroke-dasharray="4,4"/>
          <circle cx="130" cy="125" r="16" fill="#D4907A" opacity="0.7"/>
          <text x="130" y="130" font-family="Arial" font-size="14" fill="#7A3B1E" text-anchor="middle">+</text>
          <rect x="205" y="85" width="120" height="12" rx="4" fill="#7A3B1E"/>
          <rect x="205" y="105" width="95" height="8" rx="4" fill="#BFB0A0"/>
          <rect x="205" y="121" width="110" height="8" rx="4" fill="#BFB0A0"/>
          <rect x="205" y="145" width="85" height="30" rx="15" fill="#C8763A"/>
          <text x="247" y="164" font-family="Arial" font-size="11" fill="#FDFAF6" text-anchor="middle" font-weight="bold">Decode</text>
        </svg>
      </div>
      <div class="proj-body">
        <div>
          <div class="proj-name">StegaVision</div>
          <div class="proj-stack">Product Design · Python · UI Architect</div>
          <p class="proj-desc">An image steganography platform. Stripped away technical overhead to achieve a clean drag-and-drop tool, yielding a verified 35% user efficiency improvement over existing open-source variants.</p>
        </div>
        <div class="proj-tags"><span class="ptag">User Testing</span><span class="ptag">Tool Design</span><span class="ptag">Security UX</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-visual">
        <svg width="100%" height="100%" viewBox="0 0 400 220" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <rect width="400" height="220" rx="16" fill="#D4907A" opacity="0.15"/>
          <g transform="translate(60, 25)">
            <rect width="130" height="170" rx="8" fill="#FDFAF6"/>
            <rect x="15" y="20" width="45" height="10" rx="2" fill="#7A3B1E"/>
            <circle cx="105" cy="25" r="10" fill="#EEF0D8"/>
            <line x1="15" y1="45" x2="115" y2="45" stroke="#EDE4D5" stroke-width="2"/>
            <line x1="15" y1="65" x2="95" y2="65" stroke="#BFB0A0" stroke-width="4" stroke-linecap="round"/>
            <line x1="15" y1="80" x2="115" y2="80" stroke="#BFB0A0" stroke-width="4" stroke-linecap="round"/>
            <line x1="15" y1="95" x2="75" y2="95" stroke="#BFB0A0" stroke-width="4" stroke-linecap="round"/>
            <rect x="15" y="120" width="100" height="32" rx="6" fill="#F0D8CC"/>
            <rect x="30" y="132" width="70" height="8" rx="4" fill="#C8763A"/>
          </g>
          <g transform="translate(210, 50)">
            <circle cx="45" cy="45" r="45" fill="#7A3B1E"/>
            <text x="45" y="52" font-family="Georgia" font-style="italic" font-size="22" fill="#FDFAF6" text-anchor="middle">87%</text>
            <rect x="-10" y="110" width="110" height="24" rx="12" fill="#C8763A"/>
            <text x="45" y="125" font-family="Arial" font-size="10" fill="#FDFAF6" text-anchor="middle" font-weight="bold">ATS Optimized</text>
          </g>
        </svg>
      </div>
      <div class="proj-body">
        <div>
          <div class="proj-name">Resume AI Analyser</div>
          <div class="proj-stack">Visual Language · Full-Stack React</div>
          <p class="proj-desc">An interactive platform providing parsing metrics for student resumes. Replaced raw data structures with clean color-coded score circles and dynamic, contextual action panels.</p>
        </div>
        <div class="proj-tags"><span class="ptag">Dashboard UI</span><span class="ptag">Frontend Engineering</span><span class="ptag">Data Visualization</span></div>
      </div>
    </div>
  </div>
</section>

<section class="experience" id="experience">
  <span class="sec-tag">Journey</span>
  <h2 class="sec-title">Work history &<br><em>creative footprints.</em></h2>
  
  <div class="exp-list">
    <div class="exp-item">
      <div class="exp-date-col">
        <div class="exp-date">2024 — PRESENT</div>
        <div class="exp-company">UI Designer & Lead</div>
      </div>
      <div>
        <h3 class="exp-role-title">Freelance Design & Development</h3>
        <ul class="exp-bullets">
          <li>Designed end-to-end identity systems, responsive landing pages, and interactive UI component sets for global independent digital clients.</li>
          <li>Translated loose brand values into crisp high-fidelity production systems built over robust components using scalable CSS architectures.</li>
        </ul>
      </div>
    </div>

    <div class="exp-item">
      <div class="exp-date-col">
        <div class="exp-date">2023 — 2024</div>
        <div class="exp-company">Open Source Contributor</div>
      </div>
      <div>
        <h3 class="exp-role-title">Frontend & Component UI Developer</h3>
        <ul class="exp-bullets">
          <li>Refactored interactive elements for local software toolkits, bringing enhanced responsive standards and modern color harmony to existing operational layouts.</li>
          <li>Audited accessibility benchmarks to implement proper screen-reader aria behaviors and fluid typographic focus scaling matrices.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="certs">
  <span class="sec-tag">Validation</span>
  <h2 class="sec-title">Industry credentials &<br><em>professional badges.</em></h2>
  <div class="certs-row">
    <div class="cert-card">
      <div class="cert-badge ms"></div>
      <div>
        <div class="cert-name">Microsoft Certified: Azure Fundamentals</div>
        <div class="cert-issuer">Microsoft</div>
      </div>
    </div>
    <div class="cert-card">
      <div class="cert-badge ibm"></div>
      <div>
        <div class="cert-name">IBM Cybersecurity Analyst Certificate</div>
        <div class="cert-issuer">IBM Professional Certification</div>
      </div>
    </div>
  </div>
</section>

<section class="footer-cta" id="contact">
  <h2>Let's build spaces that<br><em>feel completely alive.</em></h2>
  <p>Currently searching for a Graphic Design Internship position at Canva. Let's create intentional visual frameworks together.</p>
  
  <div class="footer-links">
    <a href="mailto:jhanvijyant15201@gmail.com" class="f-link primary">Get in touch via email</a>
    <a href="https://linkedin.com/in/jhanvi-jyant" target="_blank" rel="noopener" class="f-link secondary">View LinkedIn profile</a>
  </div>
</section>

<footer class="footer-bottom">
  <div>© 2026 Jhanvi Jyant. All rights reserved. Handcrafted with precision.</div>
</footer>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    menuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
    });
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
      });
    });
  });
</script>
</body>
</html>"""

@app.route('/')
def home():
    return html_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
