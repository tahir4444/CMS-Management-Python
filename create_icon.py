#!/usr/bin/env python3
"""
Icon Creator Script
Creates a custom icon for the Customer Management System
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    """Create a custom icon for the application"""
    try:
        # Create a 256x256 image with a professional look
        size = 256
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Create a modern circular background
        margin = 20
        circle_bbox = (margin, margin, size - margin, size - margin)
        
        # Gradient-like effect with multiple circles
        colors = [
            (52, 152, 219, 255),  # Blue
            (41, 128, 185, 200),  # Darker blue
            (26, 188, 156, 150),  # Teal
        ]
        
        for i, color in enumerate(colors):
            offset = i * 10
            bbox = (margin + offset, margin + offset, 
                   size - margin - offset, size - margin - offset)
            draw.ellipse(bbox, fill=color)
        
        # Add a white circle in the center
        center_margin = 60
        center_bbox = (center_margin, center_margin, 
                      size - center_margin, size - center_margin)
        draw.ellipse(center_bbox, fill=(255, 255, 255, 255))
        
        # Add text "CMS" (Customer Management System)
        try:
            # Try to use a system font
            font_size = 80
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Calculate text position to center it
        text = "CMS"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size - text_width) // 2
        y = (size - text_height) // 2 - 10  # Slightly up for visual balance
        
        # Draw text with shadow effect
        draw.text((x + 2, y + 2), text, fill=(0, 0, 0, 100), font=font)  # Shadow
        draw.text((x, y), text, fill=(52, 152, 219, 255), font=font)  # Main text
        
        # Add a small user icon below the text
        user_y = y + text_height + 20
        user_size = 30
        
        # Draw a simple user icon (head and body)
        head_center = (size // 2, user_y)
        head_radius = user_size // 3
        
        # Head
        head_bbox = (head_center[0] - head_radius, head_center[1] - head_radius,
                    head_center[0] + head_radius, head_center[1] + head_radius)
        draw.ellipse(head_bbox, fill=(52, 152, 219, 255))
        
        # Body (simple rectangle)
        body_width = user_size // 2
        body_height = user_size // 2
        body_x = head_center[0] - body_width // 2
        body_y = head_center[1] + head_radius
        draw.rectangle([body_x, body_y, body_x + body_width, body_y + body_height], 
                      fill=(52, 152, 219, 255))
        
        # Save as ICO file with multiple sizes for better compatibility
        icon_path = "app_icon.ico"
        img.save(icon_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
        
        # Also create a PNG version for better tkinter compatibility
        png_path = "app_icon.png"
        img.save(png_path, format='PNG')
        
        # Create a smaller PNG version specifically for taskbar (32x32)
        small_img = img.resize((32, 32), Image.Resampling.LANCZOS)
        small_png_path = "app_icon_small.png"
        small_img.save(small_png_path, format='PNG')
        
        print(f"✅ Custom icon created: {icon_path}")
        print(f"✅ PNG version created: {png_path}")
        print(f"✅ Small PNG version created: {small_png_path}")
        return icon_path
        
    except Exception as e:
        print(f"❌ Error creating icon: {str(e)}")
        return None

def create_simple_icon():
    """Create a simpler icon if PIL is not available"""
    try:
        # Create a simple colored square as fallback
        size = 64
        img = Image.new('RGB', (size, size), (52, 152, 219))
        draw = ImageDraw.Draw(img)
        
        # Add a simple "C" letter
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()
        
        text = "C"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size - text_width) // 2
        y = (size - text_height) // 2
        
        draw.text((x, y), text, fill=(255, 255, 255), font=font)
        
        # Save as ICO file
        icon_path = "app_icon.ico"
        img.save(icon_path, format='ICO')
        
        print(f"✅ Simple icon created: {icon_path}")
        return icon_path
        
    except Exception as e:
        print(f"❌ Error creating simple icon: {str(e)}")
        return None

if __name__ == "__main__":
    print("Creating custom icon for Customer Management System...")
    
    # Try to create the full icon first
    icon_path = create_app_icon()
    
    if not icon_path:
        print("Falling back to simple icon...")
        icon_path = create_simple_icon()
    
    if icon_path:
        print(f"\n🎉 Icon created successfully!")
        print(f"📁 File: {icon_path}")
        print(f"📏 Size: 256x256 pixels")
        print(f"🎨 Colors: Professional blue theme")
        print(f"💡 Next: Update main.py to use this icon")
    else:
        print("❌ Failed to create icon. Using default icon.")
