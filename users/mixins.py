from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.requset.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, _("Can't go there"))
        return redirect("core:home")


class LogoutOnlyView(UserPassesTestMixin):
    permission_denied_message = "Page Not Found"

    def test_func(self):
        return not self.request.user.is_authenticated  # 사용자의 로그인 여부

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoginOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy(("users:login"))