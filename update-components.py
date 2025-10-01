#!/usr/bin/env python3
"""
Update script for Ironji website components
Updates the header and footer in all HTML pages with the latest versions
"""

import os
import re
from pathlib import Path

def read_component(component_path):
    """Read a component file and return its content"""
    if not os.path.exists(component_path):
        return None
    with open(component_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove any <style> tags from component files
    content = re.sub(r'<style>.*?</style>\s*', '', content, flags=re.DOTALL)
    return content.strip()

def update_html_file(file_path):
    """Update header and footer in a single HTML file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has static components
    if '<!-- Static Header Start -->' not in content:
        print(f"  Skipping {file_path.name} (no static components found)")
        return False

    # Read the latest components
    header_content = read_component('components/header.html')
    footer_content = read_component('components/footer.html')

    if not header_content or not footer_content:
        print("  Error: Could not read component files")
        return False

    # Update header
    header_pattern = r'<!-- Static Header Start -->.*?<!-- Static Header End -->'
    if re.search(header_pattern, content, re.DOTALL):
        # Ensure proper indentation
        header_html = '\n'.join(['    ' + line if line else '' for line in header_content.split('\n')])
        content = re.sub(
            header_pattern,
            f'<!-- Static Header Start -->\n{header_html}\n    <!-- Static Header End -->',
            content,
            flags=re.DOTALL
        )
        print(f"  ✓ Updated header in {file_path.name}")

    # Update footer
    footer_pattern = r'<!-- Static Footer Start -->.*?<!-- Static Footer End -->'
    if re.search(footer_pattern, content, re.DOTALL):
        # Ensure proper indentation
        footer_html = '\n'.join(['    ' + line if line else '' for line in footer_content.split('\n')])
        content = re.sub(
            footer_pattern,
            f'<!-- Static Footer Start -->\n{footer_html}\n    <!-- Static Footer End -->',
            content,
            flags=re.DOTALL
        )
        print(f"  ✓ Updated footer in {file_path.name}")

    # Write the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Main function to update all HTML files"""
    print("Updating Ironji website components...")
    print("=" * 50)

    # Check if component files exist
    if not os.path.exists('components/header.html'):
        print("Error: components/header.html not found!")
        return
    if not os.path.exists('components/footer.html'):
        print("Error: components/footer.html not found!")
        return

    print("Reading components from:")
    print("  - components/header.html")
    print("  - components/footer.html")
    print()

    # Find all HTML files in the root directory
    root_dir = Path('.')
    html_files = list(root_dir.glob('*.html'))

    print(f"Found {len(html_files)} HTML files to check\n")

    updated_count = 0
    for html_file in html_files:
        print(f"Processing {html_file.name}...")
        if update_html_file(html_file):
            updated_count += 1
        print()

    print("=" * 50)
    print(f"Update complete! Updated {updated_count} files.")
    print("\nHow to use this script:")
    print("1. Edit components/header.html or components/footer.html")
    print("2. Run: python3 update-components.py")
    print("3. All pages will be updated with the new components")
    print("4. Commit and push to GitHub")

if __name__ == "__main__":
    main()