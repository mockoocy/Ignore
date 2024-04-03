param(
    [Parameter(Mandatory = $false)]
    [string]$path
)

$cmd = Get-Content .\gui-parse.sh

$finalCommand = "$cmd $path"

& $finalCommand
