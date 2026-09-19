import os, json, html, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE
os.makedirs(OUT, exist_ok=True)

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
LINKEDIN   = "[LinkedIn URL]"  # placeholder — omit footer link until a real URL is set
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
      cta="Discuss your initiative"),
 dict(slug="project-recovery", nav="Project Recovery", h1="When a Project Is Already Off Track",
      tag="An honest assessment of what's recoverable, then hands-on leadership through the recovery.",
      short="Rapid assessment, a re-baselined plan, and leadership through stabilization — not just a report.",
      who="A leader who has already tried to fix it internally, and now has a date, a budget, or a commitment at risk.",
      problems="Missed deliverables. Scope that outgrew the plan. A team that has lost confidence. Leadership that no longer trusts the status reports.",
      does="A rapid, independent assessment in the first week gives you an honest picture of what's recoverable. From there I re-baseline the plan and lead the recovery — I don't hand over a report and leave.",
      deliverables=["Recovery assessment (week 1)","Re-baselined plan and scope","Stakeholder communication plan","Revised governance","Weekly executive reporting through stabilization"],
      structure="A one-week assessment, which can be purchased standalone, followed by a 60–90 day recovery.",
      cta="Get an honest assessment"),
 dict(slug="federal-nonprofit-delivery", nav="Federal & Nonprofit Delivery Support", h1="Program Support for Compliance-Driven, Resource-Constrained Teams",
      tag="Built for environments where the reporting requirements come from outside and the team executing is small.",
      short="Portfolio management, acquisition planning support, federal reporting, and audit-ready SOPs.",
      who="Federal contractors and subcontractors, federal program offices, and nonprofits managing grants, funder reporting, or a program launch.",
      problems="Reporting obligations with no supporting process. Acquisition planning capacity gaps. Data calls consuming the whole team. SOPs that don't survive an audit. Grant deliverables with no delivery structure.",
      does="Portfolio and program management, acquisition planning support, federal reporting and data call management, compliance-aligned SOP development, and stakeholder engagement strategy.",
      deliverables=["Compliance-aligned SOPs","Reporting calendar and templates","Data call response process","Program documentation package","Stakeholder engagement plan"],
      structure="Custom scope — project or retainer.",
      cta="Request a capability discussion"),
]

# Entry / core / ongoing packages — services "Ways to start" + each track page.
# No prices on site: fees quoted after a short call once scope is real.
PACKAGES = [
 dict(track="program-project-leadership", tier="Entry · Assessment", name="The Efficiency Audit",
      desc="A focused deep-dive into your operations, workflows, and team processes. You walk away with a prioritized action plan that shows exactly where the initiative is losing time, budget, and momentum.",
      includes=["Operations & workflow assessment","Bottleneck identification report","Prioritized recommendations roadmap","60-min debrief session"],
      best_for="Organizations sizing up a bigger initiative", cta="Start here"),
 dict(track="program-project-leadership", tier="Entry · One day", name="The VIP Strategy Day",
      desc="A full-day intensive working session. We map the operational landscape together, identify the highest-leverage opportunities, and build a concrete 90-day execution plan in a single focused sitting.",
      includes=["Full-day working session (6 hrs)","Operational landscape mapping","90-day execution roadmap","2-week post-day email support"],
      best_for="Decisive leaders who want a plan in a day", cta="Reserve a day"),
 dict(track="program-project-leadership", tier="Core · 30–90 days", name="The Solutions Sprint",
      desc="Hands-on program and project leadership to implement operational fixes and build the structure that gets a specific initiative to the finish line.",
      includes=["Project management & execution","Workflow design & implementation","Team alignment & SOPs","Weekly check-ins & reporting"],
      best_for="Initiatives mid-transition or launching new", cta="Let's talk scope"),
 dict(track="program-project-leadership", tier="Ongoing · Monthly", name="The Strategic Partner Retainer",
      desc="Ongoing monthly leadership for organizations that need a senior program partner embedded on a recurring basis — priority oversight across whatever is in flight, without a full-time hire.",
      includes=["Monthly strategy sessions","On-call advisory support","Ongoing process optimization","Priority project oversight","Monthly performance reporting"],
      best_for="Leaders who want a senior partner embedded year-round", cta="Apply for a retainer"),
 dict(track="project-recovery", tier="Entry · One week", name="The Recovery Assessment",
      desc="A rapid, independent assessment of a project already showing red status. You get an honest read on what's recoverable and what it will take — before committing to a full recovery engagement.",
      includes=["Rapid independent assessment","Root-cause findings","Recoverability verdict","Re-baseline recommendation"],
      best_for="A project already showing red status", cta="Get an assessment"),
 dict(track="project-recovery", tier="Core · 60–90 days", name="The Recovery Engagement",
      desc="Hands-on leadership through stabilization once the assessment is done — re-baselining the plan and leading the recovery, not just handing over a report.",
      includes=["Re-baselined plan & scope","Stakeholder communication plan","Revised governance","Weekly executive reporting through stabilization"],
      best_for="Leadership that needs the recovery led, not just diagnosed", cta="Discuss recovery"),
 dict(track="federal-nonprofit-delivery", tier="Specialized · Custom", name="Federal & Nonprofit Solutions",
      desc="Tailored program and project management support for federal agencies, contractors, and mission-driven nonprofits — built around reporting obligations that come from outside and delivery teams that are often small.",
      includes=["Portfolio & program management","Acquisition planning support","Federal reporting & data calls","Compliance-aligned SOPs","Stakeholder engagement strategy"],
      best_for="Federal agencies, contractors & nonprofits", cta="Request a proposal"),
]


METHOD = [
 ("Discover","Objectives, constraints, stakeholders, what's already been tried.","Engagement brief and success criteria","Week 1"),
 ("Diagnose","Where the work is actually breaking down — process, ownership, sequence, or capacity.","Findings report with prioritized root causes","Weeks 1–2"),
 ("Architect","Design the operating model that fits your constraints.","Operating model, RACI, sequenced plan, governance and reporting design","Weeks 2–4"),
 ("Execute","Lead the work through delivery; adjust as reality intervenes.","Weekly reporting, a managed risk register, decisions driven to close","Weeks 4–12"),
 ("Hand Off","Transfer the structure to your team.","SOPs, templates, documented governance, a transition session","Final 2 weeks"),
]


ENGAGEMENT = [
 ("Intro call","A 30-minute conversation about the initiative, constraints, and whether MaizeWay is the right fit.","Before kickoff"),
 ("Week 1","Discover and diagnose: map stakeholders, surface what's already been tried, and name the real failure points.","Days 1–7"),
 ("Weeks 2–4","Architect the operating model — ownership, sequence, governance, and the reporting cadence leadership will trust.","Design phase"),
 ("Weeks 4–12","Execute: lead delivery, drive decisions to close, and keep risk and status visible week by week.","Delivery"),
 ("Handoff","Transfer the structure to your team — SOPs, templates, governance, and a clean transition session.","Final weeks"),
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
 <a class="brand" href="index.html" aria-label="{FIRM} home"><span class="mark" aria-hidden="true">MW</span><span class="name">{FIRM}</span></a>
 <nav aria-label="Primary"><ul class="menu">
  <li{cls('services')}><a href="services.html" aria-haspopup="true" aria-expanded="false">Services {CARET}</a><div class="dd" role="menu">{dd}<a href="services.html" role="menuitem" class="all">All services {ARROW}</a></div></li>
  <li{cls('about')}><a href="about.html">About</a></li>
  <li><a class="btn btn-gold cta" href="{BOOKING}" data-track="nav_cta">Schedule a Consultation</a></li>
 </ul></nav>
 <a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE}</a>
 <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<div class="mnav" id="mnav" role="dialog" aria-modal="true" aria-label="Menu" aria-hidden="true">
 <div class="top"><a class="brand" href="index.html"><span class="mark sm" aria-hidden="true">MW</span><span class="name sm">{FIRM}</span></a><button class="burger" id="mclose" aria-label="Close menu"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
 <nav aria-label="Mobile">
  <button class="row" data-acc aria-expanded="false" aria-controls="msub"><span>Services</span><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></button>
  <div class="sub" id="msub">{mob}<a href="services.html">All services</a></div>
  <a class="row" href="about.html">About</a>
  <a class="row" href="contact.html">Contact</a>
 </nav>
 <div class="foot"><a class="btn btn-gold" href="{BOOKING}">Schedule a Consultation</a><div class="ln"><a href="tel:{PHONE_TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
</div>
"""

def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for t,h in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol><li><a href="index.html">Home</a></li>{lis}</ol></div></nav>'

def cta_band(h="Tell me what's stuck.", p="A 30-minute consultation. You describe the initiative and where it's breaking down; I'll tell you what I'd do about it and whether I'm the right person for it. No pitch deck."):
    return f"""<section class="cta" aria-labelledby="cta-h"><div class="wrap"><div class="t"><h2 id="cta-h">{h}</h2><p>{p}</p><p class="fine">Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a> · {PHONE}</p></div><a class="btn btn-navy" href="{BOOKING}" data-track="band_cta">Schedule a Consultation</a></div></section>"""

def method_block(light=False):
    cls = "steps light" if light else "steps"
    items = "".join(f'<li><p class="n">0{i+1}</p><h3>{n}</h3><p class="does">{d}</p><p class="get"><b>You get:</b> {g}</p><p class="dur">{dur}</p></li>' for i,(n,d,g,dur) in enumerate(METHOD))
    return f"""<div class="{cls}">{items}</div><p class="method-note">Most engagements move through all five stages in 30 to 90 days. The scope of an engagement is the initiative, not the calendar.</p>"""

def packages_for(slug):
    return [p for p in PACKAGES if p["track"] == slug]

def render_package(p):
    ticks = "".join(f"<li>{CHECK}{esc(i)}</li>" for i in p["includes"])
    if " · " in p["tier"]:
        a, b = p["tier"].split(" · ", 1)
        kicker = f"{esc(a)} &middot; {esc(b).upper()}"
    else:
        kicker = esc(p["tier"])
    return (
        f'<article class="pkg">'
        f'<p class="pkg-kicker">{kicker}</p>'
        f'<h3>{esc(p["name"])}</h3>'
        f'<p class="pkg-desc">{esc(p["desc"])}</p>'
        f'<ul class="ticks">{ticks}</ul>'
        f'<div class="pkg-foot"><span class="pkg-bestfor">Best for: {esc(p["best_for"])}</span>'
        f'<a class="more" href="{BOOKING}">{esc(p["cta"])} {ARROW}</a></div>'
        f'</article>'
    )

def packages_grid(pkgs, cols=None):
    if not pkgs:
        return ""
    n = cols if cols is not None else (3 if len(pkgs) == 1 else 2)
    g = "g3" if n >= 3 else "g2"
    return f'<div class="grid {g} pkgs">{"".join(render_package(p) for p in pkgs)}</div>'

def ways_to_start_section():
    groups = []
    for t in TRACKS:
        pkgs = packages_for(t["slug"])
        if not pkgs:
            continue
        cols = 3 if t["slug"] == "federal-nonprofit-delivery" else 2
        groups.append(
            f'<div class="pkg-group"><h3 class="pkg-group-h">'
            f'<a href="{t["slug"]}.html">{esc(t["nav"])}</a></h3>'
            f'{packages_grid(pkgs, cols)}</div>'
        )
    note = (
        "Every track below opens with a scoped entry point. "
        "Fees are quoted after a short call, once the scope is real — nothing here is a rate card. "
        "Package fees are quoted after discovery."
    )
    return (
        f'<section class="sec sec-stone"><div class="wrap">'
        f'<div class="head"><div class="t"><h2>Ways to start.</h2>'
        f'<p class="sub">{note}</p></div></div>'
        f'{"".join(groups)}</div></section>'
    )

def track_packages_section(t):
    pkgs = packages_for(t["slug"])
    if not pkgs:
        return ""
    cols = 3 if t["slug"] == "federal-nonprofit-delivery" else 2
    return (
        f'<section class="sec"><div class="wrap">'
        f'<div class="head"><div class="t"><h2>How to start.</h2>'
        f'<p class="sub">Fees are quoted after a short call, once the scope is real.</p></div></div>'
        f'{packages_grid(pkgs, cols)}</div></section>'
    )


def footer():
    svc = "".join(f'<li><a href="{t["slug"]}.html">{t["nav"]}</a></li>' for t in TRACKS)
    # Hide LinkedIn until a real URL replaces the placeholder
    li_link = ""
    if LINKEDIN and not LINKEDIN.startswith("["):
        li_link = f'<li><a href="{esc(LINKEDIN)}" rel="noopener" target="_blank">LinkedIn</a></li>'
    return f"""
<footer class="foot"><div class="wrap">
 <div class="fcols">
  <div class="col about"><p class="fb">{FIRM}</p><p class="fa">{TAGLINE}<br>Independent project &amp; program management consulting by {FOUNDER}, {TITLE}. {CITY_AREA}.</p><address class="fa"><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address></div>
  <div class="col"><p class="fh">Services</p><ul>{svc}<li><a href="services.html">All services</a></li></ul></div>
  <div class="col"><p class="fh">Company</p><ul><li><a href="about.html">About {FOUNDER}</a></li><li><a href="contact.html">Contact</a></li>{li_link}</ul></div>
  <div class="col"><p class="fh">Start here</p><ul><li><a href="{BOOKING}">Schedule a consultation</a></li><li><a href="privacy.html">Privacy policy</a></li></ul></div>
 </div>
 <div class="legal"><p>© <span id="year">2026</span> {FIRM}. All rights reserved.</p></div>
</div></footer>
<div class="stickybar" id="stickybar" aria-hidden="true"><a class="btn btn-gold" href="{BOOKING}" data-track="sticky_cta">Schedule a Consultation</a><a class="btn btn-line" href="tel:{PHONE_TEL}">Call</a></div>
"""

def schema_base():
    return {"@context":"https://schema.org","@graph":[
      {"@type":"ProfessionalService","@id":f"{SITE_URL}/#org","name":FIRM,"url":SITE_URL+"/","telephone":PHONE_TEL,"email":EMAIL,
       "address":{"@type":"PostalAddress","addressLocality":"Bowie","addressRegion":"MD","addressCountry":"US"},"areaServed":CITY_AREA,
       "founder":{"@id":f"{SITE_URL}/#founder"},"description":"Fractional project and program management consulting for federal, nonprofit, and mission-driven organizations."},
      {"@type":"Person","@id":f"{SITE_URL}/#founder","name":FOUNDER,"jobTitle":TITLE,"worksFor":{"@id":f"{SITE_URL}/#org"},"url":f"{SITE_URL}/about.html","hasCredential":{"@type":"EducationalOccupationalCredential","name":"Project Management Professional (PMP)"}},
      {"@type":"WebSite","@id":f"{SITE_URL}/#site","url":SITE_URL+"/","name":FIRM,"publisher":{"@id":f"{SITE_URL}/#org"}}]}

def analytics_head():
    """Placeholders only — replace G-XXXXXXXX / YOUR_CLARITY_ID / Search Console code when client provides IDs."""
    return """
<!-- ANALYTICS: needs IDs from client before launch
  GA4 measurement ID: G-XXXXXXXX  (replace stub below)
  Google Search Console: add verification meta when ready
  Microsoft Clarity: YOUR_CLARITY_ID
-->
<!-- <meta name="google-site-verification" content="SEARCH_CONSOLE_VERIFICATION_TOKEN"> -->
<script>
/* GA4 stub — no-ops until a real measurement ID is set */
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}
window.gtag=gtag;
/* TODO: set GA4_ID = 'G-XXXXXXXX' from client, then uncomment:
(function(){
  var GA4_ID='G-XXXXXXXX';
  if(!GA4_ID||GA4_ID.indexOf('X')>=0)return;
  var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+GA4_ID;
  document.head.appendChild(s);
  gtag('js',new Date());gtag('config',GA4_ID);
})();
*/
</script>
<script>
/* Microsoft Clarity stub — replace YOUR_CLARITY_ID when provided
(function(c,l,a,r,i,t,y){
  if(!i||i==='YOUR_CLARITY_ID')return;
  c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
  t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
  y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "YOUR_CLARITY_ID");
*/
</script>
"""

def page(fn, title, desc, active, body, extra_schema=None, crumb=None, noindex=True):
    sch = schema_base()
    if crumb:
        sch["@graph"].append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":f"{SITE_URL}/{h}"} for i,(n,h) in enumerate([("Home","index.html")]+[(t,h or fn) for t,h in crumb])]})
    if extra_schema: sch["@graph"] += extra_schema
    # Pre-launch: noindex sitewide until go-live
    robots = '<meta name="robots" content="noindex, nofollow">'
    og_image = f"{SITE_URL}/images/og-default.jpg"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{SITE_URL}/{fn if fn!='index.html' else ''}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{esc(FIRM)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE_URL}/{fn}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#111e32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap"></noscript>
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(sch, ensure_ascii=False)}</script>
{analytics_head()}
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


def engagement_block():
    items = "".join(
        f'<li><span class="dot" aria-hidden="true">{i:02d}</span><span class="when">{esc(when)}</span><h3>{esc(title)}</h3><p>{esc(desc)}</p></li>'
        for i, (title, desc, when) in enumerate(ENGAGEMENT, 1)
    )
    return f"""<section class="sec sec-cream" id="engagement" aria-labelledby="eng-h"><div class="wrap">
 <div class="head"><div class="t"><p class="kicker">Engagement</p><h2 id="eng-h">How an engagement works</h2><p class="sub">Fractional program leadership with a clear arc — from the first conversation through a clean handoff your team can run without me.</p></div></div>
 <ol class="engage">{items}</ol>
</div></section>"""

# ------------------------------------------------------------ HOME
svc_cards = "".join(f'<article><h3><a href="{t["slug"]}.html">{t["nav"]}</a></h3><p class="tag">{t["tag"]}</p><p>{t["short"]}</p><a class="more" href="{t["slug"]}.html" aria-label="Explore {t["nav"]}">Explore {ARROW}</a></article>' for t in TRACKS)

home = f"""
<section class="hero" aria-labelledby="h1"><div class="ring r1" aria-hidden="true"></div>
 <div class="wrap"><div class="split">
  <div class="copy">
   <p class="kicker">Fractional Program &amp; Project Leadership</p>
   <h1 id="h1">When the work matters and the structure isn't there.</h1>
   <p class="lede">I'm {FOUNDER} — a program leader who steps into complex initiatives for federal, nonprofit, and mission-driven organizations, builds the structure that makes them finish, and hands it back to your team.</p>
   <div class="acts"><a class="btn btn-gold" href="{BOOKING}" data-track="hero_cta">Schedule a Consultation</a><a class="btn btn-line" href="#method">How I Work</a></div>
  </div>
  <div class="photo"><img src="data:image/jpeg;base64,{HERO_B64}" alt="{FOUNDER}, {TITLE}, founder of {FIRM}" width="700" height="1048" fetchpriority="high"></div>
 </div></div>
</section>

<section class="sec sec-stone" aria-labelledby="proof-h"><div class="wrap proof">
 <div><h2 id="proof-h" class="vh">Credentials</h2><div class="nums"><div class="stat"><p class="n">{YEARS}</p><p class="l">Years — federal, nonprofit &amp; consulting program delivery</p></div><div class="stat"><p class="n">{CERTS}</p><p class="l">Project Management Institute certified</p></div><div class="stat"><p class="n">MPA</p><p class="l">Bowie State University</p></div></div></div>
 <p class="client-line">Work delivered for federal agencies and their contractors, nonprofit organizations, and growing private-sector teams across {CITY_AREA}. <span class="fine">[Confirm this line is accurate before publishing.]</span></p>
</div></section>

<section class="sec" aria-labelledby="prob-h"><div class="wrap">
 <div class="head"><div class="t"><h2 id="prob-h">Projects rarely fail because people stopped working.</h2><p class="sub">They fail because ownership got blurry, the sequence was wrong from the start, or nobody had visibility until a date was already missed. By the time it's obvious, the fix costs three times what it would have.</p></div></div>
 <div class="grid g3">
  <div class="card"><h3>Too many initiatives, not enough sequence.</h3><p>Everything is a priority, so capacity gets split until nothing lands.</p></div>
  <div class="card"><h3>No single owner.</h3><p>Work crosses four teams and belongs to none of them. Decisions wait.</p></div>
  <div class="card"><h3>Status you can't trust.</h3><p>Leadership asks how it's going and the honest answer is that nobody's sure.</p></div>
 </div>
</div></section>

<section class="sec sec-navy" id="method" aria-labelledby="method-h"><div class="wrap">
 <div class="head"><div class="t"><h2 id="method-h">The MaizeWay Method</h2><p class="sub">Five stages. Each one produces something your team keeps — and the last one is the point.</p></div></div>
 {method_block()}
</div></section>

<section class="sec" id="services" aria-labelledby="svc-h"><div class="wrap">
 <div class="head"><div class="t"><h2 id="svc-h">Three ways to bring in program leadership.</h2></div><a class="more" href="services.html">All services {ARROW}</a></div>
 <div class="svc">{svc_cards}</div>
</div></section>

{engagement_block()}

<section class="sec sec-stone" id="about" aria-labelledby="ab-h"><div class="wrap about">
 <div class="img"><img src="data:image/jpeg;base64,{ABOUT_B64}" alt="{FOUNDER}, founder of {FIRM}" width="600" height="899" loading="lazy"></div>
 <div class="t"><p class="kicker">Business Solutions Architect</p><h2 id="ab-h">{FOUNDER}, {CERTS}</h2><p class="sub">I'm a Business Solutions Architect with over 12 years of experience across federal government, nonprofit, and private consulting sectors — diagnosing what's broken, architecting what's missing, implementing solutions that stick.</p>
  <a class="btn btn-dark" href="about.html">More About {FOUNDER}</a></div>
</div></section>

{cta_band()}
"""

# ------------------------------------------------------------ SERVICES INDEX
_svc_rows = "".join(
    '<article class="svcrow" id="{slug}"><div>'
    '<h2><a href="{slug}.html">{h1}</a></h2>'
    '<p class="tag">{tag}</p><p class="sub">{short}</p>'
    '<a class="btn btn-dark" href="{slug}.html">Explore {nav}</a></div>'
    '<ul class="ticks">'
    '<li>{check}<span><b>Who it\'s for</b> — {who}</span></li>'
    '<li>{check}<span><b>Structure</b> — {structure}</span></li>'
    '</ul></article>'.format(
        slug=t["slug"], h1=t["h1"], tag=t["tag"], short=t["short"], nav=t["nav"],
        who=t["who"], structure=t["structure"], check=CHECK,
    )
    for t in TRACKS
)
services = f"""
{crumbs([("Services",None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><h1>How organizations bring in program leadership.</h1><p class="lede">Every engagement is scoped to the problem in front of you — not a tier on a pricing menu.</p></div></section>
<section class="sec"><div class="wrap">
 {_svc_rows}
</div></section>
{ways_to_start_section()}
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
    cta_btns = f'<a class="btn btn-gold" href="{BOOKING}" data-track="svc_hero_cta">{t["cta"]}</a>'
    # Federal & Nonprofit: ungated capability statement (PDF path reserved; file not invented)
    if t["slug"] == "federal-nonprofit-delivery":
        cta_btns += (
            '<!-- Capability statement PDF: place file at assets/maizeway-capability-statement.pdf when ready -->'
            f'<a class="btn btn-line" href="assets/maizeway-capability-statement.pdf" data-track="capability_statement">Download capability statement</a>'
        )
    also = "".join(
        f'<a class="card link-card" href="{o["slug"]}.html"><h3>{o["h1"]}</h3><p>{o["short"]}</p>'
        f'<span class="more">Details {ARROW}</span></a>'
        for o in others
    )
    body = f"""
{crumbs([("Services","services.html"),(t["nav"],None)])}
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">Track 0{i+1}</p><h1>{t["h1"]}</h1><p class="lede">{t["tag"]}</p><div class="acts">{cta_btns}</div></div></section>
<section class="sec"><div class="wrap grid g2 po">
 <div><p class="kicker">Who needs this</p><p class="sub">{t["who"]}</p></div>
 <div><p class="kicker">Problems it solves</p><p class="sub">{t["problems"]}</p></div>
</div></section>
<section class="sec sec-stone"><div class="wrap">
 <div class="head"><div class="t"><h2>What I do.</h2><p class="sub">{t["does"]}</p></div></div>
 <div class="grid g2"><ul class="ticks card">{dl}</ul>
  <div class="card"><p class="kicker">Engagement structure</p><p class="sub">{t["structure"]}</p></div></div>
</div></section>
{track_packages_section(t)}
<section class="sec"><div class="wrap"><p class="kicker">Also</p><div class="grid g2">{also}</div></div></section>
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
<section class="hero hero-inner"><div class="ring r1" aria-hidden="true"></div><div class="wrap"><p class="kicker">Contact</p><h1>Let's talk about what's stuck.</h1><p class="lede">Send a few details and I'll respond within one business day. If it's urgent, call — {PHONE}.</p></div></section>
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
  <button class="btn btn-gold full" type="submit">Schedule a Consultation</button>
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
 ("index.html", f"{FIRM} | Fractional Program & Project Leadership", f"Fractional project and program management consulting for federal, nonprofit, and mission-driven organizations. {YEARS} years, PMP-certified, {CITY_AREA}.", "home", home, None, None),
 ("services.html", f"Services | {FIRM}", "Program and project leadership, project recovery, and federal and nonprofit delivery support — scoped to the problem, not a tiered package.", "services", services, None, [("Services",None)]),
 ("about.html", f"About {FOUNDER} | {FIRM}", f"{FOUNDER}, {TITLE}: {YEARS} years leading programs across federal, nonprofit, and consulting environments.", "about", about, [{"@type":"Person","@id":f"{SITE_URL}/#founder","name":FOUNDER,"jobTitle":TITLE,"worksFor":{"@id":f"{SITE_URL}/#org"},"url":f"{SITE_URL}/about.html","description":f"{FOUNDER} is the founder of {FIRM}, providing fractional program and project leadership for federal, nonprofit, and mission-driven organizations.","hasCredential":{"@type":"EducationalOccupationalCredential","name":"Project Management Professional (PMP)"},"address":{"@type":"PostalAddress","addressLocality":"Bowie","addressRegion":"MD","addressCountry":"US"}}], [("About",None)]),
 ("contact.html", f"Schedule a Consultation | {FIRM}", f"Tell {FOUNDER} what's stuck. A 30-minute consultation, a response within one business day, no pitch deck.", "contact", contact, None, [("Contact",None)]),
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
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nDisallow: /\n\n# Sitemap retained for launch readiness (disallowed until go-live)\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT,"favicon.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#111e32" stroke="#c5973a" stroke-width="2"/><text x="32" y="40" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="20" fill="#c5973a">MW</text></svg>')
print("built", len(urls)+3, "pages")
