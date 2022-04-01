# HTML/CSS Grade
Autograder helper Python lib for easy HTML and CSS checks

# Example
```python
import htmlcssgrade

learner_css = htmlcssgrade.CSS_Check("css/style.css")
learner_html = htmlcssgrade.HTML_Check("index.html")

print(learner_css.code)
print(learner_css.check_declaration("body", "background-color: #F06543"))
print(learner_css.check_property_used("body", "font-style"))
print(learner_css.check_num_declarations(37))

print(learner_html.code)
print(learner_html.check_element_used("p"))
print(learner_html.check_element_content("a", "Home"))
print(learner_html.check_element_has_class("img", "center"))

```

# Example with Unit Testing
```python
import unittest
import htmlcssgrade

class CodingRoomsUnitTests(unittest.TestCase):

    def test_check_css(self):
        learner_css = htmlcssgrade.CSS_Check("css/style.css")
        self.assertTrue(learner_css.check_declaration("body", "background-color: #F06543"))
    
    def test_check_html(self):
        learner_html = htmlcssgrade.HTML_Check("index.html")
        self.assertTrue(learner_html.check_elements_attribute("img", "src", "img/hello.png"))

if __name__ == '__main__':
    unittest.main()
```

# Docs
To start using the library in your code, be sure to import it 
```python
import htmlcssgrade
```

### HTML_Check Class
The first class that can be instantiated is used to check an HTML file with `HTML_Check()`. The constructor has one argument, `filepath` which is the path to the file you want to check.
Example:
```python
learner_html = htmlcssgrade.HTML_Check("index.html")
```

**Properties:**
- `filepath` - the path to the file you are checking.
- `html_obj` - the BeautifulSoup object being used.
- `code` - text representation of the HTML file, which can be printed or parsed.

**Methods:**
- `check_HTML(code_snip)` - Given a snip of HTML code, returns True if the snip is found in the learner's file.   
   Example:
   ```python
   learner_html.check_HTML('<meta charset="UTF-8"/>')
   learner_html.check_HTML("<p>This is a paragraph</p>")
   ```
- `check_element_used(element)` - Given an element, returns True if the learner used the element.   
   Example:
   ```python
   learner_html.check_element_used("p")
   learner_html.check_element_used("ol")
   ```
- `check_num_element_used(element, number)` - Given an element and number, returns True if learner's file has at least specified number of that element.   
   Example:
   ```python
   learner_html.check_num_element_used("h2", 4)
   learner_html.check_num_element_used("p", 6)
   ```
- `get_num_element_used(element)` - Given an element, returns the number of times the element is used in learner's file.   
   Example:
   ```python
   learner_html.get_num_element_used("h2")
   learner_html.get_num_element_used("p")
   ```
- `check_element_content(element, content)` - Given an element and content, returns True if the content is in the element (ignores captialization, whitespace, etc).   
   Example:
   ```python
   learner_html.check_element_content("a", "Home")
   learner_html.check_element_content("title", "Super Awesome Title")
   ```
- `check_element_content_exact(element, content)` - Given an element and content, returns True if the content is in the element character for character.   
   Example:
   ```python
   learner_html.check_element_content_exact("a", "Home")
   learner_html.check_element_content_exact("title", "Super Awesome Title")
   ```
- `check_elements_attribute(element, attribute, value)` - Given an element, attribute, and value, returns True if element's attribute is equal to the value.   
   Example:
   ```python
   learner_html.check_elements_attribute("a", "href", "#")
   learner_html.check_elements_attribute("img", "src", "img/hello.png")
   ```
- `check_element_has_attribute(element, attribute)` - Given an element and attribute, returns True if element's attribute was assigned any value.   
   Example:
   ```python
   learner_html.check_element_has_attribute("img", "src")
   learner_html.check_element_has_attribute("a", "href")
   ```
- `get_list_of_elements_with_class(class_name)` - Given a class name, returns a list of all elements with class set to given name.      
   Example:
   ```python
   learner_html.get_list_of_elements_with_class("center")
   learner_html.get_list_of_elements_with_class("gold")
   ```
- `check_element_has_class(element, class_name)` - Given an element and class name, returns True if element was assigned class with given name.   
   Example:
   ```python
   learner_html.check_element_has_class("img", "center")
   learner_html.check_element_has_class("p", "center")
   ```
- `get_element_with_id(id_name)` - Given an id name, returns the element assigned the id.   
   Example:
   ```python
   learner_html.get_element_with_id("container")
   learner_html.get_element_with_id("container")
   ```
- `check_element_has_id(element, id_name)` - Given an element and id name, returns True if that element was assigned the id.   
   Example:
   ```python
   learner_html.check_element_has_id("div", "container")
   learner_html.check_element_has_id("p", "container")
   ```
- `check_use_css_file(css_filepath)` - Given a CSS filepath, returns True if HTML code uses that CSS file.   
   Example:
   ```python
   learner_html.check_use_css_file("css/style.css")
   learner_html.check_use_css_file("blah.css")
   ```
- `check_use_js_file(js_filepath)` - Given a JS filepath, returns True if HTML code uses that JS file.   
   Example:
   ```python
   learner_html.check_use_js_file("index.js")
   learner_html.check_use_js_file("blah.js")
   ```


### CSS_Check Class
The second class that can be instantiated is used to check a CSS file with `CSS_Check()`. The constructor has one argument, `filepath` which is the path to the file you want to check.
Example:
```python
learner_css = htmlcssgrade.CSS_Check("css/style.css")
```

**Properties:**
- `filepath` - the path to the file you are checking.
- `css_obj` - the cssutils object being used.
- `code` - text representation of the CSS file, which can be printed or parsed.

**Methods:**
- `check_declaration(selector, declaration)` - Given a selector and a declaration, returns True if in CSS.   
   Example:
   ```python
   learner_css.check_declaration(".center", "display: block")
   learner_css.check_declaration("body", "background-color: #F06543")
   ```
- `check_property_used(selector, property)` - Given a selector and a property name, returns True if property was given a value in CSS.   
   Example:
   ```python
   learner_css.check_property_used("body", "background-color")
   learner_css.check_property_used("body", "font-style")
   ```
- `check_selector_rule(selector, property, value)` - Given a selector, property, and property value, returns True if the property is set to that value.   
   Example:
   ```python
   learner_css.check_selector_rule("body", "background-color", "#F06543")
   learner_css.check_selector_rule("p", "font-style", "16pt")
   ```
- `check_selector_has_ruleset(selector)` - Given a selector, returns True if selector has a ruleset.   
   Example:
   ```python
   learner_css.check_selector_has_ruleset("body")
   learner_css.check_selector_has_ruleset("p")
   ```
- `get_selector_ruleset(selector)` - Given a selector, returns the ruleset text.   
   Example:
   ```python
   learner_css.get_selector_ruleset("body")
   learner_css.get_selector_ruleset(".center")
   ```
- `get_property_value(selector, property)` - Given a selector and property, returns the property's value.   
   Example:
   ```python
   learner_css.get_property_value("body", "background-color")
   learner_css.get_property_value("p", "font-style")
   ```
- `check_num_selector_declarations(selector, number)` - Given a selector and a number, returns True if selector has at least specified number of declarations.   
   Example:
   ```python
   learner_css.check_num_selector_declarations("body", 3)
   learner_css.check_num_selector_declarations("nav ul", 1)
   ```
- `check_num_selector_declarations_equal()` - Given a selector and a number, returns True if selector has exact specified number of declarations.   
   Example:
   ```python
   learner_css.check_num_selector_declarations_equal("body", 3)
   learner_css.check_num_selector_declarations_equal("nav ul", 1)
   ```
- `get_num_selector_declarations(selector)` - Given a selector, returns the number of declarations in the ruleset.   
   Example:
   ```python
   learner_css.get_num_selector_declarations("body")
   learner_css.get_num_selector_declarations("nav ul")
   ```
- `check_num_selector_rulesets(number)` - Given a number, returns True if number of selector rulesets is greater than or equal to the number.   
   Example:
   ```python
   learner_css.check_num_selector_rulesets(12)
   learner_css.check_num_selector_rulesets(20)
   ```
- `check_num_selector_rulesets_equal(number)` - Given a number, returns True if number of selector rulesets is equal to the number.   
   Example:
   ```python
   learner_css.check_num_selector_rulesets_equal(12)
   learner_css.check_num_selector_rulesets_equal(20)
   ```
- `get_num_selector_rulesets()` - Returns the number of selector rulesets in CSS file.   
   Example:
   ```python
   learner_css.get_num_selector_rulesets()
   ```
- `check_num_declarations(number)` - Given a number, returns True if number of declarations in CSS file is greater than or equal to the number.    
   Example:
   ```python
   learner_css.check_num_declarations(37)
   ```
- `check_num_declarations_equal(number)` - Given a number, returns True if number of declarations in CSS file is equal to the number.   
   Example:
   ```python
   learner_css.check_num_declarations_equal(37)
   ```
- `get_num_declarations()` - Returns the number of declarations in CSS file.   
   Example:
   ```python
   learner_css.get_num_declarations()
   ```
