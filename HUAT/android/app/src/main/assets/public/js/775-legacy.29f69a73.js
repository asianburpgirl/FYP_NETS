"use strict";(self["webpackChunkHUAT"]=self["webpackChunkHUAT"]||[]).push([[775],{8775:(e,t,n)=>{n.r(t),n.d(t,{startInputShims:()=>A});var o=n(4074),r=n(6587);
/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
const i=new WeakMap,s=(e,t,n,o=0,r=!1)=>{i.has(e)!==n&&(n?d(e,t,o,r):l(e,t))},a=e=>e===e.getRootNode().activeElement,d=(e,t,n,o=!1)=>{const r=t.parentNode,s=t.cloneNode(!1);s.classList.add("cloned-input"),s.tabIndex=-1,o&&(s.disabled=!0),r.appendChild(s),i.set(e,s);const a=e.ownerDocument,d="rtl"===a.dir?9999:-9999;e.style.pointerEvents="none",t.style.transform=`translate3d(${d}px,${n}px,0) scale(0)`},l=(e,t)=>{const n=i.get(e);n&&(i.delete(e),n.remove()),e.style.pointerEvents="",t.style.transform=""},c=(e,t,n)=>{if(!n||!t)return()=>{};const o=n=>{a(t)&&s(e,t,n)},i=()=>s(e,t,!1),d=()=>o(!0),l=()=>o(!1);return(0,r.a)(n,"ionScrollStart",d),(0,r.a)(n,"ionScrollEnd",l),t.addEventListener("blur",i),()=>{(0,r.b)(n,"ionScrollStart",d),(0,r.b)(n,"ionScrollEnd",l),t.addEventListener("ionBlur",i)}},u="input, textarea, [no-blur], [contenteditable]",m=()=>{let e=!0,t=!1;const n=document,o=()=>{t=!0},i=()=>{e=!0},s=o=>{if(t)return void(t=!1);const r=n.activeElement;if(!r)return;if(r.matches(u))return;const i=o.target;i!==r&&(i.matches(u)||i.closest(u)||(e=!1,setTimeout((()=>{e||r.blur()}),50)))};return(0,r.a)(n,"ionScrollStart",o),n.addEventListener("focusin",i,!0),n.addEventListener("touchend",s,!1),()=>{(0,r.b)(n,"ionScrollStart",o,!0),n.removeEventListener("focusin",i,!0),n.removeEventListener("touchend",s,!1)}},v=.3,f=(e,t,n)=>{var o;const r=null!==(o=e.closest("ion-item,[ion-item]"))&&void 0!==o?o:e;return p(r.getBoundingClientRect(),t.getBoundingClientRect(),n,e.ownerDocument.defaultView.innerHeight)},p=(e,t,n,o)=>{const r=e.top,i=e.bottom,s=t.top,a=Math.min(t.bottom,o-n),d=s+15,l=.75*a,c=l-i,u=d-r,m=Math.round(c<0?-c:u>0?-u:0),f=Math.min(m,r-s),p=Math.abs(f),h=p/v,w=Math.min(400,Math.max(150,h));return{scrollAmount:f,scrollDuration:w,scrollPadding:n,inputSafeY:4-(r-d)}},h=(e,t,n,o,i,s=!1)=>{let d;const l=e=>{d=(0,r.p)(e)},c=l=>{if(!d)return;const c=(0,r.p)(l);E(6,d,c)||a(t)||w(e,t,n,o,i,s)};return e.addEventListener("touchstart",l,{capture:!0,passive:!0}),e.addEventListener("touchend",c,!0),()=>{e.removeEventListener("touchstart",l,!0),e.removeEventListener("touchend",c,!0)}},w=async(e,t,n,i,a,d=!1)=>{if(!n&&!i)return;const l=f(e,n||i,a);if(n&&Math.abs(l.scrollAmount)<4)t.focus();else if(s(e,t,!0,l.inputSafeY,d),t.focus(),(0,r.r)((()=>e.click())),"undefined"!==typeof window){let r;const i=async()=>{void 0!==r&&clearTimeout(r),window.removeEventListener("ionKeyboardDidShow",a),window.removeEventListener("ionKeyboardDidShow",i),n&&await(0,o.c)(n,0,l.scrollAmount,l.scrollDuration),s(e,t,!1,l.inputSafeY),t.focus()},a=()=>{window.removeEventListener("ionKeyboardDidShow",a),window.addEventListener("ionKeyboardDidShow",i)};if(n){const e=await(0,o.g)(n),s=e.scrollHeight-e.clientHeight;if(l.scrollAmount>s-e.scrollTop)return"password"===t.type?(l.scrollAmount+=50,window.addEventListener("ionKeyboardDidShow",a)):window.addEventListener("ionKeyboardDidShow",i),void(r=setTimeout(i,1e3))}i()}},E=(e,t,n)=>{if(t&&n){const o=t.x-n.x,r=t.y-n.y,i=o*o+r*r;return i>e*e}return!1},y="$ionPaddingTimer",g=e=>{const t=document,n=t=>{b(t.target,e)},o=e=>{b(e.target,0)};return t.addEventListener("focusin",n),t.addEventListener("focusout",o),()=>{t.removeEventListener("focusin",n),t.removeEventListener("focusout",o)}},b=(e,t)=>{var n,r;if("INPUT"!==e.tagName)return;if(e.parentElement&&"ION-INPUT"===e.parentElement.tagName)return;if("ION-SEARCHBAR"===(null===(r=null===(n=e.parentElement)||void 0===n?void 0:n.parentElement)||void 0===r?void 0:r.tagName))return;const i=(0,o.a)(e);if(null===i)return;const s=i[y];s&&clearTimeout(s),t>0?i.style.setProperty("--keyboard-offset",`${t}px`):i[y]=setTimeout((()=>{i.style.setProperty("--keyboard-offset","0px")}),120)},S=!0,L=!0,A=(e,t)=>{const n=document,i="ios"===t,s="android"===t,a=e.getNumber("keyboardHeight",290),d=e.getBoolean("scrollAssist",!0),l=e.getBoolean("hideCaretOnScroll",i),u=e.getBoolean("inputBlurring",i),v=e.getBoolean("scrollPadding",!0),f=Array.from(n.querySelectorAll("ion-input, ion-textarea")),p=new WeakMap,w=new WeakMap,E=async e=>{await new Promise((t=>(0,r.c)(e,t)));const t=e.shadowRoot||e,n=t.querySelector("input")||t.querySelector("textarea"),i=(0,o.a)(e),u=i?null:e.closest("ion-footer");if(!n)return;if(i&&l&&!p.has(e)){const t=c(e,n,i);p.set(e,t)}const m="date"===n.type||"datetime-local"===n.type;if(!m&&(i||u)&&d&&!w.has(e)){const t=h(e,n,i,u,a,s);w.set(e,t)}},y=e=>{if(l){const t=p.get(e);t&&t(),p.delete(e)}if(d){const t=w.get(e);t&&t(),w.delete(e)}};u&&S&&m(),v&&L&&g(a);for(const o of f)E(o);n.addEventListener("ionInputDidLoad",(e=>{E(e.detail)})),n.addEventListener("ionInputDidUnload",(e=>{y(e.detail)}))}}}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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akMsRUFBYUMsRUFBU2lDLEdBQzNEd0gsRUFBYXJJLElBQUlyQixFQUFhbUssRUFDaEMsQ0FPQSxNQUFNQyxFQUErQixTQUFqQm5LLEVBQVF5SCxNQUFvQyxtQkFBakJ6SCxFQUFReUgsS0FDdkQsSUFBSzBDLElBQ0FsSSxHQUFjNkQsSUFDakJvRCxJQUNDUSxFQUFnQnRKLElBQUlMLEdBQWMsQ0FDbkMsTUFBTW1LLEVBQU9yRSxFQUFtQjlGLEVBQWFDLEVBQVNpQyxFQUFVNkQsRUFBVWpDLEVBQWdCbUYsR0FDMUZVLEVBQWdCdEksSUFBSXJCLEVBQWFtSyxFQUNuQyxHQUVJRSxFQUFtQnJLLElBQ3ZCLEdBQUlzQyxFQUFXLENBQ2IsTUFBTWdJLEVBQUtaLEVBQWE1SCxJQUFJOUIsR0FDeEJzSyxHQUNGQSxJQUVGWixFQUFhM0gsT0FBTy9CLEVBQ3RCLENBQ0EsR0FBSW1KLEVBQWMsQ0FDaEIsTUFBTW1CLEVBQUtYLEVBQWdCN0gsSUFBSTlCLEdBQzNCc0ssR0FDRkEsSUFFRlgsRUFBZ0I1SCxPQUFPL0IsRUFDekIsR0FFRXFKLEdBQWlCVixHQUNuQmhHLElBRUVpRCxHQUFpQmdELEdBQ25CVixFQUFvQnBFLEdBS3RCLElBQUssTUFBTXJELEtBQVM2SSxFQUNsQk0sRUFBY25KLEdBR2hCYSxFQUFJbUIsaUJBQWlCLG1CQUFxQlMsSUFDeEMwRyxFQUFjMUcsRUFBR3FILE9BQ2xCLElBQ0RqSixFQUFJbUIsaUJBQWlCLHFCQUF1QlMsSUFDMUNtSCxFQUFnQm5ILEVBQUdxSCxPQUNwQixHQUFFLEMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9IVUFULy4vbm9kZV9tb2R1bGVzL0Bpb25pYy9jb3JlL2NvbXBvbmVudHMvaW5wdXQtc2hpbXMuanMiXSwic291cmNlc0NvbnRlbnQiOlsiLyohXG4gKiAoQykgSW9uaWMgaHR0cDovL2lvbmljZnJhbWV3b3JrLmNvbSAtIE1JVCBMaWNlbnNlXG4gKi9cbmltcG9ydCB7IGcgYXMgZ2V0U2Nyb2xsRWxlbWVudCwgYyBhcyBzY3JvbGxCeVBvaW50LCBhIGFzIGZpbmRDbG9zZXN0SW9uQ29udGVudCB9IGZyb20gJy4vaW5kZXg5LmpzJztcbmltcG9ydCB7IGEgYXMgYWRkRXZlbnRMaXN0ZW5lciwgYiBhcyByZW1vdmVFdmVudExpc3RlbmVyLCByIGFzIHJhZiwgcCBhcyBwb2ludGVyQ29vcmQsIGMgYXMgY29tcG9uZW50T25SZWFkeSB9IGZyb20gJy4vaGVscGVycy5qcyc7XG5cbmNvbnN0IGNsb25lTWFwID0gbmV3IFdlYWtNYXAoKTtcbmNvbnN0IHJlbG9jYXRlSW5wdXQgPSAoY29tcG9uZW50RWwsIGlucHV0RWwsIHNob3VsZFJlbG9jYXRlLCBpbnB1dFJlbGF0aXZlWSA9IDAsIGRpc2FibGVkQ2xvbmVkSW5wdXQgPSBmYWxzZSkgPT4ge1xuICBpZiAoY2xvbmVNYXAuaGFzKGNvbXBvbmVudEVsKSA9PT0gc2hvdWxkUmVsb2NhdGUpIHtcbiAgICByZXR1cm47XG4gIH1cbiAgaWYgKHNob3VsZFJlbG9jYXRlKSB7XG4gICAgYWRkQ2xvbmUoY29tcG9uZW50RWwsIGlucHV0RWwsIGlucHV0UmVsYXRpdmVZLCBkaXNhYmxlZENsb25lZElucHV0KTtcbiAgfVxuICBlbHNlIHtcbiAgICByZW1vdmVDbG9uZShjb21wb25lbnRFbCwgaW5wdXRFbCk7XG4gIH1cbn07XG4vLyBUT0RPKEZXLTI4MzIpOiB0eXBlXG5jb25zdCBpc0ZvY3VzZWQgPSAoaW5wdXQpID0+IHtcbiAgcmV0dXJuIGlucHV0ID09PSBpbnB1dC5nZXRSb290Tm9kZSgpLmFjdGl2ZUVsZW1lbnQ7XG59O1xuY29uc3QgYWRkQ2xvbmUgPSAoY29tcG9uZW50RWwsIGlucHV0RWwsIGlucHV0UmVsYXRpdmVZLCBkaXNhYmxlZENsb25lZElucHV0ID0gZmFsc2UpID0+IHtcbiAgLy8gdGhpcyBhbGxvd3MgZm9yIHRoZSBhY3R1YWwgaW5wdXQgdG8gcmVjZWl2ZSB0aGUgZm9jdXMgZnJvbVxuICAvLyB0aGUgdXNlcidzIHRvdWNoIGV2ZW50LCBidXQgYmVmb3JlIGl0IHJlY2VpdmVzIGZvY3VzLCBpdFxuICAvLyBtb3ZlcyB0aGUgYWN0dWFsIGlucHV0IHRvIGEgbG9jYXRpb24gdGhhdCB3aWxsIG5vdCBzY3Jld1xuICAvLyB1cCB0aGUgYXBwJ3MgbGF5b3V0LCBhbmQgZG9lcyBub3QgYWxsb3cgdGhlIG5hdGl2ZSBicm93c2VyXG4gIC8vIHRvIGF0dGVtcHQgdG8gc2Nyb2xsIHRoZSBpbnB1dCBpbnRvIHBsYWNlIChtZXNzaW5nIHVwIGhlYWRlcnMvZm9vdGVycylcbiAgLy8gdGhlIGNsb25lZCBpbnB1dCBmaWxscyB0aGUgYXJlYSBvZiB3aGVyZSBuYXRpdmUgaW5wdXQgc2hvdWxkIGJlXG4gIC8vIHdoaWxlIHRoZSBuYXRpdmUgaW5wdXQgZmFrZXMgb3V0IHRoZSBicm93c2VyIGJ5IHJlbG9jYXRpbmcgaXRzZWxmXG4gIC8vIGJlZm9yZSBpdCByZWNlaXZlcyB0aGUgYWN0dWFsIGZvY3VzIGV2ZW50XG4gIC8vIFdlIGhpZGUgdGhlIGZvY3VzZWQgaW5wdXQgKHdpdGggdGhlIHZpc2libGUgY2FyZXQpIGludmlzaWJsZSBieSBtYWtpbmcgaXQgc2NhbGUoMCksXG4gIGNvbnN0IHBhcmVudEVsID0gaW5wdXRFbC5wYXJlbnROb2RlO1xuICAvLyBET00gV1JJVEVTXG4gIGNvbnN0IGNsb25lZEVsID0gaW5wdXRFbC5jbG9uZU5vZGUoZmFsc2UpO1xuICBjbG9uZWRFbC5jbGFzc0xpc3QuYWRkKCdjbG9uZWQtaW5wdXQnKTtcbiAgY2xvbmVkRWwudGFiSW5kZXggPSAtMTtcbiAgLyoqXG4gICAqIE1ha2luZyB0aGUgY2xvbmVkIGlucHV0IGRpc2FibGVkIHByZXZlbnRzXG4gICAqIENocm9tZSBmb3IgQW5kcm9pZCBmcm9tIHN0aWxsIHNjcm9sbGluZ1xuICAgKiB0aGUgZW50aXJlIHBhZ2Ugc2luY2UgdGhpcyBjbG9uZWQgaW5wdXRcbiAgICogd2lsbCBicmllZmx5IGJlIGhpZGRlbiBieSB0aGUga2V5Ym9hcmRcbiAgICogZXZlbiB0aG91Z2ggaXQgaXMgbm90IGZvY3VzZWQuXG4gICAqXG4gICAqIFRoaXMgaXMgbm90IG5lZWRlZCBvbiBpT1MuIFdoaWxlIHRoaXNcbiAgICogZG9lcyBub3QgY2F1c2UgZnVuY3Rpb25hbCBpc3N1ZXMgb24gaU9TLFxuICAgKiB0aGUgaW5wdXQgc3RpbGwgYXBwZWFycyBzbGlnaHRseSBkaW1tZWQgZXZlblxuICAgKiBpZiB3ZSBzZXQgb3BhY2l0eTogMS5cbiAgICovXG4gIGlmIChkaXNhYmxlZENsb25lZElucHV0KSB7XG4gICAgY2xvbmVkRWwuZGlzYWJsZWQgPSB0cnVlO1xuICB9XG4gIHBhcmVudEVsLmFwcGVuZENoaWxkKGNsb25lZEVsKTtcbiAgY2xvbmVNYXAuc2V0KGNvbXBvbmVudEVsLCBjbG9uZWRFbCk7XG4gIGNvbnN0IGRvYyA9IGNvbXBvbmVudEVsLm93bmVyRG9jdW1lbnQ7XG4gIGNvbnN0IHR4ID0gZG9jLmRpciA9PT0gJ3J0bCcgPyA5OTk5IDogLTk5OTk7XG4gIGNvbXBvbmVudEVsLnN0eWxlLnBvaW50ZXJFdmVudHMgPSAnbm9uZSc7XG4gIGlucHV0RWwuc3R5bGUudHJhbnNmb3JtID0gYHRyYW5zbGF0ZTNkKCR7dHh9cHgsJHtpbnB1dFJlbGF0aXZlWX1weCwwKSBzY2FsZSgwKWA7XG59O1xuY29uc3QgcmVtb3ZlQ2xvbmUgPSAoY29tcG9uZW50RWwsIGlucHV0RWwpID0+IHtcbiAgY29uc3QgY2xvbmUgPSBjbG9uZU1hcC5nZXQoY29tcG9uZW50RWwpO1xuICBpZiAoY2xvbmUpIHtcbiAgICBjbG9uZU1hcC5kZWxldGUoY29tcG9uZW50RWwpO1xuICAgIGNsb25lLnJlbW92ZSgpO1xuICB9XG4gIGNvbXBvbmVudEVsLnN0eWxlLnBvaW50ZXJFdmVudHMgPSAnJztcbiAgaW5wdXRFbC5zdHlsZS50cmFuc2Zvcm0gPSAnJztcbn07XG5cbmNvbnN0IGVuYWJsZUhpZGVDYXJldE9uU2Nyb2xsID0gKGNvbXBvbmVudEVsLCBpbnB1dEVsLCBzY3JvbGxFbCkgPT4ge1xuICBpZiAoIXNjcm9sbEVsIHx8ICFpbnB1dEVsKSB7XG4gICAgcmV0dXJuICgpID0+IHtcbiAgICAgIHJldHVybjtcbiAgICB9O1xuICB9XG4gIGNvbnN0IHNjcm9sbEhpZGVDYXJldCA9IChzaG91bGRIaWRlQ2FyZXQpID0+IHtcbiAgICBpZiAoaXNGb2N1c2VkKGlucHV0RWwpKSB7XG4gICAgICByZWxvY2F0ZUlucHV0KGNvbXBvbmVudEVsLCBpbnB1dEVsLCBzaG91bGRIaWRlQ2FyZXQpO1xuICAgIH1cbiAgfTtcbiAgY29uc3Qgb25CbHVyID0gKCkgPT4gcmVsb2NhdGVJbnB1dChjb21wb25lbnRFbCwgaW5wdXRFbCwgZmFsc2UpO1xuICBjb25zdCBoaWRlQ2FyZXQgPSAoKSA9PiBzY3JvbGxIaWRlQ2FyZXQodHJ1ZSk7XG4gIGNvbnN0IHNob3dDYXJldCA9ICgpID0+IHNjcm9sbEhpZGVDYXJldChmYWxzZSk7XG4gIGFkZEV2ZW50TGlzdGVuZXIoc2Nyb2xsRWwsICdpb25TY3JvbGxTdGFydCcsIGhpZGVDYXJldCk7XG4gIGFkZEV2ZW50TGlzdGVuZXIoc2Nyb2xsRWwsICdpb25TY3JvbGxFbmQnLCBzaG93Q2FyZXQpO1xuICBpbnB1dEVsLmFkZEV2ZW50TGlzdGVuZXIoJ2JsdXInLCBvbkJsdXIpO1xuICByZXR1cm4gKCkgPT4ge1xuICAgIHJlbW92ZUV2ZW50TGlzdGVuZXIoc2Nyb2xsRWwsICdpb25TY3JvbGxTdGFydCcsIGhpZGVDYXJldCk7XG4gICAgcmVtb3ZlRXZlbnRMaXN0ZW5lcihzY3JvbGxFbCwgJ2lvblNjcm9sbEVuZCcsIHNob3dDYXJldCk7XG4gICAgaW5wdXRFbC5hZGRFdmVudExpc3RlbmVyKCdpb25CbHVyJywgb25CbHVyKTtcbiAgfTtcbn07XG5cbmNvbnN0IFNLSVBfU0VMRUNUT1IgPSAnaW5wdXQsIHRleHRhcmVhLCBbbm8tYmx1cl0sIFtjb250ZW50ZWRpdGFibGVdJztcbmNvbnN0IGVuYWJsZUlucHV0Qmx1cnJpbmcgPSAoKSA9PiB7XG4gIGxldCBmb2N1c2VkID0gdHJ1ZTtcbiAgbGV0IGRpZFNjcm9sbCA9IGZhbHNlO1xuICBjb25zdCBkb2MgPSBkb2N1bWVudDtcbiAgY29uc3Qgb25TY3JvbGwgPSAoKSA9PiB7XG4gICAgZGlkU2Nyb2xsID0gdHJ1ZTtcbiAgfTtcbiAgY29uc3Qgb25Gb2N1c2luID0gKCkgPT4ge1xuICAgIGZvY3VzZWQgPSB0cnVlO1xuICB9O1xuICBjb25zdCBvblRvdWNoZW5kID0gKGV2KSA9PiB7XG4gICAgLy8gaWYgYXBwIGRpZCBzY3JvbGwgcmV0dXJuIGVhcmx5XG4gICAgaWYgKGRpZFNjcm9sbCkge1xuICAgICAgZGlkU2Nyb2xsID0gZmFsc2U7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IGFjdGl2ZSA9IGRvYy5hY3RpdmVFbGVtZW50O1xuICAgIGlmICghYWN0aXZlKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIC8vIG9ubHkgYmx1ciBpZiB0aGUgYWN0aXZlIGVsZW1lbnQgaXMgYSB0ZXh0LWlucHV0IG9yIGEgdGV4dGFyZWFcbiAgICBpZiAoYWN0aXZlLm1hdGNoZXMoU0tJUF9TRUxFQ1RPUikpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgLy8gaWYgdGhlIHNlbGVjdGVkIHRhcmdldCBpcyB0aGUgYWN0aXZlIGVsZW1lbnQsIGRvIG5vdCBibHVyXG4gICAgY29uc3QgdGFwcGVkID0gZXYudGFyZ2V0O1xuICAgIGlmICh0YXBwZWQgPT09IGFjdGl2ZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBpZiAodGFwcGVkLm1hdGNoZXMoU0tJUF9TRUxFQ1RPUikgfHwgdGFwcGVkLmNsb3Nlc3QoU0tJUF9TRUxFQ1RPUikpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZm9jdXNlZCA9IGZhbHNlO1xuICAgIC8vIFRPRE8gRlctMjc5NjogZmluZCBhIGJldHRlciB3YXksIHdoeSA1MG1zP1xuICAgIHNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgaWYgKCFmb2N1c2VkKSB7XG4gICAgICAgIGFjdGl2ZS5ibHVyKCk7XG4gICAgICB9XG4gICAgfSwgNTApO1xuICB9O1xuICBhZGRFdmVudExpc3RlbmVyKGRvYywgJ2lvblNjcm9sbFN0YXJ0Jywgb25TY3JvbGwpO1xuICBkb2MuYWRkRXZlbnRMaXN0ZW5lcignZm9jdXNpbicsIG9uRm9jdXNpbiwgdHJ1ZSk7XG4gIGRvYy5hZGRFdmVudExpc3RlbmVyKCd0b3VjaGVuZCcsIG9uVG91Y2hlbmQsIGZhbHNlKTtcbiAgcmV0dXJuICgpID0+IHtcbiAgICByZW1vdmVFdmVudExpc3RlbmVyKGRvYywgJ2lvblNjcm9sbFN0YXJ0Jywgb25TY3JvbGwsIHRydWUpO1xuICAgIGRvYy5yZW1vdmVFdmVudExpc3RlbmVyKCdmb2N1c2luJywgb25Gb2N1c2luLCB0cnVlKTtcbiAgICBkb2MucmVtb3ZlRXZlbnRMaXN0ZW5lcigndG91Y2hlbmQnLCBvblRvdWNoZW5kLCBmYWxzZSk7XG4gIH07XG59O1xuXG5jb25zdCBTQ1JPTExfQVNTSVNUX1NQRUVEID0gMC4zO1xuY29uc3QgZ2V0U2Nyb2xsRGF0YSA9IChjb21wb25lbnRFbCwgY29udGVudEVsLCBrZXlib2FyZEhlaWdodCkgPT4ge1xuICB2YXIgX2E7XG4gIGNvbnN0IGl0ZW1FbCA9IChfYSA9IGNvbXBvbmVudEVsLmNsb3Nlc3QoJ2lvbi1pdGVtLFtpb24taXRlbV0nKSkgIT09IG51bGwgJiYgX2EgIT09IHZvaWQgMCA/IF9hIDogY29tcG9uZW50RWw7XG4gIHJldHVybiBjYWxjU2Nyb2xsRGF0YShpdGVtRWwuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCksIGNvbnRlbnRFbC5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKSwga2V5Ym9hcmRIZWlnaHQsIGNvbXBvbmVudEVsLm93bmVyRG9jdW1lbnQuZGVmYXVsdFZpZXcuaW5uZXJIZWlnaHQgLy8gVE9ETyhGVy0yODMyKTogdHlwZVxuICApO1xufTtcbmNvbnN0IGNhbGNTY3JvbGxEYXRhID0gKGlucHV0UmVjdCwgY29udGVudFJlY3QsIGtleWJvYXJkSGVpZ2h0LCBwbGF0Zm9ybUhlaWdodCkgPT4ge1xuICAvLyBjb21wdXRlIGlucHV0J3MgWSB2YWx1ZXMgcmVsYXRpdmUgdG8gdGhlIGJvZHlcbiAgY29uc3QgaW5wdXRUb3AgPSBpbnB1dFJlY3QudG9wO1xuICBjb25zdCBpbnB1dEJvdHRvbSA9IGlucHV0UmVjdC5ib3R0b207XG4gIC8vIGNvbXB1dGUgdmlzaWJsZSBhcmVhXG4gIGNvbnN0IHZpc2libGVBcmVhVG9wID0gY29udGVudFJlY3QudG9wO1xuICBjb25zdCB2aXNpYmxlQXJlYUJvdHRvbSA9IE1hdGgubWluKGNvbnRlbnRSZWN0LmJvdHRvbSwgcGxhdGZvcm1IZWlnaHQgLSBrZXlib2FyZEhlaWdodCk7XG4gIC8vIGNvbXB1dGUgc2FmZSBhcmVhXG4gIGNvbnN0IHNhZmVBcmVhVG9wID0gdmlzaWJsZUFyZWFUb3AgKyAxNTtcbiAgY29uc3Qgc2FmZUFyZWFCb3R0b20gPSB2aXNpYmxlQXJlYUJvdHRvbSAqIDAuNzU7XG4gIC8vIGZpZ3VyZSBvdXQgaWYgZWFjaCBlZGdlIG9mIHRoZSBpbnB1dCBpcyB3aXRoaW4gdGhlIHNhZmUgYXJlYVxuICBjb25zdCBkaXN0YW5jZVRvQm90dG9tID0gc2FmZUFyZWFCb3R0b20gLSBpbnB1dEJvdHRvbTtcbiAgY29uc3QgZGlzdGFuY2VUb1RvcCA9IHNhZmVBcmVhVG9wIC0gaW5wdXRUb3A7XG4gIC8vIGRlc2lyZWRTY3JvbGxBbW91bnQgaXMgdGhlIG5lZ2F0ZWQgZGlzdGFuY2UgdG8gdGhlIHNhZmUgYXJlYSBhY2NvcmRpbmcgdG8gb3VyIGNhbGN1bGF0aW9ucy5cbiAgY29uc3QgZGVzaXJlZFNjcm9sbEFtb3VudCA9IE1hdGgucm91bmQoZGlzdGFuY2VUb0JvdHRvbSA8IDAgPyAtZGlzdGFuY2VUb0JvdHRvbSA6IGRpc3RhbmNlVG9Ub3AgPiAwID8gLWRpc3RhbmNlVG9Ub3AgOiAwKTtcbiAgLy8gb3VyIGNhbGN1bGF0aW9ucyBtYWtlIHNvbWUgYXNzdW1wdGlvbnMgdGhhdCBhcmVuJ3QgYWx3YXlzIHRydWUsIGxpa2UgdGhlIGtleWJvYXJkIGJlaW5nIGNsb3NlZCB3aGVuIGFuIGlucHV0XG4gIC8vIGdldHMgZm9jdXMsIHNvIG1ha2Ugc3VyZSB3ZSBkb24ndCBzY3JvbGwgdGhlIGlucHV0IGFib3ZlIHRoZSB2aXNpYmxlIGFyZWFcbiAgY29uc3Qgc2Nyb2xsQW1vdW50ID0gTWF0aC5taW4oZGVzaXJlZFNjcm9sbEFtb3VudCwgaW5wdXRUb3AgLSB2aXNpYmxlQXJlYVRvcCk7XG4gIGNvbnN0IGRpc3RhbmNlID0gTWF0aC5hYnMoc2Nyb2xsQW1vdW50KTtcbiAgY29uc3QgZHVyYXRpb24gPSBkaXN0YW5jZSAvIFNDUk9MTF9BU1NJU1RfU1BFRUQ7XG4gIGNvbnN0IHNjcm9sbER1cmF0aW9uID0gTWF0aC5taW4oNDAwLCBNYXRoLm1heCgxNTAsIGR1cmF0aW9uKSk7XG4gIHJldHVybiB7XG4gICAgc2Nyb2xsQW1vdW50LFxuICAgIHNjcm9sbER1cmF0aW9uLFxuICAgIHNjcm9sbFBhZGRpbmc6IGtleWJvYXJkSGVpZ2h0LFxuICAgIGlucHV0U2FmZVk6IC0oaW5wdXRUb3AgLSBzYWZlQXJlYVRvcCkgKyA0LFxuICB9O1xufTtcblxuY29uc3QgZW5hYmxlU2Nyb2xsQXNzaXN0ID0gKGNvbXBvbmVudEVsLCBpbnB1dEVsLCBjb250ZW50RWwsIGZvb3RlckVsLCBrZXlib2FyZEhlaWdodCwgZGlzYWJsZUNsb25lZElucHV0ID0gZmFsc2UpID0+IHtcbiAgbGV0IGNvb3JkO1xuICBjb25zdCB0b3VjaFN0YXJ0ID0gKGV2KSA9PiB7XG4gICAgY29vcmQgPSBwb2ludGVyQ29vcmQoZXYpO1xuICB9O1xuICBjb25zdCB0b3VjaEVuZCA9IChldikgPT4ge1xuICAgIC8vIGlucHV0IGNvdmVyIHRvdWNoZW5kL21vdXNldXBcbiAgICBpZiAoIWNvb3JkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIC8vIGdldCB3aGVyZSB0aGUgdG91Y2hlbmQvbW91c2V1cCBlbmRlZFxuICAgIGNvbnN0IGVuZENvb3JkID0gcG9pbnRlckNvb3JkKGV2KTtcbiAgICAvLyBmb2N1cyB0aGlzIGlucHV0IGlmIHRoZSBwb2ludGVyIGhhc24ndCBtb3ZlZCBYWCBwaXhlbHNcbiAgICAvLyBhbmQgdGhlIGlucHV0IGRvZXNuJ3QgYWxyZWFkeSBoYXZlIGZvY3VzXG4gICAgaWYgKCFoYXNQb2ludGVyTW92ZWQoNiwgY29vcmQsIGVuZENvb3JkKSAmJiAhaXNGb2N1c2VkKGlucHV0RWwpKSB7XG4gICAgICAvLyBiZWdpbiB0aGUgaW5wdXQgZm9jdXMgcHJvY2Vzc1xuICAgICAganNTZXRGb2N1cyhjb21wb25lbnRFbCwgaW5wdXRFbCwgY29udGVudEVsLCBmb290ZXJFbCwga2V5Ym9hcmRIZWlnaHQsIGRpc2FibGVDbG9uZWRJbnB1dCk7XG4gICAgfVxuICB9O1xuICBjb21wb25lbnRFbC5hZGRFdmVudExpc3RlbmVyKCd0b3VjaHN0YXJ0JywgdG91Y2hTdGFydCwgeyBjYXB0dXJlOiB0cnVlLCBwYXNzaXZlOiB0cnVlIH0pO1xuICBjb21wb25lbnRFbC5hZGRFdmVudExpc3RlbmVyKCd0b3VjaGVuZCcsIHRvdWNoRW5kLCB0cnVlKTtcbiAgcmV0dXJuICgpID0+IHtcbiAgICBjb21wb25lbnRFbC5yZW1vdmVFdmVudExpc3RlbmVyKCd0b3VjaHN0YXJ0JywgdG91Y2hTdGFydCwgdHJ1ZSk7XG4gICAgY29tcG9uZW50RWwucmVtb3ZlRXZlbnRMaXN0ZW5lcigndG91Y2hlbmQnLCB0b3VjaEVuZCwgdHJ1ZSk7XG4gIH07XG59O1xuY29uc3QganNTZXRGb2N1cyA9IGFzeW5jIChjb21wb25lbnRFbCwgaW5wdXRFbCwgY29udGVudEVsLCBmb290ZXJFbCwga2V5Ym9hcmRIZWlnaHQsIGRpc2FibGVDbG9uZWRJbnB1dCA9IGZhbHNlKSA9PiB7XG4gIGlmICghY29udGVudEVsICYmICFmb290ZXJFbCkge1xuICAgIHJldHVybjtcbiAgfVxuICBjb25zdCBzY3JvbGxEYXRhID0gZ2V0U2Nyb2xsRGF0YShjb21wb25lbnRFbCwgKGNvbnRlbnRFbCB8fCBmb290ZXJFbCksIGtleWJvYXJkSGVpZ2h0KTtcbiAgaWYgKGNvbnRlbnRFbCAmJiBNYXRoLmFicyhzY3JvbGxEYXRhLnNjcm9sbEFtb3VudCkgPCA0KSB7XG4gICAgLy8gdGhlIHRleHQgaW5wdXQgaXMgaW4gYSBzYWZlIHBvc2l0aW9uIHRoYXQgZG9lc24ndFxuICAgIC8vIHJlcXVpcmUgaXQgdG8gYmUgc2Nyb2xsZWQgaW50byB2aWV3LCBqdXN0IHNldCBmb2N1cyBub3dcbiAgICBpbnB1dEVsLmZvY3VzKCk7XG4gICAgcmV0dXJuO1xuICB9XG4gIC8vIHRlbXBvcmFyaWx5IG1vdmUgdGhlIGZvY3VzIHRvIHRoZSBmb2N1cyBob2xkZXIgc28gdGhlIGJyb3dzZXJcbiAgLy8gZG9lc24ndCBmcmVhayBvdXQgd2hpbGUgaXQncyB0cnlpbmcgdG8gZ2V0IHRoZSBpbnB1dCBpbiBwbGFjZVxuICAvLyBhdCB0aGlzIHBvaW50IHRoZSBuYXRpdmUgdGV4dCBpbnB1dCBzdGlsbCBkb2VzIG5vdCBoYXZlIGZvY3VzXG4gIHJlbG9jYXRlSW5wdXQoY29tcG9uZW50RWwsIGlucHV0RWwsIHRydWUsIHNjcm9sbERhdGEuaW5wdXRTYWZlWSwgZGlzYWJsZUNsb25lZElucHV0KTtcbiAgaW5wdXRFbC5mb2N1cygpO1xuICAvKipcbiAgICogUmVsb2NhdGluZy9Gb2N1c2luZyBpbnB1dCBjYXVzZXMgdGhlXG4gICAqIGNsaWNrIGV2ZW50IHRvIGJlIGNhbmNlbGxlZCwgc29cbiAgICogbWFudWFsbHkgZmlyZSBvbmUgaGVyZS5cbiAgICovXG4gIHJhZigoKSA9PiBjb21wb25lbnRFbC5jbGljaygpKTtcbiAgaWYgKHR5cGVvZiB3aW5kb3cgIT09ICd1bmRlZmluZWQnKSB7XG4gICAgbGV0IHNjcm9sbENvbnRlbnRUaW1lb3V0O1xuICAgIGNvbnN0IHNjcm9sbENvbnRlbnQgPSBhc3luYyAoKSA9PiB7XG4gICAgICAvLyBjbGVhbiB1cCBsaXN0ZW5lcnMgYW5kIHRpbWVvdXRzXG4gICAgICBpZiAoc2Nyb2xsQ29udGVudFRpbWVvdXQgIT09IHVuZGVmaW5lZCkge1xuICAgICAgICBjbGVhclRpbWVvdXQoc2Nyb2xsQ29udGVudFRpbWVvdXQpO1xuICAgICAgfVxuICAgICAgd2luZG93LnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2lvbktleWJvYXJkRGlkU2hvdycsIGRvdWJsZUtleWJvYXJkRXZlbnRMaXN0ZW5lcik7XG4gICAgICB3aW5kb3cucmVtb3ZlRXZlbnRMaXN0ZW5lcignaW9uS2V5Ym9hcmREaWRTaG93Jywgc2Nyb2xsQ29udGVudCk7XG4gICAgICAvLyBzY3JvbGwgdGhlIGlucHV0IGludG8gcGxhY2VcbiAgICAgIGlmIChjb250ZW50RWwpIHtcbiAgICAgICAgYXdhaXQgc2Nyb2xsQnlQb2ludChjb250ZW50RWwsIDAsIHNjcm9sbERhdGEuc2Nyb2xsQW1vdW50LCBzY3JvbGxEYXRhLnNjcm9sbER1cmF0aW9uKTtcbiAgICAgIH1cbiAgICAgIC8vIHRoZSBzY3JvbGwgdmlldyBpcyBpbiB0aGUgY29ycmVjdCBwb3NpdGlvbiBub3dcbiAgICAgIC8vIGdpdmUgdGhlIG5hdGl2ZSB0ZXh0IGlucHV0IGZvY3VzXG4gICAgICByZWxvY2F0ZUlucHV0KGNvbXBvbmVudEVsLCBpbnB1dEVsLCBmYWxzZSwgc2Nyb2xsRGF0YS5pbnB1dFNhZmVZKTtcbiAgICAgIC8vIGVuc3VyZSB0aGlzIGlzIHRoZSBmb2N1c2VkIGlucHV0XG4gICAgICBpbnB1dEVsLmZvY3VzKCk7XG4gICAgfTtcbiAgICBjb25zdCBkb3VibGVLZXlib2FyZEV2ZW50TGlzdGVuZXIgPSAoKSA9PiB7XG4gICAgICB3aW5kb3cucmVtb3ZlRXZlbnRMaXN0ZW5lcignaW9uS2V5Ym9hcmREaWRTaG93JywgZG91YmxlS2V5Ym9hcmRFdmVudExpc3RlbmVyKTtcbiAgICAgIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdpb25LZXlib2FyZERpZFNob3cnLCBzY3JvbGxDb250ZW50KTtcbiAgICB9O1xuICAgIGlmIChjb250ZW50RWwpIHtcbiAgICAgIGNvbnN0IHNjcm9sbEVsID0gYXdhaXQgZ2V0U2Nyb2xsRWxlbWVudChjb250ZW50RWwpO1xuICAgICAgLyoqXG4gICAgICAgKiBzY3JvbGxEYXRhIHdpbGwgb25seSBjb25zaWRlciB0aGUgYW1vdW50IHdlIG5lZWRcbiAgICAgICAqIHRvIHNjcm9sbCBpbiBvcmRlciB0byBwcm9wZXJseSBicmluZyB0aGUgaW5wdXRcbiAgICAgICAqIGludG8gdmlldy4gSXQgd2lsbCBub3QgY29uc2lkZXIgdGhlIGFtb3VudFxuICAgICAgICogd2UgY2FuIHNjcm9sbCBpbiB0aGUgY29udGVudCBlbGVtZW50LlxuICAgICAgICogQXMgYSByZXN1bHQsIHNjcm9sbERhdGEgbWF5IHJlcXVlc3QgYSBncmVhdGVyXG4gICAgICAgKiBzY3JvbGwgcG9zaXRpb24gdGhhbiBpcyBjdXJyZW50bHkgYXZhaWxhYmxlXG4gICAgICAgKiBpbiB0aGUgRE9NLiBJZiB0aGlzIGlzIHRoZSBjYXNlLCB3ZSBuZWVkIHRvXG4gICAgICAgKiB3YWl0IGZvciB0aGUgd2VidmlldyB0byByZXNpemUvdGhlIGtleWJvYXJkXG4gICAgICAgKiB0byBzaG93IGluIG9yZGVyIGZvciBhZGRpdGlvbmFsIHNjcm9sbFxuICAgICAgICogYmFuZHdpZHRoIHRvIGJlY29tZSBhdmFpbGFibGUuXG4gICAgICAgKi9cbiAgICAgIGNvbnN0IHRvdGFsU2Nyb2xsQW1vdW50ID0gc2Nyb2xsRWwuc2Nyb2xsSGVpZ2h0IC0gc2Nyb2xsRWwuY2xpZW50SGVpZ2h0O1xuICAgICAgaWYgKHNjcm9sbERhdGEuc2Nyb2xsQW1vdW50ID4gdG90YWxTY3JvbGxBbW91bnQgLSBzY3JvbGxFbC5zY3JvbGxUb3ApIHtcbiAgICAgICAgLyoqXG4gICAgICAgICAqIE9uIGlPUyBkZXZpY2VzLCB0aGUgc3lzdGVtIHdpbGwgc2hvdyBhIFwiUGFzc3dvcmRzXCIgYmFyIGFib3ZlIHRoZSBrZXlib2FyZFxuICAgICAgICAgKiBhZnRlciB0aGUgaW5pdGlhbCBrZXlib2FyZCBpcyBzaG93bi4gVGhpcyBwcmV2ZW50cyB0aGUgd2VidmlldyBmcm9tIHJlc2l6aW5nXG4gICAgICAgICAqIHVudGlsIHRoZSBcIlBhc3N3b3Jkc1wiIGJhciBpcyBzaG93biwgc28gd2UgbmVlZCB0byB3YWl0IGZvciB0aGF0IHRvIGhhcHBlbiBmaXJzdC5cbiAgICAgICAgICovXG4gICAgICAgIGlmIChpbnB1dEVsLnR5cGUgPT09ICdwYXNzd29yZCcpIHtcbiAgICAgICAgICAvLyBBZGQgNTBweCB0byBhY2NvdW50IGZvciB0aGUgXCJQYXNzd29yZHNcIiBiYXJcbiAgICAgICAgICBzY3JvbGxEYXRhLnNjcm9sbEFtb3VudCArPSA1MDtcbiAgICAgICAgICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcignaW9uS2V5Ym9hcmREaWRTaG93JywgZG91YmxlS2V5Ym9hcmRFdmVudExpc3RlbmVyKTtcbiAgICAgICAgfVxuICAgICAgICBlbHNlIHtcbiAgICAgICAgICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcignaW9uS2V5Ym9hcmREaWRTaG93Jywgc2Nyb2xsQ29udGVudCk7XG4gICAgICAgIH1cbiAgICAgICAgLyoqXG4gICAgICAgICAqIFRoaXMgc2hvdWxkIG9ubHkgZmlyZSBpbiAyIGluc3RhbmNlczpcbiAgICAgICAgICogMS4gVGhlIGFwcCBpcyB2ZXJ5IHNsb3cuXG4gICAgICAgICAqIDIuIFRoZSBhcHAgaXMgcnVubmluZyBpbiBhIGJyb3dzZXIgb24gYW4gb2xkIE9TXG4gICAgICAgICAqIHRoYXQgZG9lcyBub3Qgc3VwcG9ydCBJb25pYyBLZXlib2FyZCBFdmVudHNcbiAgICAgICAgICovXG4gICAgICAgIHNjcm9sbENvbnRlbnRUaW1lb3V0ID0gc2V0VGltZW91dChzY3JvbGxDb250ZW50LCAxMDAwKTtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgIH1cbiAgICBzY3JvbGxDb250ZW50KCk7XG4gIH1cbn07XG5jb25zdCBoYXNQb2ludGVyTW92ZWQgPSAodGhyZXNob2xkLCBzdGFydENvb3JkLCBlbmRDb29yZCkgPT4ge1xuICBpZiAoc3RhcnRDb29yZCAmJiBlbmRDb29yZCkge1xuICAgIGNvbnN0IGRlbHRhWCA9IHN0YXJ0Q29vcmQueCAtIGVuZENvb3JkLng7XG4gICAgY29uc3QgZGVsdGFZID0gc3RhcnRDb29yZC55IC0gZW5kQ29vcmQueTtcbiAgICBjb25zdCBkaXN0YW5jZSA9IGRlbHRhWCAqIGRlbHRhWCArIGRlbHRhWSAqIGRlbHRhWTtcbiAgICByZXR1cm4gZGlzdGFuY2UgPiB0aHJlc2hvbGQgKiB0aHJlc2hvbGQ7XG4gIH1cbiAgcmV0dXJuIGZhbHNlO1xufTtcblxuY29uc3QgUEFERElOR19USU1FUl9LRVkgPSAnJGlvblBhZGRpbmdUaW1lcic7XG5jb25zdCBlbmFibGVTY3JvbGxQYWRkaW5nID0gKGtleWJvYXJkSGVpZ2h0KSA9PiB7XG4gIGNvbnN0IGRvYyA9IGRvY3VtZW50O1xuICAvLyBUT0RPKEZXLTI4MzIpOiB0eXBlc1xuICBjb25zdCBvbkZvY3VzaW4gPSAoZXYpID0+IHtcbiAgICBzZXRTY3JvbGxQYWRkaW5nKGV2LnRhcmdldCwga2V5Ym9hcmRIZWlnaHQpO1xuICB9O1xuICBjb25zdCBvbkZvY3Vzb3V0ID0gKGV2KSA9PiB7XG4gICAgc2V0U2Nyb2xsUGFkZGluZyhldi50YXJnZXQsIDApO1xuICB9O1xuICBkb2MuYWRkRXZlbnRMaXN0ZW5lcignZm9jdXNpbicsIG9uRm9jdXNpbik7XG4gIGRvYy5hZGRFdmVudExpc3RlbmVyKCdmb2N1c291dCcsIG9uRm9jdXNvdXQpO1xuICByZXR1cm4gKCkgPT4ge1xuICAgIGRvYy5yZW1vdmVFdmVudExpc3RlbmVyKCdmb2N1c2luJywgb25Gb2N1c2luKTtcbiAgICBkb2MucmVtb3ZlRXZlbnRMaXN0ZW5lcignZm9jdXNvdXQnLCBvbkZvY3Vzb3V0KTtcbiAgfTtcbn07XG5jb25zdCBzZXRTY3JvbGxQYWRkaW5nID0gKGlucHV0LCBrZXlib2FyZEhlaWdodCkgPT4ge1xuICB2YXIgX2EsIF9iO1xuICBpZiAoaW5wdXQudGFnTmFtZSAhPT0gJ0lOUFVUJykge1xuICAgIHJldHVybjtcbiAgfVxuICBpZiAoaW5wdXQucGFyZW50RWxlbWVudCAmJiBpbnB1dC5wYXJlbnRFbGVtZW50LnRhZ05hbWUgPT09ICdJT04tSU5QVVQnKSB7XG4gICAgcmV0dXJuO1xuICB9XG4gIGlmICgoKF9iID0gKF9hID0gaW5wdXQucGFyZW50RWxlbWVudCkgPT09IG51bGwgfHwgX2EgPT09IHZvaWQgMCA/IHZvaWQgMCA6IF9hLnBhcmVudEVsZW1lbnQpID09PSBudWxsIHx8IF9iID09PSB2b2lkIDAgPyB2b2lkIDAgOiBfYi50YWdOYW1lKSA9PT0gJ0lPTi1TRUFSQ0hCQVInKSB7XG4gICAgcmV0dXJuO1xuICB9XG4gIGNvbnN0IGVsID0gZmluZENsb3Nlc3RJb25Db250ZW50KGlucHV0KTtcbiAgaWYgKGVsID09PSBudWxsKSB7XG4gICAgcmV0dXJuO1xuICB9XG4gIGNvbnN0IHRpbWVyID0gZWxbUEFERElOR19USU1FUl9LRVldO1xuICBpZiAodGltZXIpIHtcbiAgICBjbGVhclRpbWVvdXQodGltZXIpO1xuICB9XG4gIGlmIChrZXlib2FyZEhlaWdodCA+IDApIHtcbiAgICBlbC5zdHlsZS5zZXRQcm9wZXJ0eSgnLS1rZXlib2FyZC1vZmZzZXQnLCBgJHtrZXlib2FyZEhlaWdodH1weGApO1xuICB9XG4gIGVsc2Uge1xuICAgIGVsW1BBRERJTkdfVElNRVJfS0VZXSA9IHNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgZWwuc3R5bGUuc2V0UHJvcGVydHkoJy0ta2V5Ym9hcmQtb2Zmc2V0JywgJzBweCcpO1xuICAgIH0sIDEyMCk7XG4gIH1cbn07XG5cbmNvbnN0IElOUFVUX0JMVVJSSU5HID0gdHJ1ZTtcbmNvbnN0IFNDUk9MTF9QQURESU5HID0gdHJ1ZTtcbmNvbnN0IHN0YXJ0SW5wdXRTaGltcyA9IChjb25maWcsIHBsYXRmb3JtKSA9PiB7XG4gIGNvbnN0IGRvYyA9IGRvY3VtZW50O1xuICBjb25zdCBpc0lPUyA9IHBsYXRmb3JtID09PSAnaW9zJztcbiAgY29uc3QgaXNBbmRyb2lkID0gcGxhdGZvcm0gPT09ICdhbmRyb2lkJztcbiAgLyoqXG4gICAqIEhpZGUgQ2FyZXQgYW5kIElucHV0IEJsdXJyaW5nIGFyZSBuZWVkZWQgb24gaU9TLlxuICAgKiBTY3JvbGwgQXNzaXN0IGFuZCBTY3JvbGwgUGFkZGluZyBhcmUgbmVlZGVkIG9uIGlPUyBhbmQgQW5kcm9pZFxuICAgKiB3aXRoIENocm9tZSB3ZWIgYnJvd3NlciAobm90IENocm9tZSB3ZWJ2aWV3KS5cbiAgICovXG4gIGNvbnN0IGtleWJvYXJkSGVpZ2h0ID0gY29uZmlnLmdldE51bWJlcigna2V5Ym9hcmRIZWlnaHQnLCAyOTApO1xuICBjb25zdCBzY3JvbGxBc3Npc3QgPSBjb25maWcuZ2V0Qm9vbGVhbignc2Nyb2xsQXNzaXN0JywgdHJ1ZSk7XG4gIGNvbnN0IGhpZGVDYXJldCA9IGNvbmZpZy5nZXRCb29sZWFuKCdoaWRlQ2FyZXRPblNjcm9sbCcsIGlzSU9TKTtcbiAgY29uc3QgaW5wdXRCbHVycmluZyA9IGNvbmZpZy5nZXRCb29sZWFuKCdpbnB1dEJsdXJyaW5nJywgaXNJT1MpO1xuICBjb25zdCBzY3JvbGxQYWRkaW5nID0gY29uZmlnLmdldEJvb2xlYW4oJ3Njcm9sbFBhZGRpbmcnLCB0cnVlKTtcbiAgY29uc3QgaW5wdXRzID0gQXJyYXkuZnJvbShkb2MucXVlcnlTZWxlY3RvckFsbCgnaW9uLWlucHV0LCBpb24tdGV4dGFyZWEnKSk7XG4gIGNvbnN0IGhpZGVDYXJldE1hcCA9IG5ldyBXZWFrTWFwKCk7XG4gIGNvbnN0IHNjcm9sbEFzc2lzdE1hcCA9IG5ldyBXZWFrTWFwKCk7XG4gIGNvbnN0IHJlZ2lzdGVySW5wdXQgPSBhc3luYyAoY29tcG9uZW50RWwpID0+IHtcbiAgICBhd2FpdCBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gY29tcG9uZW50T25SZWFkeShjb21wb25lbnRFbCwgcmVzb2x2ZSkpO1xuICAgIGNvbnN0IGlucHV0Um9vdCA9IGNvbXBvbmVudEVsLnNoYWRvd1Jvb3QgfHwgY29tcG9uZW50RWw7XG4gICAgY29uc3QgaW5wdXRFbCA9IGlucHV0Um9vdC5xdWVyeVNlbGVjdG9yKCdpbnB1dCcpIHx8IGlucHV0Um9vdC5xdWVyeVNlbGVjdG9yKCd0ZXh0YXJlYScpO1xuICAgIGNvbnN0IHNjcm9sbEVsID0gZmluZENsb3Nlc3RJb25Db250ZW50KGNvbXBvbmVudEVsKTtcbiAgICBjb25zdCBmb290ZXJFbCA9ICFzY3JvbGxFbCA/IGNvbXBvbmVudEVsLmNsb3Nlc3QoJ2lvbi1mb290ZXInKSA6IG51bGw7XG4gICAgaWYgKCFpbnB1dEVsKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGlmICghIXNjcm9sbEVsICYmIGhpZGVDYXJldCAmJiAhaGlkZUNhcmV0TWFwLmhhcyhjb21wb25lbnRFbCkpIHtcbiAgICAgIGNvbnN0IHJtRm4gPSBlbmFibGVIaWRlQ2FyZXRPblNjcm9sbChjb21wb25lbnRFbCwgaW5wdXRFbCwgc2Nyb2xsRWwpO1xuICAgICAgaGlkZUNhcmV0TWFwLnNldChjb21wb25lbnRFbCwgcm1Gbik7XG4gICAgfVxuICAgIC8qKlxuICAgICAqIGRhdGUvZGF0ZXRpbWUtbG9jYWxlIGlucHV0cyBvbiBtb2JpbGUgZGV2aWNlcyBzaG93IGRhdGUgcGlja2VyXG4gICAgICogb3ZlcmxheXMgaW5zdGVhZCBvZiBrZXlib2FyZHMuIEFzIGEgcmVzdWx0LCBzY3JvbGwgYXNzaXN0IGlzXG4gICAgICogbm90IG5lZWRlZC4gVGhpcyBhbHNvIHdvcmtzIGFyb3VuZCBhIGJ1ZyBpbiBpT1MgPDE2IHdoZXJlXG4gICAgICogc2Nyb2xsIGFzc2lzdCBjYXVzZXMgdGhlIGJyb3dzZXIgdG8gbG9jayB1cC4gU2VlIEZXLTE5OTcuXG4gICAgICovXG4gICAgY29uc3QgaXNEYXRlSW5wdXQgPSBpbnB1dEVsLnR5cGUgPT09ICdkYXRlJyB8fCBpbnB1dEVsLnR5cGUgPT09ICdkYXRldGltZS1sb2NhbCc7XG4gICAgaWYgKCFpc0RhdGVJbnB1dCAmJlxuICAgICAgKCEhc2Nyb2xsRWwgfHwgISFmb290ZXJFbCkgJiZcbiAgICAgIHNjcm9sbEFzc2lzdCAmJlxuICAgICAgIXNjcm9sbEFzc2lzdE1hcC5oYXMoY29tcG9uZW50RWwpKSB7XG4gICAgICBjb25zdCBybUZuID0gZW5hYmxlU2Nyb2xsQXNzaXN0KGNvbXBvbmVudEVsLCBpbnB1dEVsLCBzY3JvbGxFbCwgZm9vdGVyRWwsIGtleWJvYXJkSGVpZ2h0LCBpc0FuZHJvaWQpO1xuICAgICAgc2Nyb2xsQXNzaXN0TWFwLnNldChjb21wb25lbnRFbCwgcm1Gbik7XG4gICAgfVxuICB9O1xuICBjb25zdCB1bnJlZ2lzdGVySW5wdXQgPSAoY29tcG9uZW50RWwpID0+IHtcbiAgICBpZiAoaGlkZUNhcmV0KSB7XG4gICAgICBjb25zdCBmbiA9IGhpZGVDYXJldE1hcC5nZXQoY29tcG9uZW50RWwpO1xuICAgICAgaWYgKGZuKSB7XG4gICAgICAgIGZuKCk7XG4gICAgICB9XG4gICAgICBoaWRlQ2FyZXRNYXAuZGVsZXRlKGNvbXBvbmVudEVsKTtcbiAgICB9XG4gICAgaWYgKHNjcm9sbEFzc2lzdCkge1xuICAgICAgY29uc3QgZm4gPSBzY3JvbGxBc3Npc3RNYXAuZ2V0KGNvbXBvbmVudEVsKTtcbiAgICAgIGlmIChmbikge1xuICAgICAgICBmbigpO1xuICAgICAgfVxuICAgICAgc2Nyb2xsQXNzaXN0TWFwLmRlbGV0ZShjb21wb25lbnRFbCk7XG4gICAgfVxuICB9O1xuICBpZiAoaW5wdXRCbHVycmluZyAmJiBJTlBVVF9CTFVSUklORykge1xuICAgIGVuYWJsZUlucHV0Qmx1cnJpbmcoKTtcbiAgfVxuICBpZiAoc2Nyb2xsUGFkZGluZyAmJiBTQ1JPTExfUEFERElORykge1xuICAgIGVuYWJsZVNjcm9sbFBhZGRpbmcoa2V5Ym9hcmRIZWlnaHQpO1xuICB9XG4gIC8vIElucHV0IG1pZ2h0IGJlIGFscmVhZHkgbG9hZGVkIGluIHRoZSBET00gYmVmb3JlIGlvbi1kZXZpY2UtaGFja3MgZGlkLlxuICAvLyBBdCB0aGlzIHBvaW50IHdlIG5lZWQgdG8gbG9vayBmb3IgYWxsIG9mIHRoZSBpbnB1dHMgbm90IHJlZ2lzdGVyZWQgeWV0XG4gIC8vIGFuZCByZWdpc3RlciB0aGVtLlxuICBmb3IgKGNvbnN0IGlucHV0IG9mIGlucHV0cykge1xuICAgIHJlZ2lzdGVySW5wdXQoaW5wdXQpO1xuICB9XG4gIC8vIFRPRE8oRlctMjgzMik6IHR5cGVzXG4gIGRvYy5hZGRFdmVudExpc3RlbmVyKCdpb25JbnB1dERpZExvYWQnLCAoKGV2KSA9PiB7XG4gICAgcmVnaXN0ZXJJbnB1dChldi5kZXRhaWwpO1xuICB9KSk7XG4gIGRvYy5hZGRFdmVudExpc3RlbmVyKCdpb25JbnB1dERpZFVubG9hZCcsICgoZXYpID0+IHtcbiAgICB1bnJlZ2lzdGVySW5wdXQoZXYuZGV0YWlsKTtcbiAgfSkpO1xufTtcblxuZXhwb3J0IHsgc3RhcnRJbnB1dFNoaW1zIH07XG4iXSwibmFtZXMiOlsiY2xvbmVNYXAiLCJXZWFrTWFwIiwicmVsb2NhdGVJbnB1dCIsImNvbXBvbmVudEVsIiwiaW5wdXRFbCIsInNob3VsZFJlbG9jYXRlIiwiaW5wdXRSZWxhdGl2ZVkiLCJkaXNhYmxlZENsb25lZElucHV0IiwiaGFzIiwiYWRkQ2xvbmUiLCJyZW1vdmVDbG9uZSIsImlzRm9jdXNlZCIsImlucHV0IiwiZ2V0Um9vdE5vZGUiLCJhY3RpdmVFbGVtZW50IiwicGFyZW50RWwiLCJwYXJlbnROb2RlIiwiY2xvbmVkRWwiLCJjbG9uZU5vZGUiLCJjbGFzc0xpc3QiLCJhZGQiLCJ0YWJJbmRleCIsImRpc2FibGVkIiwiYXBwZW5kQ2hpbGQiLCJzZXQiLCJkb2MiLCJvd25lckRvY3VtZW50IiwidHgiLCJkaXIiLCJzdHlsZSIsInBvaW50ZXJFdmVudHMiLCJ0cmFuc2Zvcm0iLCJjbG9uZSIsImdldCIsImRlbGV0ZSIsInJlbW92ZSIsImVuYWJsZUhpZGVDYXJldE9uU2Nyb2xsIiwic2Nyb2xsRWwiLCJzY3JvbGxIaWRlQ2FyZXQiLCJzaG91bGRIaWRlQ2FyZXQiLCJvbkJsdXIiLCJoaWRlQ2FyZXQiLCJzaG93Q2FyZXQiLCJhIiwiYWRkRXZlbnRMaXN0ZW5lciIsIlNLSVBfU0VMRUNUT1IiLCJlbmFibGVJbnB1dEJsdXJyaW5nIiwiZm9jdXNlZCIsImRpZFNjcm9sbCIsImRvY3VtZW50Iiwib25TY3JvbGwiLCJvbkZvY3VzaW4iLCJvblRvdWNoZW5kIiwiZXYiLCJhY3RpdmUiLCJtYXRjaGVzIiwidGFwcGVkIiwidGFyZ2V0IiwiY2xvc2VzdCIsInNldFRpbWVvdXQiLCJibHVyIiwicmVtb3ZlRXZlbnRMaXN0ZW5lciIsIlNDUk9MTF9BU1NJU1RfU1BFRUQiLCJnZXRTY3JvbGxEYXRhIiwiY29udGVudEVsIiwia2V5Ym9hcmRIZWlnaHQiLCJfYSIsIml0ZW1FbCIsImNhbGNTY3JvbGxEYXRhIiwiZ2V0Qm91bmRpbmdDbGllbnRSZWN0IiwiZGVmYXVsdFZpZXciLCJpbm5lckhlaWdodCIsImlucHV0UmVjdCIsImNvbnRlbnRSZWN0IiwicGxhdGZvcm1IZWlnaHQiLCJpbnB1dFRvcCIsInRvcCIsImlucHV0Qm90dG9tIiwiYm90dG9tIiwidmlzaWJsZUFyZWFUb3AiLCJ2aXNpYmxlQXJlYUJvdHRvbSIsIk1hdGgiLCJtaW4iLCJzYWZlQXJlYVRvcCIsInNhZmVBcmVhQm90dG9tIiwiZGlzdGFuY2VUb0JvdHRvbSIsImRpc3RhbmNlVG9Ub3AiLCJkZXNpcmVkU2Nyb2xsQW1vdW50Iiwicm91bmQiLCJzY3JvbGxBbW91bnQiLCJkaXN0YW5jZSIsImFicyIsImR1cmF0aW9uIiwic2Nyb2xsRHVyYXRpb24iLCJtYXgiLCJzY3JvbGxQYWRkaW5nIiwiaW5wdXRTYWZlWSIsImVuYWJsZVNjcm9sbEFzc2lzdCIsImZvb3RlckVsIiwiZGlzYWJsZUNsb25lZElucHV0IiwiY29vcmQiLCJ0b3VjaFN0YXJ0IiwicCIsInRvdWNoRW5kIiwiZW5kQ29vcmQiLCJoYXNQb2ludGVyTW92ZWQiLCJqc1NldEZvY3VzIiwiY2FwdHVyZSIsInBhc3NpdmUiLCJhc3luYyIsInNjcm9sbERhdGEiLCJmb2N1cyIsInIiLCJjbGljayIsIndpbmRvdyIsInNjcm9sbENvbnRlbnRUaW1lb3V0Iiwic2Nyb2xsQ29udGVudCIsInVuZGVmaW5lZCIsImNsZWFyVGltZW91dCIsImRvdWJsZUtleWJvYXJkRXZlbnRMaXN0ZW5lciIsImciLCJ0b3RhbFNjcm9sbEFtb3VudCIsInNjcm9sbEhlaWdodCIsImNsaWVudEhlaWdodCIsInNjcm9sbFRvcCIsInR5cGUiLCJ0aHJlc2hvbGQiLCJzdGFydENvb3JkIiwiZGVsdGFYIiwieCIsImRlbHRhWSIsInkiLCJQQURESU5HX1RJTUVSX0tFWSIsImVuYWJsZVNjcm9sbFBhZGRpbmciLCJzZXRTY3JvbGxQYWRkaW5nIiwib25Gb2N1c291dCIsIl9iIiwidGFnTmFtZSIsInBhcmVudEVsZW1lbnQiLCJlbCIsInRpbWVyIiwic2V0UHJvcGVydHkiLCJJTlBVVF9CTFVSUklORyIsIlNDUk9MTF9QQURESU5HIiwic3RhcnRJbnB1dFNoaW1zIiwiY29uZmlnIiwicGxhdGZvcm0iLCJpc0lPUyIsImlzQW5kcm9pZCIsImdldE51bWJlciIsInNjcm9sbEFzc2lzdCIsImdldEJvb2xlYW4iLCJpbnB1dEJsdXJyaW5nIiwiaW5wdXRzIiwiQXJyYXkiLCJmcm9tIiwicXVlcnlTZWxlY3RvckFsbCIsImhpZGVDYXJldE1hcCIsInNjcm9sbEFzc2lzdE1hcCIsInJlZ2lzdGVySW5wdXQiLCJQcm9taXNlIiwicmVzb2x2ZSIsImMiLCJpbnB1dFJvb3QiLCJzaGFkb3dSb290IiwicXVlcnlTZWxlY3RvciIsInJtRm4iLCJpc0RhdGVJbnB1dCIsInVucmVnaXN0ZXJJbnB1dCIsImZuIiwiZGV0YWlsIl0sInNvdXJjZVJvb3QiOiIifQ==