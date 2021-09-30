from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree

# def prettyXml(element, indent, newline, level = 0): 
#     if element:   
#         if element.text == None or element.text.isspace():     
#             element.text = newline + indent * (level + 1)      
#         else:    
#             element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)       
#     temp = list(element)
#     for subelement in temp:    
#         if temp.index(subelement) < (len(temp) - 1):     
#             subelement.tail = newline + indent * (level + 1)    
#         else:
#             subelement.tail = newline + indent * level   
#         prettyXml(subelement, indent, newline, level = level + 1) 



from enum import Enum
class ComponentType(Enum):
	MASTER = "MASTER"
	SLAVE = "SLVAE"
	CLIENT = "CLIENT"


def metainfoMaker():
	pass


def addComponent():
	pass

def customCommands():
	pass



metainfo = Element('metainfo')

schemaVersion = SubElement(metainfo,'schemaVersion')
schemaVersion.text = '2.0'

services = SubElement(metainfo,'services')

service = SubElement(services,'service')
name = SubElement(services,'name')
name.text = "SAMPLESRV"
displayName = SubElement(services,'displayName')
displayName.text = "New Sample Service"
comment = SubElement(services,'comment')
comment.text = "A New Sample Service"
version = SubElement(services,'version')
version.text = "1.0.0"

components = SubElement(services,'service')

component = SubElement(components,'component')

cname = SubElement(component,'name')
cname.text = "SAMPLESRV_MASTER"
cdisplayName = SubElement(component,'displayName')
cdisplayName.text = "Sample Srv Master"
ccategory = SubElement(component,'category')
ccategory.text = "MASTER"
ccardinality = SubElement(component,'cardinality')
ccardinality.text = "1"

commandScript = SubElement(component,'commandScript')

script = SubElement(commandScript,'script')
script.text = "scripts/master.py"
scriptType = SubElement(commandScript,'scriptType')
scriptType.text = "PYTHON"
timeout = SubElement(commandScript,'timeout')
timeout.text = "600"




from xml.dom import minidom
xml_string = etree.tostring(metainfo)
tree = minidom.parseString(xml_string)
xml_string = tree.toxml()

xmlstr = minidom.parseString(etree.tostring(metainfo)).toprettyxml(indent="   ")
with open("result2.xml", "w") as f:
    f.write(xmlstr.encode('utf-8'))

