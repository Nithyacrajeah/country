book = {"name": "notebook", "price": "25", "pages": "200", "type": "roled", "mrp": "20"}

print(book["name"])
print(book["pages"])
print(book["price"])
print(book["type"])
print("brand_type" in book)
book["brand_type"] = "classmate"
print(book)

print(book["mrp"])
book["mrp"] = 20
print(book)
