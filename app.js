async function check() {
  const id = document.getElementById("co").value;
  const r = await fetch(`/api/readiness/${id}`);
  const d = await r.json();
 
  document.getElementById("score").innerHTML =
    `<h2>${d.score} / 100</h2><p class="${d.route}">
     ${d.route === "ROUTE" ? "Ready to route"
                           : "Hold - inputs missing"}</p>`;
 
  document.getElementById("gaps").innerHTML =
    d.missing.map(m => `<li>${m}</li>`).join("");
}
