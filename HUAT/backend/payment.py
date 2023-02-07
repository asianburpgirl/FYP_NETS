import json
import os
import stripe
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# configure stripe
stripe_keys = {
    'secret_key': 'sk_test_51MVFnNEK9AxKlwWVNSPD8wSNLNpSmqcuX2KncHhV6gzDde4AhFOImaqbkZQQrSCWxcJ6FHZZ321jdtIGzH0F0UV100ykysWHWB',
    'publishable_key': 'pk_test_51MVFnNEK9AxKlwWVPfnTP44fQvkMd4HXXSKx1EJrb9JNHsBYtgX4KOctGmnzBiI3R6GaI9uN2rDCKQlB19LOcQJO00Nf2FrDpe',
}

# This is your test secret API key.
stripe.api_key = stripe_keys['secret_key']

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

@app.route('/config')
def get_publishable_key():
    stripe_config = {'publicKey': stripe_keys['publishable_key']}
    return jsonify(stripe_config)

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    domain_url = 'http://localhost:8100/tabs/wallet'
    try:
        data = json.loads(request.data)

        # create new checkout session
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url +
            '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/canceled',
            payment_method_types=['card'],
            mode='payment',
            line_items = calculate_order_amount(data['items'])
        )

        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)
