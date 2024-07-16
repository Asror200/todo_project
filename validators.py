from form import UserRegisterForm
from utils import Response

def check_validation(form: UserRegisterForm):
    if not form.username:
        return Response('Username is required', 404)
    if not form.password:
        return Response('Password is required', 404)