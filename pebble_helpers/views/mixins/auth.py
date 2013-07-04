from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """Applies the login_required decorator to the as_view class method of a
    view.
    Simply inherit from this class to get the benefits.
    """
    @classmethod
    def as_view(cls, **initkwargs):
        """
        """
        view = super(LoginRequiredMixin, cls).as_view
        return login_required(view(**initkwargs))
