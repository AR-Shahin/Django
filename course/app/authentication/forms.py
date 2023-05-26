from django import forms

    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class" : "form-control","type" : "text","placeholder" : "Enter Your Username"
            },
        ),
        label="User Name"
    )
    
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control","type" : "password","placeholder" : "Enter Your Password"
            },
        ),
        label="Password"
    )
    
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class" : "form-control","type" : "text","placeholder" : "Enter Your Username","value" : "Ars"
            },
        ),
        label="User Name",
        required=False
    )
    
    email = forms.CharField(
        widget= forms.EmailInput(
            attrs={
                "class" : "form-control",
                "type" : "email",
                "placeholder" : "Enter Your Email"
            },
        ),
        label="Email",
        required=False
    )
    
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control","type" : "password","placeholder" : "Enter Your Password","value" : "password"
            },
        ),
        label="Password",
        required=False
    )