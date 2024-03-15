from django import forms




# class CardFullForm(forms.Form):
#     word = forms.CharField(label='Word', max_length=100)
#     definition = forms.CharField(label='Definition', max_length=300)
#     sentence = forms.CharField(label='Sentence', max_length=250)



class UserInfo(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200)

