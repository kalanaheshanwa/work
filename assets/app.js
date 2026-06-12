/* Kalana Square — interactions */
(function () {
  "use strict";

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
