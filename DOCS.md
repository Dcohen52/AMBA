# AMBA Transpiler
The AMBA Transpiler is a Python module that converts Python code to JavaScript (for now! I'm working on support for more languages) using an Abstract Syntax Tree (AST) approach. This transpiler provides support for a wide range of Python syntax elements, including loops, conditionals, functions, and operations. It also allows for the generated JavaScript code to be exported to a file.


To utilize the JavaScript Transpiler, instantiate the `JavaScript` class and invoke the translate method with the Python code as an argument:

``` python
js = JavaScript()
js_code = js.translate('for i in range(10):\n    print(i)')
```

The resulting JavaScript code will be:

``` javascript
for (let i = 0; i < 10; i++) {
  console.log(i);
}
```
## Supported Features
The AMBA Transpiler -> JavaScript class supports a comprehensive set of Python features, including:

* **Loops:** for and while
* **Conditionals:** if, elif, and else
* **Functions:** Function definitions and calls
* **Operations:** Arithmetic, comparison, and logical operators
* **Control statements:** break, continue, return, and raise
In addition, the transpiler provides specialized support for template literals:
``` javascript
document.querySelector("#element")
document.querySelector("#element").innerHTML = "content"
```
Using pseudo-functions notation in python:

``` python
dqs("element")
innerHTML("element", "content")
```
Respectively.


## Licensing
The AMBA Transpiler is provided under the MIT License, which allows for its use, modification, and distribution with minimal restrictions.

## Changelog
Enhanced support for document.querySelector, document.querySelector.innerHTML, and template literals.
By employing the JavaScript Transpiler, developers can achieve seamless and efficient conversion of Python code to JavaScript, ensuring compatibility across various programming environments.
