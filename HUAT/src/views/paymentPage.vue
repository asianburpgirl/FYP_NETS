<template>
  <table class="table table-hover">
<thead>
  <tr>
    <th scope="col">Title</th>
    <th scope="col">Author</th>
    <th scope="col">Purchase Price</th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Green eggs and ham</td>
    <td>Dr. Seuss</td>
    <td>$9.99</td>
    <td>
      <div class="btn-group" role="group">
          <button type="button" class="btn btn-primary btn-sm" @click="purchaseBook()"> Purchase </button>
      </div>
    </td>
  </tr>
</tbody>
</table>
</template>


<script>
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
      return {
          stripe: null,
      }
  },
  methods: {
      purchaseBook() {
        fetch('http://localhost:4242/create-payment-intent', {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          
          body: JSON.stringify({ item:123 }),
        })
        .then((result) => result.json())
        .then((data) => {
          // Redirect to Stripe Checkout
          return this.stripe.redirectToCheckout({ sessionId: 123 });
        })
        .then((res) => {
          console.log(res);
        });
      },
      getStripePublishableKey() {
          fetch('http://localhost:4242/config')
          .then((result) => result.json())
          .then((data) => {
              // Initialize Stripe.js
              this.stripe = Stripe(data.publicKey); // eslint-disable-line no-undef
          });
      },
      created() {
          this.getStripePublishableKey();
      },
      mounted(){
        const recaptchaScript = document.createElement('script')
        recaptchaScript.setAttribute('src', 'https://js.stripe.com/v3/')
        document.head.appendChild(recaptchaScript)
      }
  }
})
</script>