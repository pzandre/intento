var quill = new Quill('#editor', {
modules: {
imageResize: {
},
toolbar: [
[{ 'header': [1, 2, 3, 4, 5, 6, false] }],
['bold', 'italic', 'underline', 'strike'],
[{ 'color': [] }, { 'background': [] }],
[{ 'align': [] }],
['image'],

   ]
}
});
