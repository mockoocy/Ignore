param(
    [Parameter(Mandatory = $false)]
    [string]$path
)

$cmd = Get-Content .\gui-parse.sh

$finalCommand = "$command $path"

& $finalCommand
