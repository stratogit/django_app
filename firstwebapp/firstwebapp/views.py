from django.shortcuts import render

class Article:
    def __init__ (self,title,content,id):
        self.id = id
        self.title = title
        self.content = content

def index(request):
    article1= Article    (
        id=1,
        title ='Article 1',
        content = '''article 1 content
        second line
        last line ''' #''' creates multiple lines
    )

    article2= Article    (
        id=2,
        title ='Article 2',
        content = '''article 2 content
        second line
        last line ''' #''' creates multiple lines
    )

    article3= Article    (
        id=3,
        title ='Article 3',
        content = '''article 3 content
        second line
        last line ''' #''' creates multiple lines
    )

    context ={
        'articles':[article1,article2,article3]
        
    }

    return render (request,'index.html', context)