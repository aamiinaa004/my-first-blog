from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class searchForm(forms.Form):
    ville= forms.ChoiceField(choices=[("0","choisir une ville"),("RABAT","Rabat"),], 
                             initial="0", required=False,
                          widget=forms.Select(attrs={"id":"id_ville"}))