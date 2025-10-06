from django import forms
from . models import Post, Category, Tag, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image","category", "tags"]
        labels = {
            "title" : "Title",
            "body" : "Content",
            "image" : "Photo",
            "category": "Select-category",
            "tag" : "Select-tags"
        }
        widgets = {
            "title" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Post-Title"
            
            }),

            "body" : forms.Textarea(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
            }),

            "image" : forms.FileInput(attrs={
                "class" : "block w-full text-sm text-gray-700 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",     
            }),

            "category": forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500"
            }),
            "tags": forms.SelectMultiple(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500"
            }),
            

        }

class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Category Name"
            })
        }

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name" : forms.TextInput(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Tag Name"
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        lebel = {
            "body" : "",
        }
        widgets = {
            "body" : forms.Textarea(attrs={
                "class" : "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500",
                "placeholder" : "Make your comment",
                "rows" : 4,
            })
        }

