param(
    [Parameter(Mandatory = $true)]
    [string]$path
)

antlr4-parse src/grammar/ignoreParser.g4 src/grammar/ignoreLexer.g4 program -tokens -gui -encoding utf-8 $path
