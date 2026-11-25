/* molde.js — mecânica de abas do molde científico.

   A altura da barra NÃO é constante: depende de quantas abas existem, da largura da tela e do
   tamanho da fonte. Por isso ela é MEDIDA e publicada em --barra-h, e o CSS usa essa medida no
   scroll-margin-top. Enquanto a folga for número escrito à mão, o molde funciona até a peça
   passar de N abas — e a próxima sempre passa.

   Medido em 2026-11-20, viewport de 390px, na peça real:
     12 abas -> barra de 131px, scroll-margin fixo de 210px, folga de +24px
     19 abas -> barra de 223px, scroll-margin fixo de 210px, folga de -13px (título atrás da barra)
   É por isso que a folga não pode ser número: ela é a barra + respiro.
*/
(function(){
  var nav = document.querySelector('nav.tabs');
  if(!nav){ return; }
  var secs = Array.prototype.slice.call(document.querySelectorAll('section[role="tabpanel"]'));
  var botoes = Array.prototype.slice.call(nav.querySelectorAll('button[data-tab]'));
  var TABS = botoes.map(function(b){ return b.getAttribute('data-tab'); });

  function medirBarra(){
    var h = Math.ceil(nav.getBoundingClientRect().height);
    if(h > 0){ document.documentElement.style.setProperty('--barra-h', h + 'px'); }
    return h;
  }

  function abrir(id, push){
    var alvo = document.getElementById(id);
    if(!alvo){ return; }
    secs.forEach(function(s){ s.classList.toggle('active', s.id===id); });
    var ativa = null;
    botoes.forEach(function(b){
      var on = b.getAttribute('data-tab')===id;
      b.setAttribute('aria-selected', on ? 'true':'false');
      b.setAttribute('tabindex', on ? '0':'-1');
      if(on){ b.setAttribute('aria-current','page'); ativa = b; }
      else { b.removeAttribute('aria-current'); }
    });
    medirBarra();
    /* No celular a barra é uma linha que rola de lado: a aba ativa tem de ficar à vista,
       sem arrastar a página junto (block:'nearest'). */
    if(ativa && nav.scrollWidth > nav.clientWidth + 1){
      try { ativa.scrollIntoView({block:'nearest', inline:'center'}); } catch(e){}
    }
    if(push){
      /* replaceState em vez de location.hash: o hash deixaria o NAVEGADOR posicionar a seção
         respeitando o scroll-margin, e em seguida o scrollTo(0,0) desfaria — dois donos da
         mesma rolagem. Aqui há um dono só. O scroll-margin continua valendo para quem abre a
         peça já com #seção na URL, que é o caso que o navegador posiciona sozinho. */
      if(history.replaceState){ history.replaceState(null, '', '#' + id); }
      else { location.hash = id; }
    }
    requestAnimationFrame(function(){ window.scrollTo(0,0); });
  }

  nav.addEventListener('click', function(ev){
    var b = ev.target.closest ? ev.target.closest('button[data-tab]') : null;
    if(b){ abrir(b.getAttribute('data-tab'), true); }
  });
  document.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('a[href^="#"]') : null;
    if(a){
      var id = a.getAttribute('href').slice(1);
      if(document.getElementById(id)){ ev.preventDefault(); abrir(id, true); }
    }
  });
  window.addEventListener('hashchange', function(){
    abrir((location.hash||'').slice(1) || TABS[0], false);
  });
  window.addEventListener('pageshow', function(){
    abrir((location.hash||'').slice(1) || TABS[0], false);
  });

  /* a altura muda com resize, com rotação de tela, com fonte que carrega depois e com aba
     que muda de rótulo — medir uma vez no load não basta */
  window.addEventListener('resize', medirBarra);
  window.addEventListener('orientationchange', function(){ setTimeout(medirBarra, 60); });
  if(window.ResizeObserver){ new ResizeObserver(medirBarra).observe(nav); }
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(medirBarra); }

  function iniciar(){
    abrir((location.hash||'').slice(1) || TABS[0], false);
    medirBarra();
  }
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', iniciar);
  } else { iniciar(); }
})();
