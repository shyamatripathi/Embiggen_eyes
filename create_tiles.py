import os
import math
from PIL import Image
import urllib.request
import xml.etree.ElementTree as ET

def download_image():
    """Download the image"""
    url = "https://cdn.esahubble.org/archives/images/screen/heic1502a.jpg"
    filename = "andromeda_local.jpg"
    
    if not os.path.exists(filename):
        print("Downloading image...")
        urllib.request.urlretrieve(url, filename)
        print("Download complete!")
    else:
        print("Image already exists")
    
    return filename

def create_dzi_tiles(image_path, output_name="andromeda", tile_size=256, overlap=0):
    """Create proper DZI tiles and folder structure"""
    
    # Open image
    img = Image.open(image_path)
    width, height = img.size
    print(f"Image size: {width}x{height}")
    
    # Calculate pyramid levels
    max_level = 0
    level_width, level_height = width, height
    while level_width > 1 or level_height > 1:
        max_level += 1
        level_width = math.ceil(level_width / 2)
        level_height = math.ceil(level_height / 2)
    
    print(f"Creating {max_level + 1} pyramid levels...")
    
    # Create DZI folder
    dzi_folder = f"{output_name}_files"
    os.makedirs(dzi_folder, exist_ok=True)
    
    # Create tiles for each level
    current_img = img
    for level in range(max_level + 1):
        level_dir = os.path.join(dzi_folder, str(level))
        os.makedirs(level_dir, exist_ok=True)
        
        level_width, level_height = current_img.size
        cols = math.ceil(level_width / tile_size)
        rows = math.ceil(level_height / tile_size)
        
        print(f"Level {level}: {level_width}x{level_height} -> {cols}x{rows} tiles")
        
        # Create tiles for this level
        for row in range(rows):
            for col in range(cols):
                left = col * tile_size
                upper = row * tile_size
                right = min(left + tile_size, level_width)
                lower = min(upper + tile_size, level_height)
                
                # Crop tile
                tile = current_img.crop((left, upper, right, lower))
                
                # Save tile
                tile_filename = os.path.join(level_dir, f"{col}_{row}.jpg")
                tile.save(tile_filename, "JPEG", quality=85)
        
        # Resize image for next level (half size)
        if level < max_level:
            new_width = max(1, level_width // 2)
            new_height = max(1, level_height // 2)
            current_img = current_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Create DZI XML file
    create_dzi_xml(output_name, width, height, tile_size, overlap, max_level + 1)
    
    print(f"DZI creation complete! Files in '{dzi_folder}'")

def create_dzi_xml(output_name, width, height, tile_size, overlap, levels):
    """Create the DZI XML descriptor"""
    dzi_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<Image xmlns="http://schemas.microsoft.com/deepzoom/2008"
       Format="jpg"
       Overlap="{overlap}"
       TileSize="{tile_size}">
    <Size Width="{width}" Height="{height}"/>
</Image>'''
    
    with open(f"{output_name}.dzi", "w") as f:
        f.write(dzi_content)
    
    print(f"DZI XML created: {output_name}.dzi")

def create_simple_viewer():
    """Create a simple viewer that will definitely work"""
    html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>CosmicZoom - Simple Test</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>
    <style>
        body { margin: 0; padding: 20px; background: #1a1a2e; color: white; }
        #viewer { width: 100%; height: 80vh; border: 2px solid #0f3460; }
    </style>
</head>
<body>
    <h1>CosmicZoom Test</h1>
    <p>If you can see the image below, it's working!</p>
    
    <div id="viewer"></div>
    
    <script>
        // Try multiple approaches to load the image
        try {
            const viewer = OpenSeadragon({
                id: "viewer",
                prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
                tileSources: {
                    type: 'image',
                    url: 'andromeda_local.jpg'
                },
                showNavigator: true,
                showRotationControl: true
            });
            
            viewer.addHandler('open', function() {
                console.log("SUCCESS: Image loaded!");
                document.body.innerHTML += '<p style="color: green;"> SUCCESS: Image loaded properly!</p>';
            });
            
            viewer.addHandler('tile-load-failed', function(event) {
                console.log("Tile load failed:", event);
                document.body.innerHTML += '<p style="color: red;"> Tile loading failed</p>';
            });
            
        } catch (error) {
            console.error("Error:", error);
            document.body.innerHTML += '<p style="color: red;"> Error: ' + error.message + '</p>';
        }
    </script>
</body>
</html>
'''
    with open("simple_test.html", "w") as f:
        f.write(html_content)
    print("Simple test viewer created: simple_test.html")

if __name__ == "__main__":
    # Download image
    image_path = download_image()
    
    # Create proper DZI tiles
    create_dzi_tiles(image_path)
    
    # Create a simple test viewer
    create_simple_viewer()
    
    print(" Done!")
    print("python -m http.server 8000")
