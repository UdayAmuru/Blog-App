from django import forms
from .models import *
from blog.models import *

#choices =[('coding', 'coding'),('sports','sports'),('entertainment','entertainment')]
choices = Category.objects.all().values_list('name','name')
choices_list = [choice for choice in choices]

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio' , 'profile_pic' , 'website_url' , 'fb_url' , 'twitter_url' , 'insta_url' , 'pinterest_url')
        widgets = {
                'bio':forms.Textarea(attrs={'class':'form-control'}),
                #'profile_pic':forms.ImageField(attrs={'class':'form-control'}),
                'website_url':forms.TextInput(attrs={'class':'form-control'}),
                'fb_url':forms.TextInput(attrs={'class':'form-control'}),
                'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
                'insta_url':forms.TextInput(attrs={'class':'form-control'}),
                'pinterest_url':forms.TextInput(attrs={'class':'form-control'}),
}


     





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet' , 'header_image')
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
                 #'author':forms.Select(attrs={'class':'form-control'}),
                'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
                'snippet':forms.Textarea(attrs={'class':'form-control'}),


        } 

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet')
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title place holder'}),
                'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                #'author':forms.Select(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
                'snippet':forms.Textarea(attrs={'class':'form-control'}),


        } 



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name' , 'body')
        widgets = {
                #'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title place holder'}),
                'name':forms.TextInput(attrs={'class':'form-control'}),
                #'author':forms.Select(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
                #'snippet':forms.Textarea(attrs={'class':'form-control'}),


        } 