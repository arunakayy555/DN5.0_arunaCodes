async function loadPosts() {
  const status = document.getElementById("status");
  const list = document.getElementById("list");

  status.textContent = "Loading...";
  list.innerHTML = "";

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts?_limit=5"
    );

    if (!response.ok) {
      throw new Error("Failed to fetch");
    }

    const data = await response.json();

    data.forEach(post => {
      const li = document.createElement("li");
      li.textContent = post.title;
      list.appendChild(li);
    });

    status.textContent = "";
  } catch (error) {
    status.innerHTML = "Error! <button onclick='loadPosts()'>Retry</button>";
    console.error(error);
  }
}