document.addEventListener('DOMContentLoaded', () => {
    // Dynamic Space Background
    const canvas = document.getElementById('space-bg');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const particleCount = 100;

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 5 + 1;
            this.speedX = Math.random() * 0.5 - 0.25;
            this.speedY = Math.random() * 0.5 - 0.25;
            this.type = Math.random() > 0.8 ? 'planet' : 'star';
            this.color = this.type === 'planet' ? '#ff00ff' : '#00ffcc';
        }

        draw() {
            ctx.beginPath();
            if (this.type === 'planet') {
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color;
            } else {
                ctx.fillStyle = this.color;
                ctx.fillRect(this.x, this.y, this.size, this.size);
                ctx.shadowBlur = 5;
                ctx.shadowColor = this.color;
            }
            ctx.fill();
            ctx.closePath();
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x > canvas.width) this.x = 0;
            else if (this.x < 0) this.x = canvas.width;
            if (this.y > canvas.height) this.y = 0;
            else if (this.y < 0) this.y = canvas.height;

            this.draw();
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(particle => particle.update());
        requestAnimationFrame(animate);
    }

    animate();

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    // Mouse Interaction with Background
    canvas.addEventListener('mousemove', (e) => {
        particles.forEach(particle => {
            const dx = e.x - particle.x;
            const dy = e.y - particle.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 100) {
                particle.x += dx * 0.05;
                particle.y += dy * 0.05;
            }
        });
    });

    // Creator Interaction
    const creatorText = document.querySelector('.creator-text');
    creatorText.addEventListener('mouseenter', () => {
        particles.forEach(particle => {
            particle.speedX *= 2;
            particle.speedY *= 2;
            setTimeout(() => {
                particle.speedX /= 2;
                particle.speedY /= 2;
            }, 500);
        });
    });

    // Form Interactions
    const form = document.querySelector('.form');
    const textarea = document.querySelector('.textarea');
    const submitBtn = document.querySelector('.submit-btn');

    form.addEventListener('submit', () => {
        submitBtn.style.transform = 'scale(1.2) rotate(5deg)';
        setTimeout(() => submitBtn.style.transform = 'scale(1) rotate(0deg)', 300);
    });

    textarea.addEventListener('input', () => {
        textarea.style.height = 'auto';
        textarea.style.height = `${textarea.scrollHeight}px`;
    });

    const radioLabels = document.querySelectorAll('.radio-label');
    radioLabels.forEach(label => {
        label.addEventListener('mouseover', () => {
            label.style.boxShadow = '0 0 20px #ff00ff';
        });
        label.addEventListener('mouseout', () => {
            if (!label.previousElementSibling.checked) {
                label.style.boxShadow = 'none';
            }
        });
    });
});