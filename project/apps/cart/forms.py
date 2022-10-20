from django import forms

# ============================================================================ #


# =============================== ADD CART FORM ============================== #


class CartAddBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
