(() => {
  const header = document.querySelector('[data-header]');
  const menuButton = document.querySelector('.nav-trigger');
  const megaMenu = document.querySelector('.mega-menu');
  const mobileButton = document.querySelector('.mobile-toggle');
  const primaryNav = document.querySelector('.primary-nav');
  const mobile = window.matchMedia('(max-width: 800px)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  function setMega(open) {
    megaMenu.classList.toggle('open', open);
    megaMenu.inert = !open;
    megaMenu.setAttribute('aria-hidden', String(!open));
    menuButton.setAttribute('aria-expanded', String(open));
  }

  function setMobile(open, restoreFocus = false) {
    header.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-locked', open);
    mobileButton.setAttribute('aria-expanded', String(open));
    mobileButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    primaryNav.inert = mobile.matches && !open;
    if (!open) setMega(false);
    if (open) menuButton.focus();
    if (restoreFocus) mobileButton.focus();
  }

  menuButton.addEventListener('click', () => {
    setMega(menuButton.getAttribute('aria-expanded') !== 'true');
  });
  mobileButton.addEventListener('click', () => {
    setMobile(mobileButton.getAttribute('aria-expanded') !== 'true');
  });
  primaryNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => { setMega(false); setMobile(false); });
  });
  document.addEventListener('click', event => {
    if (!header.contains(event.target)) {
      setMega(false);
      if (mobile.matches) setMobile(false);
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (menuButton.getAttribute('aria-expanded') === 'true') {
        setMega(false);
        menuButton.focus();
      } else if (mobileButton.getAttribute('aria-expanded') === 'true') {
        setMobile(false, true);
      }
    }
    if (event.key !== 'Tab' || !mobile.matches || !header.classList.contains('is-open')) return;
    const focusable = [...header.querySelectorAll('a[href], button')].filter(element =>
      !element.closest('[inert]') && element.getClientRects().length && !element.disabled
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault(); first.focus();
    }
  });
  header.addEventListener('focusout', event => {
    if (event.relatedTarget && !header.contains(event.relatedTarget) && !mobile.matches) setMega(false);
  });
  mobile.addEventListener('change', () => setMobile(false));
  setMobile(false);

  const updateScroll = () => document.body.classList.toggle('has-scrolled', window.scrollY > 20);
  window.addEventListener('scroll', updateScroll, { passive: true });
  updateScroll();

  if (!reducedMotion.matches && 'IntersectionObserver' in window) {
    const sections = document.querySelectorAll('.home-reveal');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    sections.forEach(section => {
      if (section.getBoundingClientRect().top < window.innerHeight) section.classList.add('is-visible');
      observer.observe(section);
    });
    document.body.classList.add('motion-ready');
  }
})();
