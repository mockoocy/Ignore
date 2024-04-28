from antlr4.error.ErrorListener import ErrorListener


class IgnoreErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(
            f"ERROR: when parsing line {line} column {column}: {msg}\n" 
        )
