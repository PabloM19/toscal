document.documentElement.classList.add("js");

const header = document.querySelector("[data-header]");
const menuTrigger = document.querySelector(".nav-trigger");
const megaMenu = document.querySelector(".mega-menu");
const languageToggle = document.querySelector(".language-toggle");
const languageMenu = document.querySelector(".language-menu");
const mobileTrigger = document.querySelector(".mobile-toggle");
const primaryNav = document.querySelector(".primary-nav");
const langCode = document.querySelector(".lang-code");

function setExpanded(el, open) {
  if (!el) return;
  el.setAttribute("aria-expanded", String(open));
}

function setMegaOpen(open) {
  megaMenu?.classList.toggle("open", open);
  megaMenu?.setAttribute("aria-hidden", String(!open));
  setExpanded(menuTrigger, open);
}

function setLanguageOpen(open) {
  languageMenu?.classList.toggle("open", open);
  setExpanded(languageToggle, open);
}

function setMobileOpen(open) {
  header?.classList.toggle("is-open", open);
  primaryNav?.classList.toggle("mobile-open", open);
  setExpanded(mobileTrigger, open);
  document.body.classList.toggle("nav-locked", open);
  if (!open) setMegaOpen(false);
}

function closeMenus() {
  setMegaOpen(false);
  setLanguageOpen(false);
}

menuTrigger?.addEventListener("click", (event) => {
  event.stopPropagation();
  const open = !megaMenu?.classList.contains("open");
  setLanguageOpen(false);
  setMegaOpen(open);
});

languageToggle?.addEventListener("click", (event) => {
  event.stopPropagation();
  const open = !languageMenu?.classList.contains("open");
  setMegaOpen(false);
  setLanguageOpen(open);
});

mobileTrigger?.addEventListener("click", (event) => {
  event.stopPropagation();
  const open = !header?.classList.contains("is-open");
  setLanguageOpen(false);
  setMobileOpen(open);
});

primaryNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    setMobileOpen(false);
    closeMenus();
  });
});

languageMenu?.querySelectorAll("button").forEach((button) => {
  button.addEventListener("click", () => {
    const code = (button.dataset.lang || "es").toUpperCase();
    document.documentElement.lang = button.dataset.lang;
    if (langCode) langCode.textContent = code;
    languageMenu.querySelectorAll("button").forEach((item) => {
      item.classList.toggle("is-current", item === button);
    });
    closeMenus();
  });
});

document.addEventListener("click", (event) => {
  if (!event.target.closest(".site-header")) {
    closeMenus();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  closeMenus();
  setMobileOpen(false);
});

window.addEventListener(
  "scroll",
  () => {
    document.body.classList.toggle("has-scrolled", window.scrollY > 20);
  },
  { passive: true }
);

const motionOk = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (motionOk && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -40px 0px" }
  );
  document.querySelectorAll(".reveal").forEach((node) => observer.observe(node));
} else {
  document.querySelectorAll(".reveal").forEach((node) => node.classList.add("is-visible"));
}

const qualifyForm = document.querySelector("[data-qualify-form]");

function initWizard(form) {
  const steps = [...form.querySelectorAll(".wizard-step")];
  if (!steps.length) return;
  let index = 0;
  const fill = form.querySelector(".wizard-fill");
  const counter = form.querySelector("[data-wizard-index]");
  const label = form.querySelector("[data-wizard-label]");
  const back = form.querySelector("[data-wizard-back]");
  const next = form.querySelector("[data-wizard-next]");
  const submit = form.querySelector("[data-wizard-submit]");

  function show(i) {
    index = i;
    steps.forEach((step, n) => {
      const current = n === i;
      step.classList.toggle("is-current", current);
      step.hidden = !current;
    });
    if (fill) fill.style.width = `${((i + 1) / steps.length) * 100}%`;
    if (counter) counter.textContent = String(i + 1);
    if (label) label.textContent = steps[i].dataset.label || "";
    if (back) back.hidden = i === 0;
    if (next) next.hidden = i === steps.length - 1;
    if (submit) submit.hidden = i !== steps.length - 1;
    steps[i].querySelector(".wizard-q")?.focus({ preventScroll: true });
  }

  function valid() {
    const fields = [...steps[index].querySelectorAll("input, select, textarea")];
    for (const field of fields) {
      if (!field.checkValidity()) {
        field.reportValidity();
        return false;
      }
    }
    return true;
  }

  next?.addEventListener("click", () => {
    if (!valid()) return;
    show(Math.min(index + 1, steps.length - 1));
  });
  back?.addEventListener("click", () => show(Math.max(index - 1, 0)));

  form.addEventListener("change", (event) => {
    const choice = event.target.closest(".choice");
    if (choice && event.target.type === "radio") {
      form.querySelectorAll(`input[name="${event.target.name}"]`).forEach((input) => {
        input.closest(".choice")?.classList.toggle("is-picked", input.checked);
      });
    }
    const step = event.target.closest(".wizard-step");
    if (!step?.hasAttribute("data-autostep")) return;
    if (!valid()) return;
    window.setTimeout(() => {
      if (steps[index] === step) show(index + 1);
    }, 260);
  });

  form.addEventListener("keydown", (event) => {
    if (event.key !== "Enter") return;
    if (event.target.tagName === "TEXTAREA") return;
    if (index >= steps.length - 1) return;
    event.preventDefault();
    next?.click();
  });

  show(0);
}

if (qualifyForm?.hasAttribute("data-wizard")) {
  initWizard(qualifyForm);
}

qualifyForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(qualifyForm);
  const name = String(data.get("nombre") || "").trim();
  const phone = String(data.get("telefono") || "").trim();
  const email = String(data.get("email") || "").trim();
  const town = String(data.get("poblacion") || "").trim();
  const space = String(data.get("espacio") || "").trim();
  const size = String(data.get("superficie") || "").trim();
  const timing = String(data.get("plazo") || "").trim();
  const budget = String(data.get("presupuesto") || "").trim();
  const contact = String(data.get("contacto") || "").trim();
  const message = String(data.get("mensaje") || "").trim();
  const body = [
    `Nombre: ${name}`,
    `Teléfono: ${phone}`,
    `Email: ${email}`,
    `Población: ${town}`,
    `Espacio: ${space}`,
    `Superficie: ${size}`,
    `Horizonte: ${timing}`,
    `Presupuesto: ${budget}`,
    `Contacto preferido: ${contact}`,
    "",
    message,
  ].join("\n");
  const mailto = `mailto:toscal@toscalgarden.com?subject=${encodeURIComponent("Quiero crear mi jardín")}&body=${encodeURIComponent(body)}`;
  window.location.href = mailto;
});
