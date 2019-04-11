$(function() {
    var editor = new Simditor({
        textarea: $("#id_body"),
        placeholder: "在此编辑你的文章",
        upload: true,
        toolbar: ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link', 'image', 'hr', '|', 'indent', 'outdent', 'alignment']
        //optional options
    });
});
