document.addEventListener("DOMContentLoaded", () => {
    const datetimeEl = document.getElementById("datetime");
    if (datetimeEl) {
        datetimeEl.textContent = new Date().toLocaleString();
    }

    const toggleBtn = document.getElementById("toggle-dark");
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            document.body.classList.toggle("dark");
            localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
        });
    }

    // Load theme preference
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark");
    }
});
