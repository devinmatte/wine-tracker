// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#searched-wine').DataTable({
    "columnDefs": [
            {
                "targets": [ 0 ],
                "visible": false,
                "searchable": false
            }
        ]
  });
  $('#searched-wine tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        console.log( data );
    } );

    $('#dataTable').DataTable();
});
