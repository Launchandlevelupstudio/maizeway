import os, json, html, datetime
OUT = "/mnt/user-data/outputs/maizeway-site"
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))

HERO_B64 = open(os.path.join(HERE,"hero_b64.txt")).read().strip()
ABOUT_B64 = open(os.path.join(HERE,"about_b64.txt")).read().strip()

# ===================== CONFIG =====================
SITE_URL   = "https://[maizeway.com]"          # set the real domain, no trailing slash
FIRM       = "MaizeWay"
FOUNDER    = "Eunice Maize"
TITLE      = "PMP, Business Solutions Architect"
PHONE      = "(301) 346-6557"
PHONE_TEL  = "+13013466557"
EMAIL      = "[eunice@maizeway.com]"      # domain email — currently eunicemaize@gmail.com, see notes
FORM_EMAIL = "[eunice@maizeway.com]"      # FormSubmit destination once domain email exists
CITY_AREA  = "Bowie, MD & the DC metro"
TAGLINE    = "We streamline the work. We don't add to it."
YEARS, CERTS = "12+", "PMP"
LINKEDIN   = "https://linkedin.com/in/eunicemaize"
BOOKING    = "contact.html"

# Three engagement tracks (blueprint Section 13) — replaces the five-tier menu
TRACKS = [
 dict(slug="program-project-leadership", nav="Program & Project Leadership", h1="Program & Project Leadership",
      tag="Hands-on leadership of a specific initiative, from design through delivery.",
      short="I own the structure, drive the execution, and leave the operating documentation behind.",
      who="Organizations with an initiative that matters and no one with the capacity or seniority to own it end to end.",
      problems="No single owner. Wrong sequencing. No visibility. Cross-functional work that stalls at handoffs.",
      does="I diagnose the current state, design the operating model, build the plan and the governance around it, then lead the execution through delivery.",
      deliverables=["Operating model and RACI","Sequenced delivery plan","Risk register with owners","Reporting cadence and template","SOPs for the processes created","Handoff package"],
      structure="30–90 days project-based, or a monthly retainer for ongoing portfolio oversight.",
      entry="The Operations Diagnostic — a scoped two-week assessment producing a prioritized findings report and a recommended path.",
      cta="Discuss your initiative"),
 dict(slug="federal-nonprofit-delivery", nav="Federal & Nonprofit Delivery Support", h1="Program Support for Compliance-Driven, Resource-Constrained Teams",
      tag="Built for environments where the reporting requirements come from outside and the team executing is small.",
      short="Portfolio management, acquisition planning support, federal reporting, and audit-ready SOPs.",
      who="Federal contractors and subcontractors, federal program offices, and nonprofits managing grants, funder reporting, or a program launch.",
      problems="Reporting obligations with no supporting process. Acquisition planning capacity gaps. Data calls consuming the whole team. SOPs that don't survive an audit. Grant deliverables with no delivery structure.",
      does="Portfolio and program management, acquisition planning support, federal reporting and data call management, compliance-aligned SOP development, and stakeholder engagement strategy.",
      deliverables=["Compliance-aligned SOPs","Reporting calendar and templates","Data call response process","Program documentation package","Stakeholder engagement plan"],
      structure="Custom scope — project or retainer.",
      entry="A capability discussion to map your reporting requirements against what's currently in place.",
      cta="Request a capability discussion"),
]


PACKAGES = {
 "program-project-leadership": [
   dict(name="The Efficiency Audit", tier="Entry", dur="Assessment",
        desc="A focused deep-dive into your operations, workflows, and team processes. You walk away with a prioritized action plan that shows exactly where the initiative is losing time, budget, and momentum.",
        bullets=["Operations & workflow assessment","Bottleneck identification report","Prioritized recommendations roadmap","60-min debrief session"],
        bestfor="Organizations sizing up a bigger initiative", cta="Start here"),
   dict(name="The VIP Strategy Day", tier="Entry", dur="One Day",
        desc="A full-day intensive working session. We map the operational landscape together, identify the highest-leverage opportunities, and build a concrete 90-day execution plan in a single focused sitting.",
        bullets=["Full-day working session (6 hrs)","Operational landscape mapping","90-day execution roadmap","2-week post-day email support"],
        bestfor="Decisive leaders who want a plan in a day", cta="Reserve a day"),
   dict(name="The Solutions Sprint", tier="Core", dur="30–90 Days",
        desc="Hands-on program and project leadership to implement operational fixes and build the structure that gets a specific initiative to the finish line.",
        bullets=["Project management & execution","Workflow design & implementation","Team alignment & SOPs","Weekly check-ins & reporting"],
        bestfor="Initiatives mid-transition or launching new", cta="Let's talk scope"),
   dict(name="The Strategic Partner Retainer", tier="Ongoing", dur="Monthly",
        desc="Ongoing monthly leadership for organizations that need a senior program partner embedded on a recurring basis — priority oversight across whatever is in flight, without a full-time hire.",
        bullets=["Monthly strategy sessions","On-call advisory support","Ongoing process optimization","Priority project oversight","Monthly performance reporting"],
        bestfor="Leaders who want a senior partner embedded year-round", cta="Apply for a retainer"),
 ],
 "federal-nonprofit-delivery": [
   dict(name="Federal & Nonprofit Solutions", tier="Specialized", dur="Custom Scope",
        desc="Tailored program and project management support for federal agencies, contractors, and mission-driven nonprofits — built around reporting obligations that come from outside and delivery teams that are often small.",
        bullets=["Portfolio & program management","Acquisition planning support","Federal reporting & data calls","Compliance-aligned SOPs","Stakeholder engagement strategy"],
        bestfor="Federal agencies, contractors & nonprofits", cta="Request a proposal"),
 ],
}

METHOD = [
 ("Discover","We start with a free discovery call to understand your business, your goals, and where the friction lives."),
 ("Diagnose","We assess your operations, map your workflows, and identify the highest-leverage opportunities for improvement."),
 ("Architect","We design tailored operational solutions — systems, frameworks, and plans built specifically for where you're going."),
 ("Execute","We implement. We track. We optimize. You walk away with leaner operations and more capacity to lead."),
]

BELIEFS = [
 "[Belief 1 — one opinion about projects Eunice will defend, in her own words.]",
 "[Belief 2 — from the questionnaire / conversation with Eunice.]",
 "[Belief 3 — from the questionnaire / conversation with Eunice.]",
]
# ==========================================================================

CSS = open(os.path.join(HERE,"site.css")).read()
JS  = open(os.path.join(HERE,"site.js")).read()
ARROW = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CARET = '<svg class="caret" aria-hidden="true" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>'
CHECK = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>'

def esc(s): return html.escape(s, quote=True)

def header(active):
    def cls(k): return ' class="active"' if k==active else ''
    dd = "".join(f'<a href="{t["slug"]}.html" role="menuitem">{t["nav"]}<small>{t["short"]}</small></a>' for t in TRACKS)
    mob = "".join(f'<a href="{t["slug"]}.html">{t["nav"]}</a>' for t in TRACKS)
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="nav"><div class="wrap">
 <a class="brand" href="index.html" aria-label="{FIRM} home"><span class="mark" aria-hidden="true">MW</span><span class="brand-text"><span class="name">{FIRM}</span><span class="tagline">Project Management Consulting</span></span></a>
 <nav aria-label="Primary"><ul class="menu">
  <li{cls('services')}><a href="services.html" aria-haspopup="true" aria-expanded="false">Services {CARET}</a><div class="dd" role="menu">{dd}<a href="services.html" role="menuitem" class="all">All services {ARROW}</a></div></li>
  <li{cls('about')}><a href="about.html">About</a></li>
  <li><a class="btn btn-gold cta" href="{BOOKING}" data-track="nav_cta">Book a Discovery Call</a></li>
 </ul></nav>
 <a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE}</a>
 <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<div class="mnav" id="mnav" role="dialog" aria-modal="true" aria-label="Menu" aria-hidden="true">
 <div class="top"><a class="brand" href="index.html"><span class="mark sm" aria-hidden="true">MW</span><span class="brand-text"><span class="name sm">{FIRM}</span><span class="tagline sm">Project Management Consulting</span></span></a><button class="burger" id="mclose" aria-label="Close menu"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
 <nav aria-label="Mobile">
  <button class="row" data-acc aria-expanded="false" aria-controls="msub"><span>Services</span><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></button>
  <div class="sub" id="msub">{mob}<a href="services.html">All services</a></div>
  <a class="row" href="about.html">About</a>
  <a class="row" href="contact.html">Contact</a>
 </nav>
 <div class="foot"><a class="btn btn-gold" href="{BOOKING}">Book a Discovery Call</a><div class="ln"><a href="tel:{PHONE_TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
</div>
"""


def pkg_card(p):
    bl = "".join(f"<li>{CHECK}{d}</li>" for d in p["bullets"])
    return f'''<article class="pkg">
 <p class="pkg-kicker">{p["tier"]} &middot; {p["dur"].upper()}</p>
 <h3>{p["name"]}</h3>
 <p class="pkg-desc">{p["desc"]}</p>
 <ul class="ticks">{bl}</ul>
 <div class="pkg-foot"><span class="pkg-bestfor">Best for: {p["bestfor"]}</span><a class="more" href="contact.html">{p["cta"]} {ARROW}</a></div>
</article>'''

def pkg_section(t):
    pkgs = PACKAGES.get(t["slug"], [])
    if not pkgs: return ""
    cards = "".join(pkg_card(p) for p in pkgs)
    cols = "g2" if len(pkgs) in (2,4) else "g3"
    return f'''<div class="pkg-group"><h3 class="pkg-group-h"><a href="{t["slug"]}.html">{t["nav"]}</a></h3><div class="grid {cols} pkgs">{cards}</div></div>'''

def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for t,h in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol><li><a href="index.html">Home</a></li>{lis}</ol></div></nav>'

def cta_band(h="Ready to stop managing chaos and start scaling with clarity?", p="Book a free 30-minute discovery call. We'll talk through your biggest operational challenges, identify where the real friction is, and figure out together which engagement makes the most sense for your business right now."):
    return f"""<section class="cta" aria-labelledby="cta-h"><div class="wrap"><div class="t"><h2 id="cta-h">{h}</h2><p>{p}</p><p class="fine">Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a> · {PHONE}</p></div><a class="btn btn-navy" href="{BOOKING}" data-track="band_cta">Book My Call</a></div></section>"""

def method_block(light=False):
    cls = "steps light" if light else "steps"
    items = "".join(f'<li><p class="n">0{i+1}</p><h3>{n}</h3><p class="does">{d}</p></li>' for i,(n,d) in enumerate(METHOD))
    return f"""<div class="{cls}">{items}</div><p class="method-note">Simple, structured, and built around your business. No fluff. No unnecessary steps. Just results.</p>"""

def footer():
    svc = "".join(f'<li><a href="{t["slug"]}.html">{t["nav"]}</a></li>' for t in TRACKS)
    return f"""
<footer class="foot"><div class="wrap">
 <div class="fcols">
  <div class="col about"><p class="fb">{FIRM}</p><p class="fa">{TAGLINE}<br>Independent project &amp; program management consulting by {FOUNDER}, {TITLE}. {CITY_AREA}.</p><address class="fa"><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address></div>
  <div class="col"><p class="fh">Services</p><ul>{svc}<li><a href="services.html">All services</a></li></ul></div>
  <div class="col"><p class="fh">Company</p><ul><li><a href="about.html">About {FOUNDER}</a></li><li><a href="contact.html">Contact</a></li><li><a href="{LINKEDIN}" rel="noopener" target="_blank">LinkedIn</a></li></ul></div>
  <div class="col"><p class="fh">Start here</p><ul><li><a href="{BOOKING}">Schedule a consultation</a></li><li><a href="privacy.html">Privacy policy</a></li></ul></div>
 </div>
 <div class="legal"><p>© <span id="yr"></span> {FIRM}. All rights reserved.</p></div>
</div></footer>
<div class="stickybar" id="stickybar" aria-hidden="true"><a class="btn btn-gold" href="{BOOKING}" data-track="sticky_cta">Book a Discovery Call</a><a class="btn btn-line" href="tel:{PHONE_TEL}">Call</a></div>
"""

def schema_base():
    return {"@context":"https://schema.org","@graph":[
      {"@type":"ProfessionalService","@id":f"{SITE_URL}/#org","name":FIRM,"url":SITE_URL+"/","telephone":PHONE_TEL,"email":EMAIL,
       "address":{"@type":"PostalAddress","addressLocality":"Bowie","addressRegion":"MD","addressCountry":"US"},"areaServed":CITY_AREA,
       "founder":{"@id":f"{SITE_URL}/#founder"},"description":"Operational and project management consulting for federal, nonprofit, and private-sector organizations."},
      {"@type":"Person","@id":f"{SITE_URL}/#founder","name":FOUNDER,"jobTitle":TITLE,"worksFor":{"@id":f"{SITE_URL}/#org"},"url":f"{SITE_URL}/about.html","hasCredential":{"@type":"EducationalOccupationalCredential","name":"Project Management Professional (PMP)"}},
      {"@type":"WebSite","@id":f"{SITE_URL}/#site","url":SITE_URL+"/","name":FIRM,"publisher":{"@id":f"{SITE_URL}/#org"}}]}

def page(fn, title, desc, active, body, extra_schema=None, crumb=None, noindex=False):
    sch = schema_base()
    if crumb:
        sch["@graph"].append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":f"{SITE_URL}/{h}"} for i,(n,h) in enumerate([("Home","index.html")]+[(t,h or fn) for t,h in crumb])]})
    if extra_schema: sch["@graph"] += extra_schema
    robots = '<meta name="robots" content="noindex,nofollow">' if noindex else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">{robots}
<link rel="canonical" href="{SITE_URL}/{fn if fn!='index.html' else ''}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{esc(FIRM)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE_URL}/{fn}">
<meta name="theme-color" content="#111e32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap"></noscript>
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(sch, ensure_ascii=False)}</script>
</head>
<body>
{header(active)}
<main id="main" tabindex="-1">
{body}
</main>
{footer()}
<script defer>{JS}</script>
</body>
</html>"""

# ------------------------------------------------------------ HOME
svc_cards = "".join(f'<article><h3><a href="{t["slug"]}.html">{t["nav"]}</a></h3><p class="tag">{t["tag"]}</p><p>{t["short"]}</p><a class="more" href="{t["slug"]}.html" aria-label="Explore {t["nav"]}">Explore {ARROW}</a></article>' for t in TRACKS)

def flat_packages():
    order = []
    for t in TRACKS:
        for p in PACKAGES.get(t["slug"], []):
            order.append((p, t["slug"]))
    return order

pkg_teaser_cards = "".join(
    f'<article><p class="n">0{i+1}</p><h3><a href="{slug}.html">{p["name"]}</a></h3><p class="tag">{p["tier"]} &middot; {p["dur"]}</p><p>{p["desc"]}</p><a class="more" href="{slug}.html" aria-label="Learn more: {p["name"]}">Learn more {ARROW}</a></article>'
    for i,(p,slug) in enumerate(flat_packages())
)

home = f"""
<section class="hero" aria-labelledby="h1"><div class="ring r1" aria-hidden="true"></div>
 <div class="wrap"><div class="split">
  <div class="copy">
   <p class="kicker">Business Solutions Architect</p>
   <h1 id="h1">Streamlined operations.<br>Scalable results.</h1>
   <p class="lede quote">"{TAGLINE}"</p>
   <p class="lede">You don't need more processes. You need the right ones. {FIRM} designs and implements operational systems that eliminate friction, align your team, and move your business forward — without adding to your plate.</p>
   <div class="acts"><a class="btn btn-gold" href="{BOOKING}" data-track="hero_cta">Book a Free Discovery Call</a><a class="btn btn-line" href="services.html">View Services</a></div>
  </div>
  <div class="photo"><img src="data:image/jpeg;base64,{HERO_B64}" alt="{FOUNDER}, {TITLE}, founder of {FIRM}" width="700" height="1048" fetchpriority="high"></div>
 </div></div>
</section>

<section class="sec sec-stone" aria-labelledby="proof-h"><div class="wrap proof">
 <div><h2 id="proof-h" class="vh">Credentials</h2><div class="nums"><div class="stat"><p class="n">{YEARS}</p><p class="l">Years Experience</p></div><div class="stat"><p class="n">3</p><p class="l">Sectors Served</p></div><div class="stat"><p class="n">{CERTS}</p><p class="l">Certified</p></div></div></div>
</div></section>

<section class="sec sec-navy" id="method" aria-labelledby="method-h"><div class="wrap">
 <div class="head"><div class="t"><h2 id="method-h">The MaizeWay Method</h2></div></div>
 {method_block()}
</div></section>

<section class="sec" id="services" aria-labelledby="svc-h"><div class="wrap">
 <div class="head"><div class="t"><h2 id="svc-h">Five ways to work together.</h2><p class="sub">Every engagement is built around your business — where it is today and where you're taking it. Choose the level of support that fits your season.</p></div><a class="more" href="services.html">All services {ARROW}</a></div>
 <div class="svc pkgteaser">{pkg_teaser_cards}</div>
</div></section>

<section class="sec sec-stone" id="about" aria-labelledby="ab-h"><div class="wrap about">
 <div class="img"><img src="data:image/jpeg;base64,{ABOUT_B64}" alt="{FOUNDER}, founder of {FIRM}" width="600" height="899" loading="lazy"></div>
 <div class="t"><p class="kicker">Business Solutions Architect</p><h2 id="ab-h">{FOUNDER}, {CERTS}</h2><p class="sub">I'm a Business Solutions Architect with over 12 years of experience across federal government, nonprofit, and private consulting sectors — diagnosing what's broken, architecting what's missing, implementing solutions that stick.</p>
  <a class="btn btn-dark" href="about.html">More About {FOUNDER}</a></div>
</div></section>

{cta_band()}
"""

# ------------------------------------------------------------ SERVICES INDEX
services = f"""
{crumbs([("Services",None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><h1>Five ways to work together.</h1><p class="lede">Every engagement is built around your business — where it is today and where you're taking it. Choose the level of support that fits your season.</p></div></section>
<section class="sec"><div class="wrap">
 {"".join(f'''<article class="svcrow" id="{t["slug"]}"><div><h2><a href="{t["slug"]}.html">{t["h1"]}</a></h2><p class="tag">{t["tag"]}</p><p class="sub">{t["short"]}</p><a class="btn btn-dark" href="{t["slug"]}.html">Explore {t["nav"]}</a></div><ul class="ticks"><li>{CHECK}<span><b>Who it's for</b> — {t["who"]}</span></li><li>{CHECK}<span><b>Structure</b> — {t["structure"]}</span></li></ul></article>''' for t in TRACKS)}
</div></section>
<section class="sec sec-stone"><div class="wrap">
 <div class="head"><div class="t"><h2>Ways to start.</h2><p class="sub">Every track below opens with a scoped entry point. Fees are quoted after a short call, once the scope is real — nothing here is a rate card. <span class="fine">[Price for each package needed from Eunice.]</span></p></div></div>
 {"".join(pkg_section(t) for t in TRACKS)}
</div></section>
<section class="sec"><div class="wrap" style="text-align:center">
 <p class="kicker">Not sure which fits?</p><h2>Start with a conversation, not a decision.</h2>
 <p class="sub" style="max-width:560px;margin:16px auto 0">Most engagements start with a 30-minute call and, if it makes sense, a short diagnostic. We'll figure out the shape together.</p>
</div></section>
{cta_band()}
"""

def service_page(t, i):
    others = [o for o in TRACKS if o is not t]
    dl = "".join(f"<li>{CHECK}{d}</li>" for d in t["deliverables"])
    sch = [{"@type":"Service","name":t["h1"],"serviceType":t["h1"],"provider":{"@id":f"{SITE_URL}/#org"},"areaServed":CITY_AREA,"description":t["short"],"url":f"{SITE_URL}/{t['slug']}.html"}]
    body = f"""
{crumbs([("Services","services.html"),(t["nav"],None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">Track 0{i+1}</p><h1>{t["h1"]}</h1><p class="lede">{t["tag"]}</p><div class="acts"><a class="btn btn-gold" href="{BOOKING}" data-track="svc_hero_cta">{t["cta"]}</a></div></div></section>
<section class="sec"><div class="wrap grid g2 po">
 <div><p class="kicker">Who needs this</p><p class="sub">{t["who"]}</p></div>
 <div><p class="kicker">Problems it solves</p><p class="sub">{t["problems"]}</p></div>
</div></section>
<section class="sec sec-stone"><div class="wrap">
 <div class="head"><div class="t"><h2>What I do.</h2><p class="sub">{t["does"]}</p></div></div>
 <div class="grid g2"><ul class="ticks card">{dl}</ul>
  <div class="card"><p class="kicker">Engagement structure</p><p class="sub">{t["structure"]}</p></div></div>
</div></section>
<section class="sec"><div class="wrap">
 <div class="head"><div class="t"><h2>How to start.</h2></div></div>
 <div class="grid {"g2" if len(PACKAGES.get(t["slug"],[])) in (2,4) else "g3"} pkgs">{"".join(pkg_card(p) for p in PACKAGES.get(t["slug"],[]))}</div>
</div></section>
<section class="sec"><div class="wrap"><p class="kicker">Also</p><div class="grid g2">{"".join(f'<a class="card link-card" href="{o["slug"]}.html"><h3>{o["h1"]}</h3><p>{o["short"]}</p><span class="more">Details {ARROW}</span></a>' for o in others)}</div></div></section>
{cta_band(t["cta"]+".", t["short"])}
"""
    return body, sch

# ------------------------------------------------------------ ABOUT
beliefs_html = "".join(f'<blockquote>{b}</blockquote>' for b in BELIEFS)
about = f"""
{crumbs([("About",None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">About</p><h1>{FOUNDER}, {CERTS}</h1><p class="lede">I'm a Business Solutions Architect with over 12 years of experience across federal government, nonprofit, and private consulting sectors.</p></div></section>

<section class="sec"><div class="wrap about">
 <div class="img"><img src="data:image/jpeg;base64,{ABOUT_B64}" alt="{FOUNDER}, founder of {FIRM}" width="600" height="899" loading="lazy"></div>
 <div class="t"><p class="kicker">Why {FIRM} exists</p><h2>[Headline — the moment she decided this practice needed to exist.]</h2>
  <p class="sub">[The origin story, in her own words. Not a career summary — the specific moment or pattern that led here. Example shape only: "I spent {YEARS} years watching capable teams miss dates for reasons that had nothing to do with effort." Eunice supplies the real version — this is the paragraph readers remember.]</p></div>
</div></section>

<section class="sec sec-stone"><div class="wrap">
 <div class="head"><div class="t"><h2>Where I've worked.</h2></div></div>
 <p class="sub" style="max-width:760px">[Federal, nonprofit, and consulting — what she actually did in each: program types, scale, the kind of problems. Named organizations if she can name them; descriptive if she can't, e.g. "a federal health agency," "a national education nonprofit."]</p>
</div></section>

<section class="sec"><div class="wrap">
 <div class="head"><div class="t"><h2>How I think about projects.</h2><p class="sub">Stated as opinions, not platitudes — three or four beliefs I'll defend.</p></div></div>
 <div class="beliefs">{beliefs_html}</div>
</div></section>

<section class="sec sec-stone"><div class="wrap">
 <div class="head"><div class="t"><h2>Credentials.</h2></div></div>
 <ul class="creds">
  <li><b>PMP</b> — Project Management Institute. <span class="fine">[Certification number and issue date needed.]</span></li>
  <li><b>MPA</b> — Bowie State University. <span class="fine">[Graduation year needed.]</span></li>
  <li><b>BS</b> — University of Maryland. <span class="fine">[Degree title and graduation year needed.]</span></li>
 </ul>
</div></section>

<section class="sec sec-navy" id="approach"><div class="wrap">
 <div class="head"><div class="t"><h2>How I work.</h2><p class="sub">The MaizeWay Method, as personal practice.</p></div></div>
 {method_block()}
</div></section>

<section class="sec"><div class="wrap" style="max-width:700px">
 <p class="kicker">A little about me</p>
 <p class="sub">[Two or three sentences, human and specific — {CITY_AREA}, something real, not a hobbies list.]</p>
</div></section>

{cta_band()}
"""

# ------------------------------------------------------------ CONTACT
contact = f"""
{crumbs([("Contact",None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">Contact</p><h1>Ready to stop managing chaos and start scaling with clarity?</h1><p class="lede">Book a free 30-minute discovery call. We'll talk through your biggest operational challenges and figure out which engagement fits. If it's urgent, call — {PHONE}.</p></div></section>
<section class="sec"><div class="wrap contact">
 <div><h2>What happens next.</h2>
  <ol class="next"><li><b>I read what you sent</b> and respond within one business day.</li><li><b>We talk for 30 minutes.</b> You describe the situation, I tell you how I'd approach it.</li><li><b>If it's a fit, I send a scoped proposal</b> within three business days. If it isn't, I'll tell you and point you toward someone better suited.</li></ol>
  <div class="cinfo"><div><b>Phone</b><p><a href="tel:{PHONE_TEL}">{PHONE}</a></p></div><div><b>Email</b><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div><div><b>Serving</b><p>{CITY_AREA}</p></div></div></div>
 <form class="f" id="cform" data-form action="https://formsubmit.co/{FORM_EMAIL}" method="POST" novalidate>
  <input type="hidden" name="_subject" value="New consultation request — {FIRM} website"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{SITE_URL}/thank-you.html"><input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
  <label>Name<input name="Name" autocomplete="name" required></label>
  <label>Email<input name="email" type="email" autocomplete="email" required></label>
  <label>Organization<input name="Organization" autocomplete="organization" required></label>
  <label>Title<input name="Title" autocomplete="organization-title" required></label>
  <label>Phone (optional)<input name="Phone" type="tel" autocomplete="tel"></label>
  <label>Organization type<select name="Organization Type"><option>Federal agency</option><option>Federal contractor</option><option>Nonprofit</option><option>Private company</option><option>Other</option></select></label>
  <label class="full">What's the situation?<textarea name="Message" rows="4" required placeholder="A few sentences is plenty — we'll go deeper on the call."></textarea></label>
  <label class="full">Timeline<select name="Timeline"><option>Immediate</option><option>Within 30 days</option><option>This quarter</option><option>Exploring</option></select></label>
  <p class="err full" role="alert"></p>
  <button class="btn btn-gold full" type="submit">Book My Call</button>
 </form>
</div></section>
"""

thankyou = f"""
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">Received</p><h1>Thank you.</h1><p class="lede">Your message is in. I respond within one business day — usually faster.</p></div></section>
<section class="sec"><div class="wrap grid g2">
 <div><h2>While you wait</h2><ol class="next"><li><b>Add me to your safe senders</b> so the reply doesn't land in spam: {EMAIL}</li><li><b>Skim how an engagement runs</b> — <a class="link" href="about.html#approach">the MaizeWay Method</a>.</li><li><b>Something urgent?</b> Call {PHONE}.</li></ol></div>
</div></section>
"""

privacy = f"""
{crumbs([("Privacy policy",None)])}
<section class="sec"><div class="wrap prose"><h1>Privacy policy</h1><p><em>Last updated [date].</em></p>
<h2>What is collected</h2><p>When you submit the contact form, {FIRM} collects the information you enter (name, email, organization, message) in order to respond to you.</p>
<h2>How it is used</h2><p>To reply to your enquiry and to follow up about working together. Your information is not sold or shared.</p>
<h2>Third parties</h2><p>Forms are delivered by FormSubmit. Fonts are served by Google Fonts.</p>
<h2>Your rights</h2><p>Email <a class="link" href="mailto:{EMAIL}">{EMAIL}</a> to access, correct, or delete your information.</p></div></section>
"""

notfound = f"""
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">404</p><h1>That page has moved on.</h1><div class="acts"><a class="btn btn-gold" href="index.html">Home</a><a class="btn btn-line" href="services.html">Services</a><a class="btn btn-line" href="contact.html">Contact</a></div></div></section>
"""

# ------------------------------------------------------------ WRITE
pages = [
 ("index.html", f"{FIRM} | Project Management Consulting", f"{FOUNDER} is a Business Solutions Architect with over 12 years of experience across federal government, nonprofit, and private consulting sectors. {CITY_AREA}.", "home", home, None, None),
 ("services.html", f"Services | {FIRM}", "Program and project leadership, project recovery, and federal and nonprofit delivery support — scoped to the problem, not a tiered package.", "services", services, None, [("Services",None)]),
 ("about.html", f"About {FOUNDER} | {FIRM}", f"{FOUNDER}, {TITLE}: {YEARS} years leading programs across federal, nonprofit, and consulting environments.", "about", about, None, [("About",None)]),
 ("contact.html", f"Book a Free Discovery Call | {FIRM}", f"Book a free 30-minute discovery call with {FOUNDER}. We'll talk through your biggest operational challenges and figure out which engagement fits.", "contact", contact, None, [("Contact",None)]),
]
for i,t in enumerate(TRACKS):
    b,sch = service_page(t,i)
    pages.append((f"{t['slug']}.html", f"{t['h1']} | {FIRM}", t["short"], "services", b, sch, [("Services","services.html"),(t["nav"],None)]))
for fn,tt,d,a,b,sch,cr in pages:
    open(os.path.join(OUT,fn),"w").write(page(fn,tt,d,a,b,sch,cr))
open(os.path.join(OUT,"thank-you.html"),"w").write(page("thank-you.html",f"Thank you | {FIRM}","Message received.","",thankyou,noindex=True))
open(os.path.join(OUT,"privacy.html"),"w").write(page("privacy.html",f"Privacy Policy | {FIRM}","How this site handles your information.","",privacy,crumb=[("Privacy policy",None)]))
open(os.path.join(OUT,"404.html"),"w").write(page("404.html",f"Page not found | {FIRM}","Page not found.","",notfound,noindex=True))

today = datetime.date.today().isoformat()
urls = [p[0] for p in pages]
open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'  <url><loc>{SITE_URL}/{u if u!="index.html" else ""}</loc><lastmod>{today}</lastmod><priority>{"1.0" if u=="index.html" else "0.8"}</priority></url>\n' for u in urls)+'</urlset>\n')
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT,"favicon.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#111e32" stroke="#c5973a" stroke-width="2"/><text x="32" y="40" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="20" fill="#c5973a">MW</text></svg>')
print("built", len(urls)+3, "pages")
