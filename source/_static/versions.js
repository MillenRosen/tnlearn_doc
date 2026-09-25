document.addEventListener("DOMContentLoaded", () => {
    const selector = document.getElementById("doc-version-select");
    if (selector) {
        selector.addEventListener("change", () => {
            window.location.assign(selector.value);
        });
    }
});
