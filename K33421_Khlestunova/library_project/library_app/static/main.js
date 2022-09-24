Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'upload/many/',
    maxFiles:5,
    maxFilesize:2,
    acceptedFiles:'.jpg, .jpeg, .png,.gif,.doc,.docx,.xls,.xlsx,.csv,.tsv,.ppt,.pptx,.pages,.odt,.rtf',
})