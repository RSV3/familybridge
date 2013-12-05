import xml.etree.ElementTree as et

num_institutions = 0
tree = et.parse('institutions.xml')
root = tree.getroot()
for child in root:
  num_institutions += 1

print "Num institutions:", num_institutions
   

