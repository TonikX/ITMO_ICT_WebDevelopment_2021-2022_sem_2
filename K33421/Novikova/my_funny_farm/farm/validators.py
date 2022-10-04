from django.core.exceptions import ValidationError
import magic


def file_validation(file):
    acceptable = ['image/png', 'image/jpeg', 'image/jpg']
    extension = magic.from_buffer(file.read(), mime=True)
    if extension not in acceptable:
        raise ValidationError(f'Try another file extension. For instance, PNG, JPG or JPEG')
    max_size = 5 * 1024 * 1024
    if file.size > max_size:
        raise ValidationError(f'Your file should be less than 5 MB')
