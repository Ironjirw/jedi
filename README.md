# Ironji Website

A single-page marketing website for Ironji, Rwanda's premier logistics company since 2018.

## Getting Started

Since this is a static HTML site, simply open `index.html` in your browser.

To run a local development server:
```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Features

- **Responsive Design** - Mobile-first approach with breakpoints at 768px and 480px
- **Scroll Animations** - Fade-in effects triggered by Intersection Observer
- **Animated Counters** - Stats count up when scrolled into view
- **Smooth Scrolling** - Internal navigation with smooth scroll behavior
- **Dynamic Header** - Transparent header becomes solid on scroll

## Design System

### Colors
- Primary Accent: `#FF7F1F`
- Black: `#000000`
- Dark Gray: `#1C1C1C`
- White: `#FFFFFF`
- Off-White: `#F8F8F8`

### Typography
- Font Family: Avenir
- Weights: 300, 400, 600, 700

## Component Management

### Components Location
- **Header:** `components/header.html` (HTML only, no styles)
- **Footer:** `components/footer.html` (HTML only, no styles)

### How It Works
1. Components are maintained in separate files for easy editing
2. Build script injects them into all pages as static HTML
3. This ensures GitHub Pages can serve them without JavaScript

### To Update Header or Footer

1. **Edit the component file:**
   ```bash
   # Edit header
   nano components/header.html

   # Edit footer
   nano components/footer.html
   ```

2. **Run the update script:**
   ```bash
   python3 update-components.py
   ```
   This will update all pages with the new component HTML.

3. **Deploy to GitHub Pages:**
   ```bash
   git add .
   git commit -m "Update header/footer components"
   git push
   ```

## Scripts

### `build.py`
- Initial build script that converts pages from dynamic to static components
- Only needed if adding new pages with placeholders

### `update-components.py`
- Updates existing static components in all pages
- Run this after editing component files

## Page Structure

Each page has:
```html
<!-- Static Header Start -->
[Header HTML here]
<!-- Static Header End -->

[Page content]

<!-- Static Footer Start -->
[Footer HTML here]
<!-- Static Footer End -->
```

## Adding New Pages

1. Create your HTML file with proper structure
2. Add header/footer sections with the markers shown above
3. Copy header/footer HTML from another page or run `update-components.py`

## Important Notes

- **DO NOT** use JavaScript-based component loading for GitHub Pages
- **DO NOT** edit header/footer directly in individual pages
- **ALWAYS** edit components in the `/components` folder
- **ALWAYS** run `update-components.py` after editing components

## Deployment

### GitHub Pages
The site uses static HTML with embedded components for GitHub Pages compatibility. Since styles cannot be dynamically injected on GitHub Pages:
- Header styles should be in each page's `<head>` section
- Footer styles should be in each page's `<head>` section
- Common styles are duplicated across pages for reliability

### Troubleshooting

**Changes not showing on GitHub Pages:**
1. Clear browser cache (Cmd+Shift+R or Ctrl+Shift+R)
2. Wait 5-10 minutes for GitHub Pages to update
3. Check GitHub Actions tab for deployment status

**Components not updating:**
1. Ensure you're editing files in `/components` folder
2. Run `python3 update-components.py`
3. Check for "✓ Updated" messages in script output

## Testing

### For Testing the Track Page

**Tracking Numbers:**
- TRK-2024-001234
- TRK-2024-001235

**Batch Numbers:**
- BATCH-2024-056
