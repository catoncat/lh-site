/* Language preference helper for static Lihua site */
(function () {
  const path = location.pathname;
  if (path === "/" || path === "/index.html") {
    const pref = localStorage.getItem("lihua-lang");
    const lang = pref === "en" || pref === "zh" ? pref : navigator.language.toLowerCase().startsWith("zh") ? "zh" : "en";
    location.replace("/" + lang + "/");
    return;
  }
  document.querySelectorAll("[data-set-lang]").forEach((el) => {
    el.addEventListener("click", () => {
      localStorage.setItem("lihua-lang", el.getAttribute("data-set-lang"));
    });
  });
})();
