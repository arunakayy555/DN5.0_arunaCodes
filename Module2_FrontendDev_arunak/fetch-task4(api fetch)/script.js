function loadUsers() {
    fetch("https://jsonplaceholder.typicode.com/users")
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById("userList");
            list.innerHTML = "";

            data.forEach(user => {
                let li = document.createElement("li");
                li.innerText = user.name;
                list.appendChild(li);
            });
        });
}