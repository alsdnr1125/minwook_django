from django import forms
from users.models import ImageUpload

class UploadForm(forms.ModelForm):
	class Meta:
		model = ImageUpload
		fields = {'title', 'photo'}