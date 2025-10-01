#!/usr/bin/env python3
"""
Build script for Ironji website
Injects header and footer components into all HTML pages
"""

import os
import re
from pathlib import Path

def read_component(component_path):
    """Read a component file and return its content"""
    with open(component_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_header_html():
    """Get the complete header HTML with inline styles"""
    return '''    <!-- Navigation -->
    <header id="header">
        <div class="nav-container">
            <a href="/" class="logo">IRONJI</a>
            <nav>
                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="#services" class="nav-link">
                            Services
                            <span class="dropdown-arrow"></span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="#services" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
                                </span> Products Distribution
                            </a>
                            <a href="#services" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                                </span> Inter-warehouse Transport
                            </a>
                            <a href="#services" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m5.2-13.2l-4.2 4.2m-1 1l-4.2 4.2m13.2-5.2h-6m-6 0H1m13.2 5.2l-4.2-4.2m-1-1L4.8 4.8"/></svg>
                                </span> Custom Solutions
                            </a>
                            <a href="#schedule" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                                </span> Schedule & Prices
                            </a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="track.html" class="nav-link">Track Shipment</a>
                    </li>
                    <li class="nav-item">
                        <a href="quote.html" class="nav-link">Get Instant Quotation</a>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">
                            Company
                            <span class="dropdown-arrow"></span>
                        </a>
                        <div class="dropdown-menu">
                            <a href="about.html" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
                                </span> About Us
                            </a>
                            <a href="profile.html" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="9" y1="9" x2="15" y2="9"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="13" y2="17"/></svg>
                                </span> Company Profile
                            </a>
                            <a href="#news" class="dropdown-item">
                                <span class="dropdown-item-icon">
                                    <svg viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><line x1="12" y1="7" x2="17" y2="7"/><line x1="12" y1="11" x2="17" y2="11"/></svg>
                                </span> News & Insights
                            </a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="tel:+250784635871" class="nav-link">
                            <span class="dropdown-item-icon">
                                <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                            </span> Emergency
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#contact" class="nav-cta">Contact Us</a>
                    </li>
                </ul>
                <button class="menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </nav>
        </div>
    </header>'''

def get_footer_html():
    """Get the complete footer HTML"""
    return '''    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-brand">
                <h3>IRONJI</h3>
                <p>Revolutionizing logistics in Rwanda with innovative solutions,
                   unmatched reliability, and a commitment to excellence since 2018.</p>
            </div>
            <div class="footer-column">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="/about.html">About Us</a></li>
                    <li><a href="/track.html">Track Shipment</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Services</h4>
                <ul>
                    <li><a href="#">Distribution</a></li>
                    <li><a href="#">Warehousing</a></li>
                    <li><a href="#">On Demand Transport</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Contact</h4>
                <ul>
                    <li><a href="mailto:ironji.sales@gmail.com">ironji.sales@gmail.com</a></li>
                    <li><a href="tel:+250784635871">+250 784 635 871</a></li>
                    <li><a href="#">Kigali, Rwanda</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Ironji. All rights reserved.</p>
            <div class="social-links">
                <a href="#" class="social-link">f</a>
                <a href="#" class="social-link">𝕏</a>
                <a href="#" class="social-link">in</a>
            </div>
        </div>
    </footer>

    <!-- Mobile Click-to-Call Button -->
    <a href="tel:+250784635871" class="mobile-call-btn" title="Call Us Now">
        <svg viewBox="0 0 24 24" width="28" height="28" style="stroke: white; fill: none; stroke-width: 2;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    </a>'''

def process_html_file(file_path, header_html, footer_html):
    """Process a single HTML file to inject header and footer"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file already has the static header/footer
    if '<!-- Static Header Start -->' in content:
        print(f"  Skipping {file_path.name} (already has static components)")
        return False

    # Replace header placeholder
    header_pattern = r'<div id="header-placeholder">\s*</div>|<!-- Navigation -->\s*<div id="header-placeholder"></div>'
    if re.search(header_pattern, content):
        content = re.sub(
            header_pattern,
            f'<!-- Static Header Start -->\n{header_html}\n    <!-- Static Header End -->',
            content
        )
        print(f"  ✓ Replaced header placeholder in {file_path.name}")

    # Replace footer placeholder
    footer_pattern = r'<!-- Footer -->\s*<div id="footer-placeholder">\s*</div>'
    if re.search(footer_pattern, content):
        content = re.sub(
            footer_pattern,
            f'<!-- Static Footer Start -->\n{footer_html}\n    <!-- Static Footer End -->',
            content
        )
        print(f"  ✓ Replaced footer placeholder in {file_path.name}")

    # Remove component loader script as it's no longer needed
    loader_pattern = r'<!-- Component Loader -->.*?<script src="/js/components-loader\.js.*?"></script>'
    if re.search(loader_pattern, content, re.DOTALL):
        content = re.sub(loader_pattern, '', content, flags=re.DOTALL)
        print(f"  ✓ Removed component loader script from {file_path.name}")

    # Write the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Main function to process all HTML files"""
    print("Building Ironji website...")
    print("=" * 50)

    # Get the header and footer HTML
    header_html = get_header_html()
    footer_html = get_footer_html()

    # Find all HTML files in the root directory
    root_dir = Path('/Users/descholar/descholar/myprojects/ironji/jedi')
    html_files = list(root_dir.glob('*.html'))

    print(f"Found {len(html_files)} HTML files to process\n")

    processed_count = 0
    for html_file in html_files:
        print(f"Processing {html_file.name}...")
        if process_html_file(html_file, header_html, footer_html):
            processed_count += 1
        print()

    print("=" * 50)
    print(f"Build complete! Processed {processed_count} files.")
    print("\nTo update components in the future:")
    print("1. Edit the get_header_html() or get_footer_html() functions in this script")
    print("2. Run: python3 build.py")
    print("3. Commit and push to GitHub")

if __name__ == "__main__":
    main()