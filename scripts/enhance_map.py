#!/usr/bin/env python3
"""
Rwanda Map Enhancement Script
Adds coverage indicators to the Rwanda districts map
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

# Input and output paths
input_image = "assets/Rwanda_Districts_Map.jpg"
output_image = "assets/Rwanda_Coverage_Map.png"

# Load the original map
img = Image.open(input_image)
width, height = img.size

# Create a copy to work with
enhanced = img.copy()

# Create a drawing context
draw = ImageDraw.Draw(enhanced, 'RGBA')

# Define colors
accent_color = (255, 127, 31, 255)  # Orange
accent_glow = (255, 127, 31, 100)   # Semi-transparent orange
white = (255, 255, 255, 255)
black = (0, 0, 0, 200)

# Add a dark overlay for better visibility
overlay = Image.new('RGBA', img.size, (15, 15, 35, 180))
enhanced = Image.alpha_composite(img.convert('RGBA'), overlay)
draw = ImageDraw.Draw(enhanced, 'RGBA')

# District positions (accurate centers based on Rwanda map analysis)
# These positions are scaled to the image dimensions
# Format: (x_percentage, y_percentage, "District Name")
districts = [
    # Northern Province (top of map)
    (0.38, 0.20, "Burera"),
    (0.58, 0.32, "Gicumbi"),
    (0.32, 0.32, "Gakenke"),
    (0.45, 0.30, "Musanze"),
    (0.48, 0.38, "Rulindo"),

    # Kigali Province (center)
    (0.48, 0.50, "Gasabo"),
    (0.52, 0.54, "Kicukiro"),
    (0.44, 0.52, "Nyarugenge"),

    # Eastern Province (right side)
    (0.68, 0.18, "Nyagatare"),
    (0.72, 0.32, "Gatsibo"),
    (0.78, 0.47, "Kayonza"),
    (0.68, 0.50, "Rwamagana"),
    (0.62, 0.62, "Bugesera"),
    (0.72, 0.62, "Ngoma"),
    (0.82, 0.66, "Kirehe"),

    # Southern Province (bottom center)
    (0.48, 0.62, "Kamonyi"),
    (0.42, 0.70, "Muhanga"),
    (0.42, 0.76, "Ruhango"),
    (0.48, 0.78, "Huye"),
    (0.38, 0.82, "Nyanza"),
    (0.45, 0.86, "Gisagara"),
    (0.32, 0.88, "Nyaruguru"),
    (0.38, 0.92, "Nyamagabe"),

    # Western Province (left side)
    (0.25, 0.34, "Rubavu"),
    (0.22, 0.42, "Nyabihu"),
    (0.28, 0.48, "Ngororero"),
    (0.22, 0.56, "Rutsiro"),
    (0.28, 0.62, "Karongi"),
    (0.18, 0.72, "Nyamasheke"),
    (0.15, 0.82, "Rusizi"),
]

# Try to load a font, fallback to default if not available
try:
    # Try different font paths
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, 16)
            label_font = ImageFont.truetype(font_path, 12)
            break
    if font is None:
        font = ImageFont.load_default()
        label_font = ImageFont.load_default()
except:
    font = ImageFont.load_default()
    label_font = ImageFont.load_default()

# Draw coverage indicators for each district
for x_pct, y_pct, district_name in districts:
    x = int(x_pct * width)
    y = int(y_pct * height)

    # Draw glow effect (multiple circles with decreasing opacity)
    for i in range(3, 0, -1):
        radius = 12 + (i * 3)
        opacity = int(20 - (i * 4))
        draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=(255, 127, 31, opacity)
        )

    # Draw main coverage circle
    radius = 12
    draw.ellipse(
        [x - radius, y - radius, x + radius, y + radius],
        fill=accent_glow,
        outline=accent_color,
        width=2
    )

    # Draw center dot
    center_radius = 3
    draw.ellipse(
        [x - center_radius, y - center_radius, x + center_radius, y + center_radius],
        fill=accent_color
    )

    # Draw district name with background for readability
    bbox = draw.textbbox((x, y + radius + 3), district_name, font=label_font)
    padding = 3
    draw.rectangle(
        [bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding],
        fill=black
    )
    draw.text(
        (x, y + radius + 3),
        district_name,
        fill=white,
        font=label_font,
        anchor="mt"
    )

# Add title
title = "IRONJI - COMPLETE RWANDA COVERAGE"
subtitle = "Serving All 30 Districts Across 5 Provinces"

# Title background
title_bbox = draw.textbbox((width // 2, 40), title, font=font)
draw.rectangle(
    [title_bbox[0] - 20, title_bbox[1] - 10, title_bbox[2] + 20, title_bbox[3] + 10],
    fill=black
)
draw.text((width // 2, 40), title, fill=accent_color, font=font, anchor="mt")

# Subtitle
subtitle_bbox = draw.textbbox((width // 2, 70), subtitle, font=label_font)
draw.rectangle(
    [subtitle_bbox[0] - 15, subtitle_bbox[1] - 8, subtitle_bbox[2] + 15, subtitle_bbox[3] + 8],
    fill=black
)
draw.text((width // 2, 70), subtitle, fill=white, font=label_font, anchor="mt")

# Add coverage stats box
stats_text = [
    "✓ 5 Provinces",
    "✓ 30 Districts",
    "✓ 100% Coverage"
]

stats_x = width - 200
stats_y = height - 150

# Stats background
draw.rectangle(
    [stats_x - 20, stats_y - 20, stats_x + 180, stats_y + 100],
    fill=(0, 0, 0, 200),
    outline=accent_color,
    width=3
)

for i, text in enumerate(stats_text):
    draw.text(
        (stats_x, stats_y + i * 35),
        text,
        fill=accent_color,
        font=font
    )

# Add corner accents
corner_size = 50
corner_width = 4

# Top-left corner
draw.line([(20, 20), (20 + corner_size, 20)], fill=accent_color, width=corner_width)
draw.line([(20, 20), (20, 20 + corner_size)], fill=accent_color, width=corner_width)

# Top-right corner
draw.line([(width - 20 - corner_size, 20), (width - 20, 20)], fill=accent_color, width=corner_width)
draw.line([(width - 20, 20), (width - 20, 20 + corner_size)], fill=accent_color, width=corner_width)

# Bottom-left corner
draw.line([(20, height - 20), (20 + corner_size, height - 20)], fill=accent_color, width=corner_width)
draw.line([(20, height - 20 - corner_size), (20, height - 20)], fill=accent_color, width=corner_width)

# Bottom-right corner
draw.line([(width - 20 - corner_size, height - 20), (width - 20, height - 20)], fill=accent_color, width=corner_width)
draw.line([(width - 20, height - 20 - corner_size), (width - 20, height - 20)], fill=accent_color, width=corner_width)

# Save the enhanced image
enhanced.save(output_image, 'PNG', quality=95)
print(f"✅ Enhanced map saved to: {output_image}")
print(f"📍 Added coverage indicators for all 30 districts")
print(f"🎨 Image size: {width}x{height}px")
