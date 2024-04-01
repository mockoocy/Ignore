param(
    [Parameter(Mandatory = $false)]
    [string]$path
)

$cmd = Get-Conetnt .\gui-parse.sh

$finalCommand = "$command $path"

& $finalCommand