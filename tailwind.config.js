// Production Tailwind config, used by scripts/build.py to compile a purged
// stylesheet from the freshly-rendered out/**/*.html (replacing the
// Tailwind Play CDN <script> tag that the site used to ship in production —
// see build.py's compile_tailwind_css() for the full rationale). Mirrors
// tailwind.qa.config.js (same content glob, same defaults) — kept as a
// separate file so it's clear this one is the production build's config,
// not just a QA-screenshot helper.
module.exports = {
  content: ["./out/**/*.html"],
  theme: { extend: {} },
  plugins: [],
}
