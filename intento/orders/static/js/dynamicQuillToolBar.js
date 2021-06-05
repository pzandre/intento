const parentDiv = Array.from(document.getElementsByClassName("django-quill-widget-container"));
const toolbar = Array.from(document.getElementsByClassName("ql-toolbar"));
const editor = Array.from(document.getElementsByClassName("ql-editor"));

function clearToolbar(index) {
  toolbar[index].style.display = "none";
  parentDiv[index].style.borderTop = "1px solid #ccc";
}

let editorArray = [];

for (let h = 0; h < editor.length; h++) {
  editorArray.push(h);
}
for (let i = 0; i < editor.length; i++) {
  toolbar[i].style.display = "none";
  parentDiv[i].style.borderTop = "1px solid #ccc";
  editor[i].addEventListener("focusin", function () {
    Array.prototype.except = function(val) {
      return this.filter(function(x) { return x !== val; });
    };

    parentDiv[i].style.borderTop = "";
    toolbar[i].style.display = "";
    editorArray.except(i).forEach(clearToolbar);
  });
}
