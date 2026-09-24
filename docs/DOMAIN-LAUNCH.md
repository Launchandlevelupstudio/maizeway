# Domain launch checklist

Canonical, Open Graph, JSON-LD, sitemap `<loc>`, and the contact form `_next` URL use `https://maizewaystrategy.com`.

Pre-launch SEO stays locked: sitewide `noindex, nofollow` and `robots.txt` `Disallow: /` remain until a later indexing go-live.

## Files / tags to update

| Location | What to change |
|---|---|
| `build.py` → `SITE_URL` | `https://maizewaystrategy.com` (no trailing slash) |
| `build.py` → `EMAIL` / `FORM_EMAIL` | Real mailbox once DNS/email exist |
| `build.py` → `LINKEDIN` | Real profile URL (footer link appears automatically) |
| All generated HTML | `link[rel=canonical]`, `og:url`, `og:image`, `twitter:image` |
| JSON-LD (`application/ld+json`) | `ProfessionalService` / `Person` / `WebSite` / `Service` absolute URLs |
| `sitemap.xml` | All `<loc>` values |
| `robots.txt` | `Sitemap:` URL; switch from `Disallow: /` to allow indexing |
| Contact form `_next` | Thank-you absolute URL |
| Pre-launch SEO | Remove sitewide `<meta name="robots" content="noindex, nofollow">` in `build.py` `page()` |
| Analytics stubs in `<head>` | GA4 `G-XXXXXXXX`, Search Console verification meta, Clarity `YOUR_CLARITY_ID` |
| Capability statement | Drop PDF at `assets/maizeway-capability-statement.pdf` |

## Rebuild

```bash
python3 build.py
```

Then commit the regenerated HTML (CSS/JS are inlined from `site.css` / `site.js`).
