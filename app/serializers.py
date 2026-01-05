import json
import xml.etree.ElementTree as Et
from app.book import Book


class BookSerializer(Book):
    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = Et.Element("book")
            title = Et.SubElement(root, "title")
            title.text = self.title
            content = Et.SubElement(root, "content")
            content.text = self.content
            return Et.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
