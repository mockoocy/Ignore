param(
    [Parameter(Mandatory = $true)]
    [string]$path
)

&antlr4-parse ignoreParser.g4 ignoreLexer.g4 program -gui $path
