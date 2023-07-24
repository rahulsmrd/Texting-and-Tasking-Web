from django import forms
from home_page.models import *

#start your forms here

class taskForm(forms.ModelForm):
    class Meta():
        model=taskModel
        fields=('task','assigned_to')
        widgets={
             'task': forms.TextInput(attrs={
                  'placeholder':'Enter the task',
             })
        }

class messageForm(forms.ModelForm):
    class Meta():
        model=messageModel
        fields=('message',)
        
        widgets={
            'message' : forms.TextInput(attrs={
                 'placeholder':'Type a Message',
                 'style':'width:21em;text-align:center;',
                 'class':'form-control active fs-5',
            })
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['message'].label = ""



class newmessageForm(forms.ModelForm):
    class Meta():
        model=messageModel
        fields=('message','to_user',)
        
        widgets={
            'message' : forms.TextInput(attrs={'placeholder':'Type a Message',})
        }
