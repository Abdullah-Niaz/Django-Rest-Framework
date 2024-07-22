from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
    def __str__(self):
        return f"Comment: {self.content} by {self.email} at {self.created}"
comment = Comment(email='leila@example.com', content='foo bar')
print(comment)