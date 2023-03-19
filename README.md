# AMBA Transpiler

AMBA transpiler provides a powerful tool for developers seeking to translate their Python code into JavaScript, enabling them to seamlessly transition between the two languages. Leveraging the power of the ast module, this class accurately parses Python code and generates equivalent JavaScript code, with support for Python 3 syntax.

With a simple and intuitive API, this class provides a range of methods for visiting different types of nodes in the abstract syntax tree, enabling developers to quickly and easily generate high-quality JavaScript code. The translate method takes in Python code as a string and returns the corresponding JavaScript code, making it easy to integrate this tool into your existing development workflow.

In addition to its robust functionality, this class is also highly customizable - I'm currently working on adding support for additional languages. Furthermore, the class provides an export_js method that allows developers to easily export their generated code to a JavaScript file, streamlining the process of integrating this code into their projects.

## Features
* **Accurate translation:** the class accurately translates Python code to JavaScript code, ensuring that the resulting code is correct and error-free.
* **Python 3 syntax support:** the class is specifically designed to support Python 3 syntax, making it suitable for modern Python projects.
* **Intuitive API:** the class provides an intuitive API with a range of methods for visiting different types of nodes in the abstract syntax tree, making it easy for developers to generate JavaScript code from Python.
* **Customizable:** the class is highly customizable, with the developer currently working on adding support for additional languages. This allows developers to tailor the tool to their specific needs and requirements.
* **Easy integration:** the translate method takes in Python code as a string and returns the corresponding JavaScript code as a string, making it easy to integrate this tool into existing development workflows.
* **File export:** the class provide developers an easiy way to export their generated JavaScript code to a file, streamlining the process of integrating this code into their projects.
* **Versatility:** this tool can be used for a variety of applications, from web development to building cross-platform applications - check out [tempt](https://github.com/Dcohen52/tempt) and [MVCactus](https://github.com/Dcohen52/MVCactus)

## Getting started
1. Clone the repository from GitHub using the following command:

```git clone https://github.com/Dcohen52/AMBA.git```


2. Navigate to the root directory of the cloned repository using the cd command:

```cd AMBA```

You're now ready to use the code in the repository! Refer to the documentation (coming soon) or README file for more information on how to use the code.

### Example:
```
from AMBA import JavaScript

with open('script.py', 'r') as file:    # python file as input
    js_code = file.read()

js_transpiler = JavaScript()    # create an instance of JavaScript()
js = str(js_transpiler.translate(js_code))      # do the actual traspiling, using "js_transpiler.translate()"
js_transpiler.export_js(js, 'script', path='web/')  # Export to you prefered path, this one is: "web/script.js" (code, file_name, path_upto_wanted_folder)

# print(js) if you don't want to export to a file
```


## PYPI
The AMBA transpiler has yet to be added to PYPI, but I am currently working on expanding its capabilities. This includes adding support for new languages and making it more user-friendly for daily use.

## Contribute
Contributions to this project are welcome and encouraged! If you find a bug, have an idea for a new feature, or would like to contribute code, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this code for any purpose, as long as you include the original license and copyright notice. Please see the LICENSE file for more details.
