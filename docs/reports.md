# Technical reports

These pages are a collection of findings while working on ComPWA packages such as
{mod}`ampform`, {mod}`qrules`, and {mod}`tensorwaves`. Most of these findings were not
implemented, but may become relevant later on or could be useful to other frameworks as
well.

```{include} report-inventory.md

```

<!-- DataTables to make the table above look nice -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<script type="text/javascript" src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready( function () {
    $('table').DataTable( {
        "columnDefs": [
            { "width": "3em", "targets": 0 },
            { "width": "10em", "targets": 2 }
        ],
        "pageLength": 100,
    });
} );
</script>

````{dropdown} Execution times
```{nb-exec-table}
```
````

```{toctree}
:glob:
:hidden:
report/*
```
