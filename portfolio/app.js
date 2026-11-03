const profile = window.PORTFOLIO;
const setText = (selector, value) => document.querySelectorAll(selector).forEach(el => el.textContent = value);
setText('[data-name]', profile.displayName);
setText('[data-full-name]', `${profile.fullName} · AI Engineering Portfolio`);
setText('[data-grad-year]', profile.graduationYear);
setText('[data-intern-dates]', profile.internship.dates);
setText('[data-intern-title]', profile.internship.title);
setText('[data-intern-company]', profile.internship.company);
setText('[data-intern-description]', profile.internship.description);
if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(profile.email)) {
  const link = document.querySelector('[data-email-link]');
  link.href = `mailto:${profile.email}`;
  link.hidden = false;
  document.querySelector('[data-email-placeholder]').hidden = true;
}
if (/^https:\/\//.test(profile.licensePlateRepository)) {
  const link = document.querySelector('[data-project-link]');
  link.href = profile.licensePlateRepository;
  link.hidden = false;
}
const menu = document.querySelector('.menu');
const nav = document.querySelector('nav');
function closeMenu() { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }
menu.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });

