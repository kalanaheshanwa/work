/* Kalana Square — interactions */
(function () {
  "use strict";

  /* ---- compact mobile navigation ---- */
  var menuToggle = document.querySelector(".nav-menu-toggle");
  var mobileNav = document.getElementById("mobile-nav");
  function closeMobileNav() {
    if (!menuToggle || !mobileNav) return;
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    mobileNav.hidden = true;
  }
  if (menuToggle && mobileNav) {
    menuToggle.addEventListener("click", function () {
      var open = menuToggle.getAttribute("aria-expanded") === "true";
      menuToggle.setAttribute("aria-expanded", open ? "false" : "true");
      menuToggle.setAttribute("aria-label", open ? "Open navigation" : "Close navigation");
      mobileNav.hidden = open;
    });
    [].slice.call(mobileNav.querySelectorAll("a")).forEach(function (link) {
      link.addEventListener("click", closeMobileNav);
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMobileNav(); });
  }

  /* ---- scroll reveal for cards ---- */
  var cards = [].slice.call(document.querySelectorAll(".card"));
  if (cards.length) {
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e, i) {
          if (e.isIntersecting) {
            var el = e.target;
            var visIndex = cards.filter(function (c) { return !c.classList.contains("hide"); }).indexOf(el);
            setTimeout(function () { el.classList.add("in"); }, Math.max(0, visIndex % 9) * 45);
            io.unobserve(el);
          }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
      cards.forEach(function (c) { io.observe(c); });
    } else {
      cards.forEach(function (c) { c.classList.add("in"); });
    }
  }

  /* ---- filtering ---- */
  var chips = [].slice.call(document.querySelectorAll(".chip"));
  var grid = document.getElementById("grid");
  var empty = document.getElementById("empty");
  var countEl = document.getElementById("count");

  function applyFilter(cat) {
    var shown = 0;
    cards.forEach(function (card) {
      var cats = (card.getAttribute("data-cats") || "").split("|");
      var match = cat === "all" || cats.indexOf(cat) !== -1;
      card.classList.toggle("hide", !match);
      if (match) {
        shown++;
        card.classList.remove("in");
        // re-trigger reveal
        // eslint-disable-next-line no-unused-expressions
        card.offsetHeight;
        requestAnimationFrame(function () {
          setTimeout(function () { card.classList.add("in"); }, (shown % 9) * 40);
        });
      }
    });
    if (countEl) countEl.textContent = String(shown).padStart(2, "0") + " / " + String(cards.length).padStart(2, "0");
    if (empty) empty.style.display = shown === 0 ? "block" : "none";
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
      chip.setAttribute("aria-pressed", "true");
      applyFilter(chip.getAttribute("data-cat"));
      if (history.replaceState) {
        var c = chip.getAttribute("data-cat");
        history.replaceState(null, "", c === "all" ? location.pathname : "#" + c);
      }
    });
  });

  // deep-link via hash on load
  if (chips.length) {
    var hash = (location.hash || "").replace("#", "");
    var target = chips.filter(function (c) { return c.getAttribute("data-cat") === hash; })[0];
    if (target) {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
      target.setAttribute("aria-pressed", "true");
      applyFilter(hash);
    } else if (countEl) {
      countEl.textContent = String(cards.length).padStart(2, "0") + " / " + String(cards.length).padStart(2, "0");
    }
  }

  /* ---- interactive project process ---- */
  var processTabs = [].slice.call(document.querySelectorAll(".process-tab"));
  var processPanels = [].slice.call(document.querySelectorAll(".process-panel"));
  var processCurrent = document.getElementById("process-current");
  var processPrev = document.querySelector(".process-prev");
  var processNext = document.querySelector(".process-next");
  var processPips = [].slice.call(document.querySelectorAll(".process-pips span"));
  function selectProcessTab(tab, moveFocus) {
    var panelId = tab.getAttribute("aria-controls");
    var activeIndex = processTabs.indexOf(tab);
    processTabs.forEach(function (item) {
      var active = item === tab;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-selected", active ? "true" : "false");
      item.setAttribute("tabindex", active ? "0" : "-1");
    });
    processPanels.forEach(function (panel) {
      var active = panel.id === panelId;
      panel.classList.toggle("is-active", active);
      panel.hidden = !active;
    });
    processPips.forEach(function (pip, index) { pip.classList.toggle("is-active", index === activeIndex); });
    if (processCurrent) processCurrent.textContent = String(activeIndex + 1);
    if (processPrev) processPrev.disabled = activeIndex === 0;
    if (processNext) processNext.disabled = activeIndex === processTabs.length - 1;
    if (tab.scrollIntoView && window.innerWidth <= 760) tab.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    if (moveFocus) tab.focus();
  }
  processTabs.forEach(function (tab, index) {
    tab.addEventListener("click", function () { selectProcessTab(tab, false); });
    tab.addEventListener("keydown", function (e) {
      if (e.key !== "ArrowLeft" && e.key !== "ArrowRight" && e.key !== "Home" && e.key !== "End") return;
      e.preventDefault();
      var next = index;
      if (e.key === "ArrowRight") next = (index + 1) % processTabs.length;
      if (e.key === "ArrowLeft") next = (index - 1 + processTabs.length) % processTabs.length;
      if (e.key === "Home") next = 0;
      if (e.key === "End") next = processTabs.length - 1;
      selectProcessTab(processTabs[next], true);
    });
  });
  if (processPrev) processPrev.addEventListener("click", function () {
    var index = processTabs.findIndex(function (tab) { return tab.classList.contains("is-active"); });
    if (index > 0) selectProcessTab(processTabs[index - 1], false);
  });
  if (processNext) processNext.addEventListener("click", function () {
    var index = processTabs.findIndex(function (tab) { return tab.classList.contains("is-active"); });
    if (index < processTabs.length - 1) selectProcessTab(processTabs[index + 1], false);
  });

  /* ---- lightbox for full-site screenshots ---- */
  var lb = document.getElementById("lb");
  if (lb) {
    var lbImg = lb.querySelector("img");
    var lbName = lb.querySelector(".nm");
    var closeBtn = lb.querySelector(".x");

    function openLB(src, name) {
      lbImg.src = src;
      if (lbName) lbName.textContent = name || "";
      lb.classList.add("on");
      document.body.style.overflow = "hidden";
    }
    function closeLB() {
      lb.classList.remove("on");
      document.body.style.overflow = "";
      setTimeout(function () { lbImg.src = ""; }, 200);
    }

    [].slice.call(document.querySelectorAll("[data-zoom]")).forEach(function (z) {
      z.addEventListener("click", function () {
        openLB(z.getAttribute("data-zoom"), z.getAttribute("data-name"));
      });
    });
    if (closeBtn) closeBtn.addEventListener("click", closeLB);
    lb.addEventListener("click", function (e) { if (e.target === lb || e.target.classList.contains("lbscroll")) closeLB(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeLB(); });
  }

  /* ---- floating back-to-top ---- */
  var totop = document.getElementById("totop");
  if (totop) {
    var onScroll = function () {
      if (window.pageYOffset > 520) totop.classList.add("show");
      else totop.classList.remove("show");
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    totop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---- keyboard prev/next on project pages ---- */
  document.addEventListener("keydown", function (e) {
    if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    if (e.key === "ArrowLeft") {
      var p = document.querySelector(".pager a.prev:not(.disabled)");
      if (p) window.location.href = p.getAttribute("href");
    }
    if (e.key === "ArrowRight") {
      var n = document.querySelector(".pager a.next:not(.disabled)");
      if (n) window.location.href = n.getAttribute("href");
    }
  });
})();
