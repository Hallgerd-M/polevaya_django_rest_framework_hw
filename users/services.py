import stripe

from config import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_price(amount):
    """Creates price in Stripe"""

    return stripe.Price.create(
        currency="RUB",
        unit_amount=amount * 100,
        product_data={"name": "payment"},
    )


def create_stripe_session(price):
    """Create payment session in Stripe"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
