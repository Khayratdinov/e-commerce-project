from django.forms import ModelForm, TextInput, NumberInput, Textarea

# ============================================================================ #
from .models import ContactMessage


# ============================== CONTACT MESSAGE ============================= #


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "subject", "message"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Name *"}),
            "phone": NumberInput(
                attrs={"class": "form-control", "placeholder": "Phone * +99894123456"}
            ),
            "subject": TextInput(
                attrs={"class": "form-control", "placeholder": "Subject (Mavzu)"}
            ),
            "message": Textarea(
                attrs={"class": "form-control", "placeholder": "Xabar ..."}
            ),
        }
