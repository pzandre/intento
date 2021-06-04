const parentDiv = Array.from(document.getElementsByClassName("django-quill-widget-container"));
const toolbar = Array.from(document.getElementsByClassName("ql-toolbar"));
const editor = Array.from(document.getElementsByClassName("ql-editor"));

for (let i = 0; i < editor.length; i++) {
    toolbar[i].style.display = "none";
    parentDiv[i].style.borderTop = "1px solid #ccc";
    editor[i].addEventListener("focusin", function () {
      toolbar[i].style.display = "";
      parentDiv[i].style.borderTop = "";
    });
    editor[i].addEventListener("focusout", function () {
      toolbar[i].style.display = "none";
      parentDiv[i].style.borderTop = "1px solid #ccc";
    });
}