# Create your views here.
from pebble_helpers.views.mixins.forms import RedirectReverseMixin


class SuccessUrlView(RedirectReverseMixin):
    """View that has a Success Url
    """
    success_url = 'testproject-success-plain'
