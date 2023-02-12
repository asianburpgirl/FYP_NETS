<template>
  <div>
    <stripe-checkout
      ref="checkoutRef"
      mode="payment"
      :pk="publishableKey"
      :line-items="lineItems"
      :success-url="successURL"
      :cancel-url="cancelURL"
      @loading="v => loading = v"
    />
    <button @click="submit">Pay now!</button>
  </div>
</template>

<script>
import { StripeCheckout } from 'vue-stripe-checkout';
export default {
  components: {
    StripeCheckout,
  },
  data () {
    this.publishableKey = 'pk_test_51MVFnNEK9AxKlwWVPfnTP44fQvkMd4HXXSKx1EJrb9JNHsBYtgX4KOctGmnzBiI3R6GaI9uN2rDCKQlB19LOcQJO00Nf2FrDpe';
    return {
      loading: false,
      lineItems: [
        {
          price: 'price_1MabPcEK9AxKlwWVgzlADBHE', // The id of the one-time price you created in your Stripe dashboard
          quantity: 1,
        },
      ],
      successURL: 'http://localhost:8100/tabs/wallet/successPage',
      cancelURL: 'http://localhost:8100/tabs/wallet/successPage',
    };
  },
  methods: {
    submit () {
      // You will be redirected to Stripe's secure checkout page
      this.$refs.checkoutRef.redirectToCheckout();
    },
    mounted () {
      const recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', 'https://js.stripe.com/v3/')
      document.head.appendChild(recaptchaScript)
    }
  },
};
</script>
