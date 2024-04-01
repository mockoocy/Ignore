# Ignore

a simple yet powerful

## Generating AST for the language

Bundled with script to generate Abstract Syntax Tree for the lang.

### Windows

```powershell
gui-parse <filename>
```

### Linux

```bash
sh gui-parse.sh <filename>
```

### Requiremens

JDK >= 11

### Generating Lexer and Parser

To generate Lexer and Parser for our language run the following command using ANTLR CLI.

```bash
antlr4 -Dlanguage=Python3 src/ignoreLexer.g4 src/ignoreParser.g4
# or using bash:
sh generate.sh
```
