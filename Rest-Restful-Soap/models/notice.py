class Notice:
    def __init__(self,name,url):
        self.name = name
        self.url = url

    def to_json(self,) -> dict:
        return{
            'name' : self.name,
            'url' : self.url
        }
