"use strict";(self["webpackChunkHUAT"]=self["webpackChunkHUAT"]||[]).push([[990],{8990:(t,e,n)=>{n.r(e),n.d(e,{createSwipeBackGesture:()=>i});var r=n(6587),s=n(545),a=n(6515);
/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
const i=(t,e,n,i,o)=>{const c=t.ownerDocument.defaultView,h=(0,s.i)(t),u=t=>{const e=50,{startX:n}=t;return h?n>=c.innerWidth-e:n<=e},l=t=>h?-t.deltaX:t.deltaX,d=t=>h?-t.velocityX:t.velocityX,k=t=>u(t)&&e(),w=t=>{const e=l(t),n=e/c.innerWidth;i(n)},p=t=>{const e=l(t),n=c.innerWidth,s=e/n,a=d(t),i=n/2,h=a>=0&&(a>.2||e>i),u=h?1-s:s,k=u*n;let w=0;if(k>5){const t=k/Math.abs(a);w=Math.min(t,540)}o(h,s<=0?.01:(0,r.h)(0,s,.9999),w)};return(0,a.A)({el:t,gestureName:"goback-swipe",gesturePriority:40,threshold:10,canStart:k,onStart:n,onMove:w,onEnd:p})}}}]);
//# sourceMappingURL=990.7c8b4718.js.map