from jinja2 import Template


names = [{'name': 'вася', 'old': '18'},
         {'name': 'гриша', 'old': '4'}]

tpl = '''
{%- for i in name -%}
    {{ i.name.upper() }} 
{% endfor -%}
'''

tm = Template(tpl)

mgs = tm.render(name = names)

print(mgs)