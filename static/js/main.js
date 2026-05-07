// Auto-dismiss messages
document.querySelectorAll('.message').forEach(msg => {
  setTimeout(() => msg.remove(), 5000);
});

// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.style.display === 'flex';
    links.style.display = open ? 'none' : 'flex';
    links.style.flexDirection = 'column';
    links.style.position = 'fixed';
    links.style.top = '64px';
    links.style.left = '0';
    links.style.right = '0';
    links.style.background = '#0a0a0a';
    links.style.padding = '20px';
    links.style.borderBottom = '1px solid #222';
  });
}

// Card entrance animation on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      entry.target.style.animationDelay = `${i * 60}ms`;
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.project-card').forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(16px)';
  card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
  observer.observe(card);
});

document.addEventListener('animationend', (e) => {
  if (e.target.classList.contains('project-card')) return;
});

// Manual visible class trigger
document.querySelectorAll('.project-card').forEach((card, i) => {
  setTimeout(() => {
    card.style.opacity = '1';
    card.style.transform = 'translateY(0)';
  }, 100 + i * 80);
});
