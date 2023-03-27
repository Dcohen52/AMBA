# Changelog

All notable changes to this project will be documented in this file.

## 2023-03-27

### Added
- Support for template literals in JavaScript.

## 2023-03-23

### Added
- Support for the `document.querySelector` method added - use `%dqs("element_name")`.
- Support for setting the `innerHTML` property of a selected element using `document.querySelector` - use `%innerHTML("html_content")`.


## 2023-03-19
### Initial release
Initialy implemented features:
- The class supports a diverse range of syntaxes, including loops, conditionals, functions, and operations.
- The class utilizes the Python ast module for parsing input code and generating corresponding JavaScript code.
- An example usage is provided for easy implementation.
- The `export_js` method enables the generated JavaScript code to be saved to a file.
- The class supports various Python constructs, such as:
  - function definitions.
  - returns.
  - assignments.
  - names.
  - numbers.
  - strings.
  - binary operations.
  - comparisons.
  - conditionals.
  - for loops.
  - while loops.
  - break and continue statements.
  - expressions.
  - unary operations.
  - boolean operations.
  - list comprehension.
  - joined strings.
  - formatted values.
  - constants.
  - name constants.
  - None types.
- The JavaScript class also provides support for attributes and generator expressions.
- The raise method handles exceptions effectively.
