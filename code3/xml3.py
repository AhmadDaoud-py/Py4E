import xml.etree.ElementTree as ET

data = ''' <a>
                <b>X</b>
                <c>
                    <d>Y</d>
                    <e>Z</e>
                </c>
            </a> ''' 

tree = ET.fromstring(data)

print(tree.find("/a/c/e").text)
