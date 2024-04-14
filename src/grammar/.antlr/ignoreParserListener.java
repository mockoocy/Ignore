// Generated from /home/s2i/uczelnia/kompilatory/Ignore/src/grammar/ignoreParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ignoreParser}.
 */
public interface ignoreParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ignoreParser#literalNumeric}.
	 * @param ctx the parse tree
	 */
	void enterLiteralNumeric(ignoreParser.LiteralNumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#literalNumeric}.
	 * @param ctx the parse tree
	 */
	void exitLiteralNumeric(ignoreParser.LiteralNumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ignoreParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ignoreParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ignoreParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ignoreParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ignoreParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ignoreParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#property}.
	 * @param ctx the parse tree
	 */
	void enterProperty(ignoreParser.PropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#property}.
	 * @param ctx the parse tree
	 */
	void exitProperty(ignoreParser.PropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#endTag}.
	 * @param ctx the parse tree
	 */
	void enterEndTag(ignoreParser.EndTagContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#endTag}.
	 * @param ctx the parse tree
	 */
	void exitEndTag(ignoreParser.EndTagContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#startTag}.
	 * @param ctx the parse tree
	 */
	void enterStartTag(ignoreParser.StartTagContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#startTag}.
	 * @param ctx the parse tree
	 */
	void exitStartTag(ignoreParser.StartTagContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ignoreParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ignoreParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(ignoreParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(ignoreParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#functionStart}.
	 * @param ctx the parse tree
	 */
	void enterFunctionStart(ignoreParser.FunctionStartContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#functionStart}.
	 * @param ctx the parse tree
	 */
	void exitFunctionStart(ignoreParser.FunctionStartContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(ignoreParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(ignoreParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(ignoreParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(ignoreParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(ignoreParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(ignoreParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ignoreParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ignoreParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(ignoreParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(ignoreParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(ignoreParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(ignoreParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#elif}.
	 * @param ctx the parse tree
	 */
	void enterElif(ignoreParser.ElifContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#elif}.
	 * @param ctx the parse tree
	 */
	void exitElif(ignoreParser.ElifContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#elif_statement}.
	 * @param ctx the parse tree
	 */
	void enterElif_statement(ignoreParser.Elif_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#elif_statement}.
	 * @param ctx the parse tree
	 */
	void exitElif_statement(ignoreParser.Elif_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void enterElse_statement(ignoreParser.Else_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void exitElse_statement(ignoreParser.Else_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#control_statement}.
	 * @param ctx the parse tree
	 */
	void enterControl_statement(ignoreParser.Control_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#control_statement}.
	 * @param ctx the parse tree
	 */
	void exitControl_statement(ignoreParser.Control_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ignoreParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ignoreParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ignoreParser#wrapped_expr}.
	 * @param ctx the parse tree
	 */
	void enterWrapped_expr(ignoreParser.Wrapped_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ignoreParser#wrapped_expr}.
	 * @param ctx the parse tree
	 */
	void exitWrapped_expr(ignoreParser.Wrapped_exprContext ctx);
}