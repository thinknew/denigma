from django.forms import ModelForm, CharField, Textarea

from models import Post


class PostForm(ModelForm):
    #title = CharField(widget=Textarea(attrs))
    text = CharField(widget=Textarea(attrs={'rows': 10, 'cols': 10,
                                            'style': 'font-family: monospace'}),
    help_text='<a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html=">reStructuredText Quick Reference</a>\
     | <a href="daringfireball.net/projects/markdown/basics">Markdown Basics</a></p>')

    comment = CharField(help_text='Optional, used for revision control.', required=False)

    class Meta:
        fields = ('title','text', 'tags', 'url', 'images', 'published', 'comment')
        model = Post