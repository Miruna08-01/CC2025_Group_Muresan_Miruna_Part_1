const API_URL = "const API_URL = \"https://cc2025-api.azurewebsites.net/api/data\";\n";

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
