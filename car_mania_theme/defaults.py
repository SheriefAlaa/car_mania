from __future__ import unicode_literals
# from socket import gethostname
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook's link"),
    description=_("Car Mania Dealer's Facebook page."),
    editable=True,
    default="https://facebook.com/carmaniadealer",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter's link"),
    description=_("Car Mania Dealer's Twitter page."),
    editable=True,
    default="https://twitter.com/carmaniadealer",
)

register_setting(
    name="SOCIAL_LINK_INSTAGRAM",
    label=_("Instagram's link"),
    description=_("Car Mania Dealer's Instagram page."),
    editable=True,
    default="#",
)

register_setting(
    name="SOCIAL_LINK_YOUTUBE",
    label=_("Youtube's link"),
    description=_("Car Mania Dealer's YouTube page."),
    editable=True,
    default="#",
)

register_setting(
    name="PHONE_NUMBER",
    label=_("Phone"),
    description=_("Car Mania Dealer's phone."),
    editable=True,
    default="0000-00000-00000",
)

register_setting(
    name="EMAIL",
    label=_("Email"),
    description=_("Car Mania Dealer's email."),
    editable=True,
    default="sales@carmaniadealer.com",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    default=("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_TWITTER",
    		 "SOCIAL_LINK_INSTAGRAM", "SOCIAL_LINK_YOUTUBE",
             "PHONE_NUMBER", "EMAIL", ),
    append=True,
)
