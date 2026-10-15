(() => {
  const form = document.querySelector('[data-demo-form]');
  form?.addEventListener('submit', event => {
    event.preventDefault();
    form.querySelector('[role="status"]').textContent = 'Campos completos. Este ejemplo no envía datos.';
  });
})();
