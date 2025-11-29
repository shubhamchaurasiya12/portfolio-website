// =========================================
// 1. FLUID WAVE ANIMATION (Sphinx Style)
// =========================================
const canvas = document.getElementById('hero-canvas');

if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height;
    let time = 0;

    // Colors: Off-white background to light cyan/blue
    const colorPalette = {
        c1: {r: 117, g: 226, b: 245},
        c2: {r: 253, g: 253, b: 245}
    };

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);
        time += 0.002;

        const gradient = ctx.createLinearGradient(0, 0, width, height);
        gradient.addColorStop(0, `rgba(${colorPalette.c2.r}, ${colorPalette.c2.g}, ${colorPalette.c2.b}, 0)`);
        gradient.addColorStop(0.5, `rgba(${colorPalette.c1.r}, ${colorPalette.c1.g}, ${colorPalette.c1.b}, 0.15)`);
        gradient.addColorStop(1, `rgba(${colorPalette.c1.r}, ${colorPalette.c1.g}, ${colorPalette.c1.b}, 0.3)`);

        ctx.fillStyle = gradient;
        
        // Draw Wave
        ctx.beginPath();
        for (let i = 0; i <= width; i += 10) {
            const y = height / 2 + 
                      Math.sin(i * 0.003 + time) * 80 + 
                      Math.sin(i * 0.01 + time * 2) * 40;
            ctx.lineTo(i, y);
        }
        ctx.lineTo(width, height);
        ctx.lineTo(0, height);
        ctx.closePath();
        ctx.fill();

        requestAnimationFrame(animate);
    }

    window.addEventListener('resize', resize);
    resize();
    animate();
}

// =========================================
// 2. MOBILE MENU LOGIC
// =========================================
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

function toggleMenu() {
    mobileMenu.classList.toggle('active');
    // Animate burger lines (optional simple rotation or color change could go here)
}

if (menuBtn) {
    menuBtn.addEventListener('click', toggleMenu);
}

// =========================================
// 3. SCROLL REVEAL ANIMATIONS
// =========================================
// This detects when elements enter the viewport and adds the 'active' class
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => {
    observer.observe(el);
});