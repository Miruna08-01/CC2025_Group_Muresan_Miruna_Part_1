const API_URL = "http://127.0.0.1:5000/api/data";

async function loadData() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    const tbody = document.querySelector("#dataTable tbody");
    tbody.innerHTML = "";
    data.forEach(item => {
      const row = `<tr><td>${item.id}</td><td>${item.service}</td><td>${item.category}</td></tr>`;
      tbody.innerHTML += row;
    });
  } catch (err) {
    console.error("Error fetching data:", err);
  }
}

document.addEventListener("DOMContentLoaded", loadData);
