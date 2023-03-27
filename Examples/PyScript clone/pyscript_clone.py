import re
from AMBA import JavaScript

class HTMLToJS:
    """
    This class provides a transpilation functionality for HTML code that contains embedded Python code snippets
    enclosed in tags of a specified name (jiminy - in this example). The class is an implementation example of the AMBA transpiler, which is
    a simple PyScript clone.

    The HTMLToJS class allows for the customization of the tag name used to identify Python code snippets and
    provides a template string for the generated JavaScript code. The transpiler uses the JavaScript class
    from the same module to translate the Python code to equivalent JavaScript code.

    Example usage:
    html_to_js = HTMLToJS()
    translated_html = html_to_js.translate('<html><jiminy>for i in range(10): print(i)</jiminy></html>')
    print(translated_html) # Output: '<html><script>for (let i = 0; i < 10; i++) { console.log(i); }</script></html>'
    """

    def __init__(self, tag_name='jiminy', js_code_template='{}'):
        self.tag_name = tag_name
        self.js_code_template = js_code_template
        self.python_tag_regex = re.compile(
            f'<{self.tag_name}>(.+?)</{self.tag_name}>', re.DOTALL)
        self.js_transpiler = JavaScript()

    def translate(self, html):
        python_tags = self.python_tag_regex.findall(html)

        for python_tag in python_tags:
            js_code = self.js_transpiler.translate(python_tag.strip())
            js_code = self.js_code_template.format(js_code)
            html = html.replace(
                f'<{self.tag_name}>{python_tag}</{self.tag_name}>', f"<script>{js_code}</script>")

        return html

# # Read the HTML file contents from disk
# with open('index.html', 'r') as f:
#     html_code = f.read()

# # Working on a fix for new-line parsing in external files - for now code-blocks are not working.


html_code = """
<!DOCTYPE html>
<html>

<head>
    <title>Example HTML file</title>
</head>

<body>
    <jiminy>
numbers = [1, 2, 3, 4, 5] 
total = sum(numbers) 
print(f'The sum of the numbers is {total}')
    </jiminy>
    <p>This is some regular HTML content.</p>
</body>

</html>
"""


# create an instance of the HTMLToJS class
html_to_js = HTMLToJS()

# convert the HTML code to JavaScript
js_code = html_to_js.translate(html_code)

print(js_code)


