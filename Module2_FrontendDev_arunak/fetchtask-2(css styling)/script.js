async function loadPosts() {
  const status = document.getElementById("status");
  const list = document.getElementById("list");

  status.textContent = "Loading notifications...";
  list.innerHTML = "";

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts?_limit=5"
    );

    if (!response.ok) {
      throw new Error("Error fetching data");
    }

    const data = await response.json();

    data.forEach(post => {
      const li = document.createElement("li");
      li.innerHTML = `
        <strong>${post.title}</strong>
        <p>${post.body}</p>
      `;
      list.appendChild(li);
    });

    status.textContent = "✅ Loaded successfully!";
  } catch (error) {
    status.innerHTML = `
      ❌ Failed to load notifications.<br>
      <button onclick="loadPosts()">Retry</button>
    `;
    console.error(error);
  }
}