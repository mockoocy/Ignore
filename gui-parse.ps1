param(
    [Parameter(Mandatory = $false)]
    [string]$path
)

&antlr4-parse src/ignoreParser.g4 src/ignoreLexer.g4 program -tokens -gui $path
