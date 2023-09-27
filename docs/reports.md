# Technical reports

These pages are a collection of findings while working on ComPWA packages such as
{mod}`ampform`, {mod}`qrules`, and {mod}`tensorwaves`. Most of these findings were not
implemented, but may become relevant later on or could be useful to other frameworks as
well.

```{include} report-inventory.md

```

<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<style>
td.details-control {
    background: url('https://www.datatables.net/examples/resources/details_open.png') no-repeat center center;
    cursor: pointer;
}
tr.shown td.details-control {
    background: url('https://www.datatables.net/examples/resources/details_close.png') no-repeat center center;
}
</style>

<script>
function format(d) {
    return d[3] + d[4];
}

let table = new DataTable('table', {
    "columnDefs": [
        { "visible": false, "targets": [3, 4] },
        {
            "className": 'details-control',
            "orderable": false,
            "data": null,
            "defaultContent": '',
            "targets": 0
        },
        { "width": "10em", "targets": 5 },
    ],
    "order": [[1, 'asc']],
    "pageLength": 100,
});

table.on('click', 'td.details-control', function (e) {
    var tr = $(this).closest('tr');
    var row = table.row( tr );
    if ( row.child.isShown() ) {
        row.child.hide();
        tr.removeClass('shown');
    } else {
        row.child( format(row.data()) ).show();
        tr.addClass('shown');
    }
});
</script>

```{toctree}
:glob:
:hidden:
report/*
```

````{dropdown} Execution times
```{nb-exec-table}
```
````
