# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Ironji website - a single-page marketing website for Rwanda's logistics company. The site is built as a static HTML file with inline CSS and JavaScript.

**Company Info:**
- Ironji: Rwanda's Premier Logistics Partner since 2014
- Services: Distribution Network, Warehouse Transport, Express Delivery
- Contact: ironji.sales@gmail.com, +250 784 635 871

## Development

Since this is a static HTML site, no build process is required. Simply open `index.html` in a browser to view the site.

To run a local development server:
```bash
python3 -m http.server 8000
# or
python -m SimpleHTTPServer 8000  # Python 2
```

Then visit http://localhost:8000

## Architecture

**Single-File Structure:**
- The entire website is contained in `index.html` with inline styles and scripts
- Uses modern CSS features: CSS custom properties (variables), Grid, Flexbox
- Vanilla JavaScript for interactions (no frameworks)

**Design System:**
- Color palette defined in CSS variables:
  - `--accent: #FF7F1F` (Primary orange)
  - `--black: #000000`, `--dark-gray: #1C1C1C`
  - `--white: #FFFFFF`, `--off-white: #F8F8F8`
- Typography: Poppins font family (Google Fonts)
- Responsive breakpoints: 768px (tablet), 480px (mobile)

**Key Sections:**
1. **Hero** (lines 197-753): Full-viewport hero with gradient background, animated text, CTA buttons
2. **Stats** (lines 345-775): Animated counter displaying company metrics
3. **Services** (lines 380-816): Card-based service showcase
4. **CTA** (lines 494-828): Call-to-action section with gradient background
5. **Footer** (lines 552-873): Multi-column footer with links and social icons

**JavaScript Features:**
- Header scroll effect (line 876-884): Adds transparency/blur to header on scroll
- Smooth scroll anchors (line 886-898): Smooth scrolling for internal navigation
- Intersection Observer animations (line 900-916): Fade-in effects on scroll
- Animated counters (line 918-946): Numbers count up when scrolled into view

## Design Patterns

**Animations:**
- CSS keyframe animations: `fadeInUp`, `drift`, `bounce`, `rotate`
- Intersection Observer API for scroll-triggered animations
- Transition-based hover effects throughout

**Responsive Design:**
- Mobile-first approach with progressive enhancement
- Grid layouts with `auto-fit` for fluid responsiveness
- Hidden mobile menu toggle (not fully implemented in current version)

## Common Modifications

When editing this site:
- **Colors:** Modify CSS custom properties in `:root` (lines 19-29)
- **Content:** Update text directly in HTML sections
- **Sections:** Each major section has its own class (`.hero`, `.stats`, `.services`, etc.)
- **Animations:** Controlled by `.fade-in` class and Intersection Observer (lines 900-916)
- **Stats:** Update numbers in `.stat-number` divs (lines 759-772)

## Notes

- The mobile menu toggle button exists but functionality is not implemented
- Social link placeholders use single-character representations ('f', '𝕏', 'in')
- Navigation links reference anchor IDs that may not all exist (#about, #track, #contact, #quote)
- Design follows modern trends: minimalism, bold typography, generous whitespace, subtle animations