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
Python >= 3.12

### Generating Lexer and Parser

To generate Lexer and Parser for our language run the following command using ANTLR CLI.

```bash
sh generate.sh #Bash
generate #Powershell
```

To odpalić the program type the following thing:

```bash
python run.py <filename>
```

### Testing

To run tests run

```bash
python pytest tests/*
```
