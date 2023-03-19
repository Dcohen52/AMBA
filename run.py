from AMBA import JavaScript

with open('script.py', 'r') as file:
    js_code = file.read()

js_transpiler = JavaScript()
js = str(js_transpiler.translate(js_code))
js_transpiler.export_js(js, 'script', path='web/')  # Export to "web/script.js"
# print(js)

