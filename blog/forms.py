from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name' : 'Your Name',
            'user_email' : 'Your Email',
            'comment_text' : 'Your Comment'
        }

        error_messages = {
            'user_name' : {
                'required' : 'Your name can not be empty!',
                'max_length' : 'Your name is too long!'
                },
            'user_email' : {
                'required' : 'Your email can not be empty!',
                'invalid' : 'Please enter valid emial address',
            },
            'comment_text' :{
                'required' : 'Comment field is required!'
            }
        }
        