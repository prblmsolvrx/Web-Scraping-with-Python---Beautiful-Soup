"""
 It appears there's a minor hiccup with the current code,
 as it's not listing the subproducts with class 'product'.
 Dive in and determine what might be causing the issue. Remember,
 the extraction should focus on all items marked as products.
"""

from bs4 import BeautifulSoup

html_content = '''
<div class="inventory">
    <span class="product">Widget A</span>
    <span class="product">Widget B</span>
    <span class="tool">
        <span class="product">Subproduct C - 1</span>
    </span>
</div>'''

soup = BeautifulSoup(html_content, 'html.parser')
products = [item.text for item in soup.select('.product')]
print(products)

"""
output :-
['Widget A', 'Widget B', 'Subproduct C - 1']
"""