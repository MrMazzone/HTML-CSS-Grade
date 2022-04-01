# HTML/CSS Grade
Autograder helper Python lib for easy HTML and CSS checks

# Example
```

```

# Example with Unit Testing
```

```

# Docs
To start using the library in your code, be sure to import it 
```
import htmlcssgrade
```

### HTML_Check Class
The first class taht can be instantiated to check an HTML file with `HTML_Check()`. The constructor has one argument, `filepath` which is the path to the file you want to check.
Example:
```
```

**Properties:**
- `filepath` - the path to the file you are checking.
- `html_obj` - the BeautifulSoup object being used.
- `code` - text representation of the css file, which can be printed or parsed.

**Methods:**
check_HTML() - Given a snip of HTML code, returns True if the snip is found in the student's file.
check_element_used() - Given an element, returns True if the student used the element.
check_num_element_used() - Given an element and number, returns True if student's file has at least specified number of that element. 
get_num_element_used() - Given an element, returns the number of times the element is used in student's file.
check_element_content() - Given an element and content, returns True if the content is in the element (ignores captialization, whitespace, etc).
check_element_content_exact() - Given an element and content, returns True if the content is in the element character for character.
check_elements_attribute() - Given an element, attribute, and value, returns True if element's attribute is equal to the value.
check_element_has_attribute() - Given an element and attribute, returns True if element's attribute was assigned any value.
get_list_of_elements_with_class() - Given a class name, returns a list of all elements with class set to given name.
check_element_has_class() - Given an element and class name, returns True if element was assigned class with given name.
get_element_with_id() - Given an id name, returns the element assigned the id.
check_element_has_id() - Given an element and id name, returns True if that element was assigned the id.
check_use_css_file() - Given a CSS filepath, returns True if HTML code uses that CSS file.
check_use_js_file() - Given a JS filepath, returns True if HTML code uses that JS file.





### CSS_Check Class
The second class that can be instantiated to check a CSS file with `CSS_Check()`. The constructor has one argument, `filepath` which is the path to the file you want to check.
Example:
```
```

**Properties:**
- `filepath` - the path to the file you are checking.
- `css_obj` - the cssutils object being used.
- `code` - text representation of the css file, which can be printed or parsed.

**Methods:**
check_declaration() - Given a selector and a declaration, returns True if in CSS.
check_property_used() - Given a selector and a property name, returns True if property was given a value in CSS.
check_selector_rule() - Given a selector, property, and property value, returns True if the property is set to that value.
check_selector_has_ruleset() - Given a selector, returns True if selector has a ruleset.
get_selector_ruleset() - Given a selector, returns the ruleset text.
get_property_value() - Given a selector and property, returns the property's value.
check_num_selector_declarations() - Given a selector and a number, returns True if selector has at least specified number of declarations.
check_num_selector_declarations_equal() - Given a selector and a number, returns True if selector has exact specified number of declarations.
get_num_selector_declarations() - Given a selector, returns the number of declarations in the ruleset.
check_num_selector_rulesets() - Given a number, returns True if number of selector rulesets is greater than or equal to the number.
check_num_selector_rulesets_equal() - Given a number, returns True if number of selector rulesets is equal to the number.
get_num_selector_rulesets() - Returns the number of selector rulesets in CSS file.
check_num_declarations() - Given a number, returns True if number of declarations in CSS file is greater than or equal to the number. 
check_num_declarations_equal() - Given a number, returns True if number of declarations in CSS file is equal to the number.
get_num_declarations() - Returns the number of declarations in CSS file.
