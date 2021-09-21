$(document).ready(function () {
    $('#example')
            .dataTable({
                "responsive": true,
                "ajax": 'data.json'
            });
});