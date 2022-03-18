function copy_to_clipboard(element) {
	var copied_text = document.getElementById(element);
	navigator.clipboard.writeText(decodeURIComponent(copied_text.innerHTML));
	alert('Copied!');
}
