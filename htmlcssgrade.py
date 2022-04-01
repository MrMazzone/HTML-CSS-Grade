#######################
# HTML/CSS Grade
# Version 1.0.1
# Created by Joe Mazzone
# Documentation: https://github.com/MrMazzone/HTML-CSS-Grade
#######################

from bs4 import BeautifulSoup
import cssutils

class HTML_Check:
    """
    Create an object that allows you to check learner HTML code.

    Properties
    ----------
    filepath - the path to the file you are checking.
    html_obj - the BeautifulSoup object being used.
    code - text representation of the HTML file, which can be printed or parsed.

    Methods
    -------
    check_HTML() - Given a snip of HTML code, returns True if the snip is found in the learner's file.
    check_element_used() - Given an element, returns True if the learner used the element.
    check_num_element_used() - Given an element and number, returns True if learner's file has at least specified number of that element. 
    get_num_element_used() - Given an element, returns the number of times the element is used in learner's file.
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
    """
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath) as fp:
            self.html_obj = BeautifulSoup(fp, 'html.parser')
        self.code = self.html_obj.prettify()
        
    def check_HTML(self, code_snip):
        """Does learner HTML have ___ code snip?"""
        return (code_snip.casefold().replace(" ", "").replace("\n", "") in str(self.html_obj.contents[2]).casefold().replace(" ", "").replace("\n", ""))

    def check_element_used(self, element):
        """Does learner HTML have ___ element?"""
        return (len(self.html_obj.find_all(element)) > 0)

    def check_num_element_used(self, element, number):
        """Does learner HTML have ___ number of ___ element?"""
        return (len(self.html_obj.find_all(element)) >= number)

    def get_num_element_used(self, element):
        """Gets the number of times ___ element is used."""
        return (len(self.html_obj.find_all(element)))

    def check_element_content(self, element, content):
        """Does ___ element contain ___ content?"""
        for line in self.html_obj.find_all(element):
            if (content.casefold().replace(" ", "").replace("\n", "") in str(line.contents).casefold().replace(" ", "").replace("\n", "")):
                return True
        return False

    def check_element_content_exact(self, element, content):
        """Is ___ element's content ___ exactly?"""
        for line in self.html_obj.find_all(element):
            if (content in str(line.contents)):
                return True
        return False

    def check_elements_attribute(self, element, attribute, value):
        """Does ___ element have ___ attribute with ___ value?"""
        for line in self.html_obj.find_all(element):
            if (value == line.attrs.get(attribute)):
                return True
        return False

    def check_element_has_attribute(self, element, attribute):
        """Does ___ element have ___ attribute with a value?"""
        for line in self.html_obj.find_all(element):
            if (line.attrs.get(attribute) != None):
                return True
        return False

    def get_list_of_elements_with_class(self, class_name):
        """Gets a list of all elements with ___ class name."""
        return self.html_obj.find_all(class_=class_name)

    def check_element_has_class(self, element, class_name):
        """"Is ___ element assigned ___ class name?"""
        return (len(self.html_obj.find_all(element, class_=class_name)) > 0)

    def get_element_with_id(self, id_name):
        """Gets element with ___ id name."""
        return self.html_obj.find(id=id_name).name
        
    def check_element_has_id(self, element, id_name):
        """Does ___ element have ___ id name assigned?"""
        return (len(self.html_obj.find_all(element, id=id_name)) > 0)

    def check_use_css_file(self, css_filepath):
        """Does learner HTML use ___ CSS file?"""
        for line in self.html_obj.find_all("link"):
            if (str(line.attrs.get("rel")) == "['stylesheet']" and str(line.attrs.get("href")) == css_filepath):
                return True
        return False

    def check_use_js_file(self, js_filepath):
        """Does learner HTML use ___ JS file?"""
        for line in self.html_obj.find_all("script"):
            if (str(line.attrs.get("type")) == "text/javascript" and str(line.attrs.get("src")) == js_filepath):
                return True
        return False


class CSS_Check:
    """
    Create an object that allows you to check learner CSS code.

    Properties
    ----------
    filepath - the path to the file you are checking.
    css_obj - the cssutils object being used.
    code - text representation of the CSS file, which can be printed or parsed.

    Methods
    -------
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
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.css_obj = cssutils.parseFile(filepath)
        self.code = self.css_obj.cssText
    
    def check_declaration(self, selector, declaration):
        """Does ___ selector have ___ declaration?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (declaration.replace(" ", "").replace(";", "") in rule.style.cssText.replace(" ", "").replace(";", ""))
        return False

    def check_property_used(self, selector, property):
        """Does ___ selector have ___ property set?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (property.replace(" ", "") in rule.style.cssText)
        return False
    
    def check_selector_rule(self, selector, property, value):
        """Does ___ selector have rule with ___ property set to ___ value?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (rule.style[property] == value)
        return False

    def check_selector_has_ruleset(self, selector):
        """Does ___ selector have a ruleset?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return True
        return False

    def get_selector_ruleset(self, selector):
        """Gets ___ selector's ruleset"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                if (len(rule.style.cssText) > 0):
                    return rule.style.cssText
        return selector + " does not have a ruleset."
    
    def get_property_value(self, selector, property):
        """Gets ___ selector's ___ property value"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                if (len(rule.style[property]) > 0):
                    return rule.style[property]
        return selector + " does not have " + property + " set."

    def check_num_selector_declarations(self, selector, number):
        """Does ___ selector have at least ___ number of declarations?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (rule.style.cssText.count("\n")+1 >= number)
        return False

    def check_num_selector_declarations_equal(self, selector, number):
        """Does ___ selector have at least ___ number of declarations?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (rule.style.cssText.count("\n")+1 == number)
        return False
    
    def get_num_selector_declarations(self, selector):
        """Gets ___ selector's number of declarations?"""
        for rule in self.css_obj:
            if rule.selectorText == selector:
                return (rule.style.cssText.count("\n")+1)
        return 0

    def check_num_selector_rulesets(self, number):
        """Does CSS file have at least ___ number of selector rulesets?"""
        count = 0
        for rule in self.css_obj:
            count += 1
        return (count >= number)
    
    def check_num_selector_rulesets_equal(self, number):
        """Does CSS file have exactly ___ number of selector rulesets?"""
        count = 0
        for rule in self.css_obj:
            count += 1
        return (count == number)

    def get_num_selector_rulesets(self):
        """Gets number of selector rulesets in CSS file."""
        count = 0
        for rule in self.css_obj:
            count += 1
        return count

    def check_num_declarations(self, number):
        """Does CSS file have at least ___ number of declarations?"""
        count = 0
        for rule in self.css_obj:
            count += rule.style.cssText.count("\n")+1 
        return (count >= number)

    def check_num_declarations_equal(self, number):
        """Does CSS file have exactly ___ number of declarations?"""
        count = 0
        for rule in self.css_obj:
            count += rule.style.cssText.count("\n")+1 
        return (count == number)

    def get_num_declarations(self):
        """Gets number of declarations in CSS file"""
        count = 0
        for rule in self.css_obj:
            count += rule.style.cssText.count("\n")+1 
        return count

"""
MIT License
Copyright (c) 2022 Joe Mazzone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""