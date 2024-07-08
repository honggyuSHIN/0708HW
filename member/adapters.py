# member/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class NoEmailAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.email = ''
        if commit:
            user.save()
        return user