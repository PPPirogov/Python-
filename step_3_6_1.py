from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)

for element in root.iter("scores"):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)


# tree.write("example_modified.xml")