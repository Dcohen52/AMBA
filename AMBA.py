import ast
import io
import sys


class JavaScript:
    """A transpiler that translates Python code to JavaScript.

    The JavaScript class provides methods to convert Python code to JavaScript, supporting various syntaxes,
    including loops, conditionals, functions, and operations. It uses the Python ast module to parse the input code
    and outputs the corresponding JavaScript code.

    Example usage:
        js = JavaScript()
        js_code = js.translate('for i in range(10):\n    print(i)')

        print(js_code)  # Output: 'for (let i = 0; i < 10; i++) {\n  console.log(i);\n}'

    The JavaScript class also includes a method to export the generated JavaScript code to a file.

    License: MIT
    """

    def __init__(self):
        self.indent_level = 0

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def emit(self, code):
        print('  ' * self.indent_level + code)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f'No visit_{type(node).__name__} method found')

    def visit_Module(self, node):
        for child in node.body:
            self.visit(child)

    def visit_FunctionDef(self, node):
        self.emit(f'function {node.name}({", ".join([arg.arg for arg in node.args.args])}) {{')
        self.indent()
        for child in node.body:
            self.visit(child)
        self.dedent()
        self.emit('}')

    def visit_Return(self, node):
        if node.value:
            self.emit(f'return {self.visit(node.value)};')
        else:
            self.emit('return;')

    def visit_Assign(self, node):
        target = self.visit(node.targets[0])
        value = self.visit(node.value)
        self.emit(f'let {target} = {value};')

    def visit_Name(self, node):
        return node.id

    def visit_Num(self, node):
        return str(node.n)

    def visit_Str(self, node):
        return f"'{node.s}'"

    def visit_BinOp(self, node):
        op = self.visit(node.op)
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f'({left} {op} {right})'

    def visit_Add(self, node):
        return '+'

    def visit_Sub(self, node):
        return '-'

    def visit_Mult(self, node):
        return '*'

    def visit_Div(self, node):
        return '/'

    def visit_Mod(self, node):
        return '%'

    def visit_Pow(self, node):
        return '**'

    def visit_Compare(self, node):
        ops = [self.visit(child) for child in node.ops]
        left = self.visit(node.left)
        comparators = [self.visit(child) for child in node.comparators]
        return f'({left} {ops[0]} {comparators[0]})'

    def visit_Eq(self, node):
        return '=='

    def visit_NotEq(self, node):
        return '!='

    def visit_Lt(self, node):
        return '<'

    def visit_LtE(self, node):
        return '<='

    def visit_Gt(self, node):
        return '>'

    def visit_GtE(self, node):
        return '>='

    def visit_If(self, node):
        test = self.visit(node.test)
        self.emit(f'if ({test}) {{')
        self.indent()
        self.visit(node.body[0])
        self.dedent()
        if node.orelse:
            self.emit('} else {')
            self.indent()
            self.visit(node.orelse[0])
            self.dedent()
        self.emit('}')

    def visit_For(self, node):
        target = self.visit(node.target)
        iter = self.visit(node.iter)
        if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
            if len(node.iter.args) == 1:
                self.emit(f'for (let {target} = 0; {target} < {self.visit(node.iter.args[0])}; {target}++) {{')
            elif len(node.iter.args) == 2:
                self.emit(
                    f'for (let {target} = {self.visit(node.iter.args[0])}; {target} < {self.visit(node.iter.args[1])}; {target}++) {{')
            elif len(node.iter.args) == 3:
                self.emit(
                    f'for (let {target} = {self.visit(node.iter.args[0])}; {target} < {self.visit(node.iter.args[1])}; {target} += {self.visit(node.iter.args[2])}) {{')
        elif isinstance(node.iter, ast.Call) and isinstance(node.iter.func,
                                                            ast.Attribute) and node.iter.func.attr == 'items':
            self.emit(
                f'for (let [{target}, {self.visit(node.target)}] of Object.entries({self.visit(node.iter.func.value)})) {{')
        elif isinstance(node.iter, ast.Call) and isinstance(node.iter.func,
                                                            ast.Attribute) and node.iter.func.attr == 'keys':
            self.emit(f'for (let {target} of Object.keys({self.visit(node.iter.func.value)})) {{')
        elif isinstance(node.iter, ast.Call) and isinstance(node.iter.func,
                                                            ast.Attribute) and node.iter.func.attr == 'values':
            self.emit(f'for (let {target} of Object.values({self.visit(node.iter.func.value)})) {{')
        elif isinstance(node.iter, ast.Name) and node.iter.id == 'zip':
            targets = [self.visit(target) for target in node.target.elts]
            iters = [self.visit(iter) for iter in node.iter.elts]
            max_length = self.translate(f"len({targets[0]})")
            for target, iter in zip(targets, iters):
                self.emit(f"let {target};")
            self.emit(f"for (let i = 0; i < {max_length}; i++) {{")
            self.indent()
            for target, iter in zip(targets, iters):
                self.emit(f"{target} = {iter}[i];")
            for child in node.body:
                self.visit(child)
            self.dedent()
            self.emit("}")
        else:
            self.emit(f'for (let {target} of {iter}) {{')
        self.indent()
        for child in node.body:
            self.visit(child)
        self.dedent()
        self.emit('}')

    def visit_Call(self, node):
        func = self.visit(node.func)
        args = ', '.join([self.visit(arg) for arg in node.args])
        if func == 'print':
            self.emit(f'console.log({args});')
        else:
            return f'{func}({args})'

    def visit_List(self, node):
        elts = [self.visit(child) for child in node.elts]
        return f'[{", ".join(elts)}]'

    def visit_Tuple(self, node):
        elts = [self.visit(child) for child in node.elts]
        return f'({", ".join(elts)})'

    def visit_Index(self, node):
        return self.visit(node.value)

    def visit_Subscript(self, node):
        value = self.visit(node.value)
        index = self.visit(node.slice)
        return f'{value}[{index}]'

    def visit_While(self, node):
        test = self.visit(node.test)
        self.emit(f'while ({test}) {{')
        self.indent()
        for child in node.body:
            self.visit(child)
        if node.orelse:
            self.emit('} else {')
            self.indent()
            for child in node.orelse:
                self.visit(child)
            self.dedent()
            self.emit('}')
        self.dedent()
        self.emit('}')

    def visit_Break(self, node):
        self.emit('break;')

    def visit_Continue(self, node):
        self.emit('continue;')

    def visit_Expr(self, node):
        self.visit(node.value)

    def visit_UnaryOp(self, node):
        op = self.visit(node.op)
        operand = self.visit(node.operand)
        return f'{op}{operand}'

    def visit_USub(self, node):
        return '-'

    def visit_UAdd(self, node):
        return '+'

    def visit_BoolOp(self, node):
        op = self.visit(node.op)
        values = [self.visit(child) for child in node.values]
        return f'({op.join(values)})'

    def visit_And(self, node):
        return '&&'

    def visit_Or(self, node):
        return '||'

    def visit_Not(self, node):
        return '!'

    def visit_ListComp(self, node):
        elt = self.visit(node.elt)
        generators = [self.visit(child) for child in node.generators]
        source = generators[0].split(' in ')[1]
        loop_vars = [gen.split(' in ')[0][1:] for gen in generators]
        output = f'{source}.map(({", ".join(loop_vars)}) => {elt}'
        for if_clause in generators[1:]:
            if 'if' in if_clause:
                output += f'.filter(({", ".join(loop_vars)}) => {self.visit(if_clause.split("if ")[1])})'
            else:
                output += f'.map(({", ".join(loop_vars)}) => {self.visit(if_clause)})'
        output += ')'
        return output

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return f"'{node.value}'"
        else:
            return str(node.value)

    def visit_comprehension(self, node):
        target = self.visit(node.target)
        iter = self.visit(node.iter)
        return f'.map(({target}) => {self.visit(node.ifs[0])})'

    def visit_NameConstant(self, node):
        return str(node.value).lower()

    def visit_NoneType(self, node):
        return 'null'

    def translate(self, code):
        parsed = ast.parse(code)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        self.visit(parsed)
        js_code = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return js_code

    def visit_GeneratorExp(self, node):
        elt = self.visit(node.elt)
        generators = [self.visit(child) for child in node.generators]
        source = generators[0].split(' in ')[1]
        loop_var = generators[0].split(' in ')[0][1:]
        for if_clause in generators[1:]:
            if 'if' in if_clause:
                source += f'.filter(({loop_var}) => {self.visit(if_clause.split("if ")[1])})'
            else:
                source += f'{self.visit(if_clause)}'
        return f'{source}.map(({loop_var}) => {elt})'

    def visit_Attribute(self, node):
        value = self.visit(node.value)
        attr = node.attr
        return f'{value}.{attr}'

    def visit_Raise(self, node):
        if node.exc:
            exc = self.visit(node.exc)
            self.emit(f'throw {exc};')
        else:
            self.emit('throw new Error();')

    def export_js(self, code, filename, path=''):
        with open(f"{path}{filename}.js", 'w') as file:
            file.write(str(code))