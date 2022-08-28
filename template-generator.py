# template-generator.py
# given original text, such as product intro, find generic pieces that can be isolated and changed
# look for specific adjectives that can be changed to generic ones to apply more broadly
# 
# Example intro:
# Original: Got a design emergency? Good news: Spencer is on the job. Available in two of our most popular fabrics for speedier delivery, this track-arm sofa is still sleek, still modern, and still tailored by hand, just the way you'd expect an Ethan Allen sofa to be.
# Generic: Got a design emergency? Good news: <Product Name> is on the job. Available in our most popular materials for speedier delivery, this comfortable <product type> is elegant, traditional, and crafted by hand, just the way you would expect a Highly Favored <product type> to be.

import re

original = 'Got a design emergency? Good news: Spencer is on the job. Available in two of our most popular fabrics for speedier delivery, this track-arm sofa is still sleek, still modern, and still tailored by hand, just the way you\'d expect an Ethan Allen sofa to be. '
print("Original: " + original)

product_name = 'Spencer'
seller = 'Ethan Allen'
product_type = 'sofa'

template = re.sub(product_name, "<Product Name>", original)
template = re.sub(seller, "<Seller>", template)
template = re.sub(product_type, "<product type>", template)
print("Template: " + template)
