/* global frappe */
(function () {
	if (!(window.frappe && frappe.boot)) return;

	var themeName = frappe.boot.newara_theme;
	if (!themeName) return;

	var id = "newara-customer-theme";
	if (document.getElementById(id)) return;

	var link = document.createElement("link");
	link.id = id;
	link.rel = "stylesheet";
	link.href = "/assets/newara/css/themes/" + encodeURIComponent(themeName) + ".css";
	document.head.appendChild(link);
})();
