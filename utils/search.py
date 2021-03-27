from hello_world.models import *


class Search:
    def __init__(self, pattern, mode="lazy"):

        self.pattern = re.compile(pattern=pattern)
        self.mode = mode
        self.matched = []
        self.search()

    # searching for matching commas and thread post in names and texts
    def search(self):
        thread_set = Thread.objects.all()
        for _thread in thread_set.iterator():

            result_name = re.search(self.pattern, _thread.name)
            result_text = re.search(self.pattern, _thread.text)
            instance = None
            if result_text is not None or result_name is not None:
                instance = {"thread": _thread, "comments": []}

            comment_set = Comment.objects.filter(thread=_thread)
            for comment in comment_set.iterator():
                result_comment_text = re.search(self.pattern, comment.text)

                if result_comment_text is not None:
                    if instance is None:
                        instance = {"thread": _thread, "comments": []}
                    instance["comments"].append(comment)
            if instance is not None:
                self.push(instance)

    def push(self, instance):
        self.matched.append(instance)

    def popAll(self):
        return self.matched

    pass
