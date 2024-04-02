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
sh generate.sh #Bash
generate #Powershell
```

To odpalić the program type the following thing:

```bash
python src/lang/Driver.py <filename>
```
