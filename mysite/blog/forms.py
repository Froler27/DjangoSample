from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class BlogForm(forms.Form):
    title = forms.CharField(label="标题", max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="内容", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'20'}))

