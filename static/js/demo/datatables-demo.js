// Call the dataTables jQuery plugin
$(document).ready(function () {
    var table = $('#searched-wine').DataTable({
        "columnDefs": [
            {
                "targets": [0],
                "visible": false,
                "searchable": false
            }
        ]
    });
    $('#searched-wine tbody').on('click', 'button', function () {
        var data = table.row($(this).parents('tr')).data();
        console.log(data);
        $(this).attr("disabled", true);
        fetch('/save', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(function (response) {
                console.log(response.text())
            });
    });

    $('#dataTable').DataTable();
});
