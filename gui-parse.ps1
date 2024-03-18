param(
    [Parameter(Mandatory = $false)]
    [string]$path
)

&antlr4-parse ignoreParser.g4 ignoreLexer.g4 program -tokens -gui $path
