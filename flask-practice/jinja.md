# Jinja Template Engine in Flask

Jinja is a **template engine** for Python that Flask uses to generate dynamic HTML. It allows you to embed Python code directly in HTML files, making it easy to create dynamic web pages.

## What Is a Template Engine?

Instead of returning plain HTML strings from your Python code, you use templates with placeholders that get filled in with dynamic data. Here's the difference:

**Without templating (tedious):**

```python
@app.route('/user/')
def greet(name):
    return f'Hello, {name}!Welcome to my site.'
```

**With Jinja templating (clean):**

```python
@app.route('/user/')
def greet(name):
    return render_template('greeting.html', name=name)
```

And the template file (`greeting.html`):

```html
Hello, {{ name }}! Welcome to my site.
```

## Basic Syntax

### 1. Variables - Insert Python values

```jinja
<h1>{{ title }}</h1>
<p>{{ user.email }}</p>
<p>{{ items[0] }}</p>
```

### 2. Filters - Transform data

```jinja
<p>{{ name|upper }}</p>           <!-- Convert to uppercase -->
<p>{{ message|lower }}</p>        <!-- Convert to lowercase -->
<p>{{ price|round(2) }}</p>       <!-- Round to 2 decimals -->
<p>{{ text|length }}</p>          <!-- Get length -->
<p>{{ date|strftime('%Y-%m-%d') }}</p>  <!-- Format date -->
```

### 3. Conditionals - if/else logic

```jinja
{% if user.is_authenticated %}
    <p>Welcome back, {{ user.name }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

### 4. Loops - Iterate over data

```jinja
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### 5. Comments - Hidden from output

```jinja
{# This is a comment and won't appear in the HTML #}
```

## Complete Flask + Jinja Example

### Python code (app.py):

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def products():
    product_list = [
        {'name': 'Laptop', 'price': 999},
        {'name': 'Mouse', 'price': 25},
        {'name': 'Keyboard', 'price': 75}
    ]
    user = {'name': 'John', 'is_admin': True}

    return render_template('products.html',
                         products=product_list,
                         user=user)

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML template (templates/products.html):

```html
Products Welcome, {{ user.name }}! {% if user.is_admin %} You have admin
privileges. {% endif %} Our Products {% for product in products %} {{
product.name }} - ${{ product.price }} {% endfor %}
```

## Template Inheritance

Jinja lets you create a base template and extend it in child templates (DRY principle).

### base.html:

```html
{% block title %}My Site{% endblock %} My Website {% block content %}{% endblock
%} &copy; 2026 My Site
```

### child.html:

```html
{% extends "base.html" %} {% block title %}Products{% endblock %} {% block
content %} Our Products Here are our products... {% endblock %}
```

## Jinja Syntax Reference

| Syntax                   | Purpose                      |
| ------------------------ | ---------------------------- |
| `{{ variable }}`         | Insert variables/expressions |
| `{% statement %}`        | Control flow (if, for, etc.) |
| `{# comment #}`          | Comments (not rendered)      |
| `\|`                     | Apply filters to data        |
| `{% extends %}`          | Inherit from parent template |
| `{% block name %}`       | Define replaceable sections  |
| `{% include %}`          | Include another template     |
| `{% for item in list %}` | Loop over items              |
| `{% if condition %}`     | Conditional statement        |

## Common Filters

| Filter       | Example                       | Description                          |
| ------------ | ----------------------------- | ------------------------------------ |
| `upper`      | `{{ name\|upper }}`           | Convert to uppercase                 |
| `lower`      | `{{ text\|lower }}`           | Convert to lowercase                 |
| `capitalize` | `{{ text\|capitalize }}`      | Capitalize first letter              |
| `length`     | `{{ items\|length }}`         | Get length of list/string            |
| `round`      | `{{ price\|round(2) }}`       | Round to decimal places              |
| `sort`       | `{{ items\|sort }}`           | Sort a list                          |
| `reverse`    | `{{ items\|reverse }}`        | Reverse a list                       |
| `join`       | `{{ items\|join(', ') }}`     | Join list with separator             |
| `default`    | `{{ value\|default('N/A') }}` | Provide default value                |
| `safe`       | `{{ html_content\|safe }}`    | Mark as safe HTML (disable escaping) |

## Advanced Loops

### Loop with index:

```jinja
{% for item in items %}
    <li>{{ loop.index }}: {{ item }}</li>
{% endfor %}
```

### Loop with conditionals:

```jinja
{% for item in items %}
    {% if loop.first %}
        <li><strong>First: {{ item }}</strong></li>
    {% elif loop.last %}
        <li><strong>Last: {{ item }}</strong></li>
    {% else %}
        <li>{{ item }}</li>
    {% endif %}
{% endfor %}
```

### Loop object variables:

- `loop.index` - Current iteration (1-indexed)
- `loop.index0` - Current iteration (0-indexed)
- `loop.revindex` - Iteration from end (1-indexed)
- `loop.first` - True if first iteration
- `loop.last` - True if last iteration
- `loop.length` - Total length of the sequence

## Template Macros

Reusable template functions:

```jinja
{% macro render_product(product) %}
    <div class="product">
        <h3>{{ product.name }}</h3>
        <p>${{ product.price }}</p>
    </div>
{% endmacro %}

<!-- Using the macro -->
{% for product in products %}
    {{ render_product(product) }}
{% endfor %}
```

## Why Use Jinja?

✅ Keeps HTML separate from Python logic  
✅ Makes code more readable and maintainable  
✅ Prevents SQL injection and XSS attacks (auto-escapes HTML by default)  
✅ Allows code reuse through template inheritance  
✅ Reduces repetition with loops and conditionals  
✅ Easy to learn and powerful

## File Structure

```
my_flask_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── products.html
│   ├── user_profile.html
│   └── ...
└── static/
    ├── css/
    ├── js/
    └── images/
```

**Important:** Flask looks for templates in a `templates/` folder by default in your project root.

## Quick Start

1. Create a Flask app and templates folder
2. Use `render_template()` to return HTML templates
3. Pass variables to templates using keyword arguments
4. Use Jinja syntax in your HTML files
5. Templates are rendered with the variables you pass

## Resources

- [Official Jinja Documentation](https://jinja.palletsprojects.com/)
- [Flask Template Documentation](https://flask.palletsprojects.com/en/latest/templating/)
- [Jinja Built-in Filters](https://jinja.palletsprojects.com/en/latest/templates/#builtin-filters)

---

Jinja is the standard templating engine for Flask and makes building dynamic web applications much easier!
