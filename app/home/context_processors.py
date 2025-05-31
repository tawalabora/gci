# from .forms import NewsletterForm
from .models import Organization


def provider(request):
    org = Organization.objects.first()

    has_any_social_media_link = org and (
        org.twitter
        or org.facebook
        or org.instagram
        or org.linkedin
        or org.tiktok
        or org.youtube
        or org.whatsapp
        or org.telegram
        or org.snapchat
        or org.pinterest
    )

    return {
        # Hardcoded values for the organization
        "org_fullname": "Great Commissioners International",
        "org_shortname": "GCI",
        "org_motto": "",
        "org_accent_color": "red",
        # Dynamic values from the Organization
        "org": org,
        # Boolean indicating if the Organization has any social media link present
        "has_any_social_media_link": bool(has_any_social_media_link),
        # "newsletterform": NewsletterForm(),
    }
