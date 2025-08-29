document.getElementById("searchBox").addEventListener("keyup", function() {
  let filter = this.value.toLowerCase();
  let items = document.querySelectorAll("#testList li");

  items.forEach(li => {
    let text = li.textContent.toLowerCase();
    li.style.display = text.includes(filter) ? "" : "none";
  });
});
document.getElementById("searchBox").addEventListener("keyup", function() {
  let filter = this.value.toLowerCase();
  let items = document.querySelectorAll("#testList li");

  items.forEach(li => {
    let text = li.textContent.toLowerCase();
    li.style.display = text.includes(filter) ? "" : "none";
  });
});
