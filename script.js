// Intentionally minimal: the hero trace animation is pure CSS (see style.css).
// This only handles the current-section highlight in the top nav.
const links = document.querySelectorAll('.topnav a');
const sections = [...links].map(l => document.querySelector(l.getAttribute('href')));

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = '#' + entry.target.id;
      links.forEach(l => l.style.color = l.getAttribute('href') === id ? 'var(--text)' : '');
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => s && observer.observe(s));
