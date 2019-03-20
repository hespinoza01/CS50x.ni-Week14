class Comment:
    def __init__(self, __name=None, __content=None):
        self.name = __name
        self.content = __content


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value