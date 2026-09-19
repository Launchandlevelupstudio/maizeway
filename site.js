(function(){
'use strict';
var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var yr=$('#year')||$('#yr'); if(yr) yr.textContent=new Date().getFullYear();
var items=$$('.menu>li'); function closeAll(){items.forEach(function(i){i.classList.remove('open');var a=$('a[aria-haspopup]',i);if(a)a.setAttribute('aria-expanded','false');});}
items.forEach(function(li){var dd=$('.dd',li);if(!dd)return;var a=$('a',li);
 function open(){closeAll();li.classList.add('open');a.setAttribute('aria-expanded','true');}
 li.addEventListener('mouseenter',open); li.addEventListener('focusin',open);
 a.addEventListener('click',function(e){if(window.matchMedia('(hover:none)').matches){e.preventDefault();var was=li.classList.contains('open');closeAll();if(!was)open();}});
});
var nav=$('#nav'); if(nav){nav.addEventListener('mouseleave',closeAll);nav.addEventListener('focusout',function(e){if(!nav.contains(e.relatedTarget))closeAll();});}
var mnav=$('#mnav'),burger=$('#burger'),mclose=$('#mclose'),lastFocus;
function trap(e){if(e.key!=='Tab')return;var f=$$('a,button,input,[tabindex]:not([tabindex="-1"])',mnav).filter(function(x){return x.offsetParent!==null});if(!f.length)return;var first=f[0],last=f[f.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}
function openMobile(){lastFocus=document.activeElement;mnav.classList.add('open');mnav.setAttribute('aria-hidden','false');burger.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';mclose.focus();document.addEventListener('keydown',trap);}
function closeMobile(){if(!mnav.classList.contains('open'))return;mnav.classList.remove('open');mnav.setAttribute('aria-hidden','true');burger.setAttribute('aria-expanded','false');document.body.style.overflow='';document.removeEventListener('keydown',trap);if(lastFocus)lastFocus.focus();}
if(burger){burger.addEventListener('click',openMobile);mclose.addEventListener('click',closeMobile);}
$$('[data-acc]').forEach(function(b){b.addEventListener('click',function(){var s=b.nextElementSibling,o=s.classList.toggle('open');b.setAttribute('aria-expanded',o);});});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeAll();closeMobile();}});
var bar=$('#stickybar'),hero=$('.hero');
if(bar&&hero&&'IntersectionObserver' in window){new IntersectionObserver(function(en){var on=!en[0].isIntersecting;bar.classList.toggle('on',on);bar.setAttribute('aria-hidden',!on);},{threshold:0}).observe(hero);}
$$('form[data-form]').forEach(function(f){
 var err=$('.err',f);
 function invalid(el,msg){el.setAttribute('aria-invalid','true');if(err){err.textContent=msg;err.classList.add('on');}}
 f.addEventListener('submit',function(e){e.preventDefault();
  $$('[aria-invalid]',f).forEach(function(x){x.removeAttribute('aria-invalid')});if(err){err.classList.remove('on');err.textContent='';}
  var bad=$$('[required]',f).filter(function(x){return !x.value.trim()});
  var em=$('[type=email]',f); if(em&&em.value&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value))bad.unshift(em);
  if(bad.length){invalid(bad[0],bad[0].type==='email'?'Please enter a valid email address.':'Please fill in the highlighted field.');bad[0].focus();return;}
  var btn=$('button[type=submit]',f),txt=btn.textContent;btn.disabled=true;btn.textContent='Sending…';
  fetch(f.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',headers:{'Accept':'application/json'},body:new FormData(f)})
   .then(function(r){if(!r.ok)throw 0;var nx=$('[name=_next]',f);if(nx&&nx.value&&nx.value.indexOf('[')<0){location.href=nx.value;return;}f.innerHTML='<p class="ok full">Thank you — your request is in. I will reply within one business day.</p>';})
   .catch(function(){btn.disabled=false;btn.textContent=txt;f.submit();});
 });
});
document.addEventListener('click',function(e){var t=e.target.closest('[data-track]');if(t&&window.gtag)gtag('event','cta_click',{label:t.getAttribute('data-track')});});
})();
