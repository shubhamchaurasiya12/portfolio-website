# ⚡ Data Scientist Portfolio

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Sphinx_Design-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)

A high-performance, design-forward portfolio website built to showcase Data Science projects. 

This project moves away from generic templates, utilizing a **custom-built design system** inspired by *Sphinx HQ*. It features fluid canvas animations, bento-grid layouts, and a clean, technical typography system (Inter + JetBrains Mono) to reflect a "fintech/data" aesthetic.

---

## 🎨 Design Philosophy

The UI was re-engineered from scratch to prioritize readability and motion without sacrificing performance.

* **Fluid Wave Engine:** A custom HTML5 Canvas script (`script.js`) generates a mathematically procedural wave background that mimics 3D liquid motion, replacing heavy video backgrounds.
* **Bento Grid Layout:** Projects are displayed in a responsive CSS Grid that adapts from a strict 12-column layout on desktop to a single column on mobile.
* **Glassmorphism & Noise:** Elements use `backdrop-filter: blur()` and a custom SVG noise overlay to create a tactile, "premium paper" texture.
* **Micro-Interactions:** * Infinite scrolling marquee for skills.
    * Scroll-triggered reveals using `IntersectionObserver`.
    * Magnetic hover effects on cards and buttons.

## 🛠️ Tech Stack

### Backend
* **Python (Flask):** Serves dynamic routes, handles form submissions, and renders Jinja2 templates.
* **Jinja2:** Used for component reusability (navbars, footers) and dynamic project rendering.

### Frontend
* **HTML5 / CSS3:** Custom CSS variables for theming (Cream/Charcoal palette).
* **JavaScript (ES6+):** Handles the Canvas animation, mobile navigation, and scroll observers.
* **Devicon:** Lightweight vector icons for the tech stack.

---

## 🚀 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/shubhamchaurasiya12/portfolio-v2.git](https://github.com/shubhamchaurasiya12/portfolio-v2.git)
    cd portfolio-v2
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install Flask
    ```

4.  **Run the Application**
    ```bash
    flask run
    ```
    Visit `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```text
/portfolio
├── app.py                 # Main Flask application logic
├── static/
│   ├── css/
│   │   └── style.css      # Sphinx-inspired design system
│   ├── js/
│   │   └── script.js      # Canvas animation & UI logic
│   └── images/            # Project thumbnails & icons
├── templates/
│   ├── index.html         # Homepage (Landing, Grid, Skills)
│   └── project_detail.html # Dynamic Case Study template
└── README.md
```
# 📬 Contact
Portfolio: https://shubham-portfolio-ftzo.onrender.com/
LinkedIn: https://www.linkedin.com/in/chrsshubh/
Email: xshubhamchaurasiya@gmail.com
