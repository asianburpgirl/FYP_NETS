import json
import os
import stripe
from flask import Flask, render_template, jsonify, request, redirect
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
CORS(app)

@app.route('/config')
def get_publishable_key():
    stripe_config = {'publicKey': stripe_keys['publishable_key']}
    return jsonify(stripe_config)

YOUR_DOMAIN = 'http://13.55.33.68:8100/tabs/wallet'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = ""
        # data = json.loads(request.data)
        # found_item = ''
        # for item in Items:
        #     if item['id'] == data['itemId']:
        #         found_item = item
        # print(found_item)

        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    
                    'quantity': 1,
                    'price': 'price_1MYtU8EK9AxKlwWVvlseiWzF'
                }
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/successPage',
            cancel_url=YOUR_DOMAIN + '/successPage',
            
        )

        checkout_session = checkout_session.url

        return checkout_session
        
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)