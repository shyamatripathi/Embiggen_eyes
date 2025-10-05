# CosmicZoom - Space Imagery Platform

**CosmicZoom** is a web-based platform that lets you explore **high-resolution space images** with smooth zooming and interactive annotations.  
Built for the **NASA Space Apps Challenge 2025**, it enables users to load any space image via URL, zoom into fine details, and annotate features directly on the image  all within a browser.

---

## Features

- **Zoom & Pan:** Smooth navigation of large images using **OpenSeadragon**
- **Annotations:** Click anywhere to add notes or mark discoveries
- **Export Data:** Save annotations as JSON for analysis or sharing
- **No Backend Needed:** Runs entirely in the browser using `localStorage`
- **Supports Any Image URL:** Works with NASA images, Hubble photos, Mars rover images, and more
- **Responsive Design:** Works seamlessly on desktop and tablet devices

---

##  Quick Start

1. **Download** all project files to a folder on your computer  
2. **Open terminal/command prompt** in that folder  
3. **Start a local server:**
   ```bash
   python -m http.server 8000
Open your browser and go to:

http://localhost:8000/fixed_viewer.html
Paste any image URL or try the example NASA images below

Example NASA Image URLs
Object	URL
Hubble Andromeda Galaxy	View Image
Mars Perseverance Rover	View Image
Earth from ISS	View Image

How to Use
Basic Navigation
Mouse wheel: Zoom in and out

Click and drag: Pan around the image

Navigator: Use the small preview in the bottom-right for quick navigation

Reset button: Return to the initial view

Adding Annotations
Click the “Enable Annotations” button

Click anywhere on the image to add a note

View and manage all annotations in the right panel

Export annotations as JSON using the “Export JSON” button

Keyboard Shortcuts
Key	Action
A	Toggle annotation mode
+ / -	Zoom in / out
0	Reset view
Space	Go to home position

Project Structure
bash
Copy code
├── cosmiczoom_with_annotations.html   # Main application
├── create_tiles.py                    # Image processing script
├── andromeda_local.jpg                # Sample space image
├── debug_test.html                    # Diagnostic tool
└── fixed_viewer.html                  # Alternative viewer
Technical Details
Frontend: HTML, CSS, JavaScript

Image Viewer: OpenSeadragon

Storage: Browser localStorage

Processing: Python with PIL/Pillow

AI Usage Disclosure
This project used AI assistance (ChatGPT/GPT-4) for code generation and documentation.
All code was reviewed and modified by the development team.
No AI-generated images or modified NASA branding were used.

NASA Space Apps Challenge 2025
Developed for the NASA Space Apps Challenge 2025 under the theme of exploring massive NASA image datasets.
CosmicZoom addresses the challenge of making trillion-pixel space imagery accessible and interactive for everyone.

License
This project is developed for educational and demonstration purposes as part of the NASA Space Apps Challenge.
All NASA imagery remains the property of NASA.
