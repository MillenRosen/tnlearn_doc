/* The theme wraps tables in a second ready callback; observe those wrappers. */
jQuery(function () {
    let pendingTables = [...document.querySelectorAll(".rst-content table.docutils")];
    const updateScrollRegion = (wrapper) => {
        if (wrapper.scrollWidth > wrapper.clientWidth + 1) {
            wrapper.tabIndex = 0;
            wrapper.setAttribute("role", "region");
        } else {
            wrapper.removeAttribute("tabindex");
            wrapper.removeAttribute("role");
        }
    };
    const resizeObserver = new ResizeObserver((entries) => {
        entries.forEach(({ target }) => updateScrollRegion(target));
    });
    const prepareTables = () => {
        pendingTables = pendingTables.filter((table) => {
            const wrapper = table.closest(".wy-table-responsive");
            if (!wrapper) return true;
            const headers = [...table.querySelectorAll("thead tr:first-child th")];
            table.dataset.columns = headers.length;
            table.classList.toggle("parameter-table", headers[0]?.textContent.trim() === "Parameter"
                && headers[1]?.textContent.trim() === "Default");
            const heading = table.closest("section")?.querySelector("h2, h1");
            const label = heading?.cloneNode(true);
            label?.querySelector(".headerlink")?.remove();
            wrapper.setAttribute("aria-label", (label?.textContent.trim() || "Documentation") + " table");
            updateScrollRegion(wrapper);
            resizeObserver.observe(wrapper);
            return false;
        });
        if (!pendingTables.length) tableObserver.disconnect();
    };
    const tableObserver = new MutationObserver(prepareTables);
    tableObserver.observe(document.querySelector(".document"), { childList: true, subtree: true });
    prepareTables();

    const toggle = document.querySelector(".doc-menu-toggle");
    const navigation = document.querySelector(".wy-nav-side");
    if (!toggle || !navigation) return;
    navigation.id = "doc-navigation";
    toggle.setAttribute("aria-controls", navigation.id);
    const syncNavigation = () => {
        const open = navigation.classList.contains("shift");
        const label = open ? "Close navigation" : "Open navigation";
        toggle.setAttribute("aria-expanded", String(open));
        toggle.setAttribute("aria-label", label);
        toggle.title = label;
    };
    new MutationObserver(syncNavigation).observe(navigation, {
        attributes: true, attributeFilter: ["class"],
    });
    syncNavigation();
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && navigation.classList.contains("shift")) {
            toggle.click();
            toggle.focus();
        }
    });
});
