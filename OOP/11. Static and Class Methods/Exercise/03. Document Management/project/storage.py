from music.category import Category
from music.topic import Topic
from music.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_ids = [category.id for category in self.categories]
        if category_id in category_ids:
            self.categories[category_ids.index(category_id)].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_ids = [topic.id for topic in self.topics]
        if topic_id in topic_ids:
            self.topics[topic_ids.index(topic_id)] = Topic(new_topic, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document_ids = [document.id for document in self.documents]
        self.documents[document_ids.index(document_id)].file_name = new_file_name

    def delete_category(self, category_id):
        category_ids = [category.id for category in self.categories]
        self.categories.remove(self.categories[category_ids.index(category_id)])

    def delete_topic(self, topic_id):
        topic_ids = [topic.id for topic in self.topics]
        self.topics.remove(self.topics[topic_ids.index(topic_id)])

    def delete_document(self, document_id):
        document_ids = [document.id for document in self.documents]
        self.documents.remove(self.documents[document_ids.index(document_id)])

    def get_document(self, document_id):
        document_ids = [document.id for document in self.documents]
        return self.documents[document_ids.index(document_id)]

    def __repr__(self):
        string = ''
        for document in self.documents:
            string += document.__repr__() + '\n'
        return string
