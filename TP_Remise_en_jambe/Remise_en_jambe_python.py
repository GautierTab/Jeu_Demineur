import requests
import xml.etree.ElementTree as ET

url = 'https://wxs.ign.fr/essentiels/geoportail/wmts?SERVICE=WMTS&REQUEST=GetCapabilities'

filename = 'donnees.xml'
r = requests.get(url,)

if r.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(r.content)

ET.register_namespace('', "http://www.opengis.net/wmts/1.0")
ET.register_namespace('ows', "http://www.opengis.net/ows/1.1")
ET.register_namespace('xlink', "http://www.w3.org/1999/xlink")
ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace('gml', "http://www.opengis.net/gml")

tree = ET.parse(filename)
root = tree.getroot()

# Affichage des noms 
# print(root[3])
# print(root[3][0])
# print(root[3][0][4])

contents = root.find('{http://www.opengis.net/wmts/1.0}Contents')
layers = contents.findall('{http://www.opengis.net/wmts/1.0}Layer')

dict = ['ADMIN_EXPRESS', 'CADASTRALPARCELS.PARCELLAIRE_EXPRESS', 'GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2', 'ORTHOIMAGERY.ORTHOPHOTOS']

for layer in layers:
    identifier = layer.find('{http://www.opengis.net/ows/1.1}Identifier')
    value = identifier.text
    if value not in dict:
        contents.remove(layer)

tree.write('output.xml', encoding="utf-8")
