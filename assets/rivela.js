/* Ceraldi Caffè: comparsa discreta delle sezioni (solo se il visitatore non ha chiesto di ridurre il movimento).
   Senza JavaScript, o con movimento ridotto, tutto resta visibile. */
(function () {
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var el = document.querySelectorAll('.rivela');
  if (!el.length) return;
  document.documentElement.classList.add('js-rivela');
  var io = new IntersectionObserver(function (voci) {
    voci.forEach(function (v) {
      if (v.isIntersecting) { v.target.classList.add('visto'); io.unobserve(v.target); }
    });
  }, { rootMargin: '0px 0px -6% 0px' });
  el.forEach(function (x) { io.observe(x); });
})();
