(() => {
  const form = document.querySelector('[data-qualify-form]');
  if (!form) return;
  const steps = [...form.querySelectorAll('.wizard-step')];
  const back = form.querySelector('[data-wizard-back]');
  const next = form.querySelector('[data-wizard-next]');
  const submit = form.querySelector('[data-wizard-submit]');
  const counter = form.querySelector('[data-wizard-index]');
  const label = form.querySelector('[data-wizard-label]');
  const fill = form.querySelector('.wizard-fill');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  let autoStepTimer;

  function validStep(step) {
    for (const field of step.querySelectorAll('input, select, textarea')) {
      if (!field.checkValidity()) {
        field.reportValidity();
        return false;
      }
    }
    return true;
  }
  function showStep(newIndex, moveFocus = true) {
    clearTimeout(autoStepTimer);
    index = Math.max(0, Math.min(steps.length - 1, newIndex));
    steps.forEach((step, n) => {
      step.hidden = n !== index;
      step.classList.toggle('is-current', n === index);
    });
    counter.textContent = String(index + 1);
    label.textContent = steps[index].dataset.label;
    fill.style.width = `${((index + 1) / steps.length) * 100}%`;
    back.hidden = index === 0;
    next.hidden = index === steps.length - 1;
    submit.hidden = index !== steps.length - 1;
    if (moveFocus) {
      steps[index].querySelector('.wizard-q').focus({ preventScroll: true });
      if (form.getBoundingClientRect().top < 120) {
        form.scrollIntoView({ block: 'start', behavior: reducedMotion.matches ? 'instant' : 'smooth' });
      }
    }
  }
  function advance() {
    clearTimeout(autoStepTimer);
    if (validStep(steps[index])) showStep(index + 1);
  }
  next.addEventListener('click', advance);
  back.addEventListener('click', () => showStep(index - 1));
  form.addEventListener('change', event => {
    const step = event.target.closest('.wizard-step');
    if (!step?.hasAttribute('data-autostep') || event.target.type !== 'radio') return;
    clearTimeout(autoStepTimer);
    autoStepTimer = window.setTimeout(() => {
      if (steps[index] === step && validStep(step)) showStep(index + 1);
    }, 220);
  });
  form.addEventListener('keydown', event => {
    if (event.key !== 'Enter' || event.target.tagName === 'TEXTAREA' || event.target.tagName === 'BUTTON') return;
    if (index < steps.length - 1) {
      event.preventDefault();
      advance();
    }
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (index < steps.length - 1) { advance(); return; }
    for (let n = 0; n < steps.length; n++) {
      const invalid = [...steps[n].querySelectorAll('input, select, textarea')].some(field => !field.checkValidity());
      if (invalid) {
        showStep(n);
        validStep(steps[n]);
        return;
      }
    }
    const data = new FormData(form);
    const fields = [
      ['Nombre', 'nombre'], ['Teléfono', 'telefono'], ['Email', 'email'],
      ['Población', 'poblacion'], ['Espacio', 'espacio'], ['Superficie', 'superficie'],
      ['Horizonte', 'plazo'], ['Presupuesto', 'presupuesto'], ['Contacto preferido', 'contacto']
    ];
    const body = fields.map(([title, key]) => `${title}: ${String(data.get(key) || '').trim()}`);
    body.push('', String(data.get('mensaje') || '').trim());
    window.location.href = `mailto:toscal@toscalgarden.com?subject=${encodeURIComponent('Quiero crear mi jardín')}&body=${encodeURIComponent(body.join('\n'))}`;
  });
  showStep(0, false);
})();
