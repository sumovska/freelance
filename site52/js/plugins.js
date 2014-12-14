// Avoid `console` errors in browsers that lack a console.
(function () {
	var method;
	var noop = function () {
	};
	var methods = [
		'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
		'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
		'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
		'timeStamp', 'trace', 'warn'
	];
	var length = methods.length;
	var console = (window.console = window.console || {});

	while (length--) {
		method = methods[length];

		// Only stub undefined methods.
		if (!console[method]) {
			console[method] = noop;
		}
	}
}());

// Place any jQuery/helper plugins in here.

/* BxSlider v4.1.2 - Fully loaded, responsive container slider http://bxslider.com */
eval(function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('!4(t){8 e={},s={j:"10",2t:"",1r:!0,2Z:!1,1u:30,1P:1s,1q:0,1J:0,31:!1,32:!1,1v:!1,33:!1,1W:!1,2u:30,34:!1,35:!0,2v:"36",2w:!0,2d:37,38:!0,2x:37,39:!0,3a:!0,3b:!1,19:!0,3c:"3O",3d:" / ",2y:1s,2e:1s,2f:1s,6:!0,3e:"3P",3f:"3Q",2g:1s,2h:1s,1Q:!1,3g:"3R",3h:"3S",2z:!1,2A:1s,1l:!1,3i:3T,2B:!0,2i:"14",3j:!1,2C:0,1a:1,11:1,1w:0,1m:0,3k:4(){},3l:4(){},3m:4(){},3n:4(){},3o:4(){},3p:4(){}};t.3U.3q=4(n){F(0==G.K)17 G;F(G.K>1)17 G.1x(4(){t(G).3q(n)}),G;8 o={},r=G;e.1z=G;8 a=t(1R).1g(),l=t(1R).1A(),d=4(){o.2=t.3V({},s,n),o.2.1m=1X(o.2.1m),o.5=r.5(o.2.2t),o.5.K<o.2.1a&&(o.2.1a=o.5.K),o.5.K<o.2.11&&(o.2.11=o.5.K),o.2.31&&(o.2.1J=1n.3r(1n.3W()*o.5.K)),o.7={9:o.2.1J},o.1K=o.2.1a>1||o.2.11>1,o.1K&&(o.2.2v="3s"),o.2D=o.2.1a*o.2.1m+(o.2.1a-1)*o.2.1q,o.2E=o.2.11*o.2.1m+(o.2.11-1)*o.2.1q,o.1Y=!1,o.6={},o.1B=1s,o.1L="1h"==o.2.j?"1d":"1b",o.2j=o.2.35&&"1S"!=o.2.j&&4(){8 t=3X.3Y("15"),e=["3Z","40","41","42"];2k(8 i 43 e)F(1y 0!==t.1M[e[i]])17 o.1Z=e[i].44("45","").46(),o.1L="-"+o.1Z+"-47",!0;17!1}(),"1h"==o.2.j&&(o.2.11=o.2.1a),r.1C("1T",r.1U("1M")),r.5(o.2.2t).1x(4(){t(G).1C("1T",t(G).1U("1M"))}),c()},c=4(){r.48(\'<15 18="B-49"><15 18="B-J"></15></15>\'),o.J=r.2F(),o.2G=t(\'<15 18="B-4a" />\'),o.J.2H(o.2G),r.R({1g:"10"==o.2.j?2I*o.5.K+4b+"%":"1l",12:"2J"}),o.2j&&o.2.1P?r.R("-"+o.1Z+"-2K-3t-4",o.2.1P):o.2.1P||(o.2.1P="4c"),f(),o.J.R({1g:"2I%",4d:"4e",12:"2J"}),o.J.2F().R({4f:p()}),o.2.19||o.J.2F().R({4g:"0 1l 4h"}),o.5.R({"4i":"10"==o.2.j?"1b":"2L",4j:"2L",12:"2J"}),o.5.R("1g",u()),"10"==o.2.j&&o.2.1q>0&&o.5.R("4k",o.2.1q),"1h"==o.2.j&&o.2.1q>0&&o.5.R("4l",o.2.1q),"1S"==o.2.j&&(o.5.R({12:"4m",20:0,3u:"2L"}),o.5.Q(o.2.1J).R({20:o.2.2d,3u:"4n"})),o.6.1z=t(\'<15 18="B-6" />\'),o.2.32&&P(),o.7.1o=o.2.1J==x()-1,o.2.34&&r.4o();8 e=o.5.Q(o.2.1J);"3s"==o.2.2v&&(e=o.5),o.2.1v?o.2.19=!1:(o.2.19&&T(),o.2.6&&C(),o.2.1l&&o.2.1Q&&E(),(o.2.6||o.2.1Q||o.2.19)&&o.J.4p(o.6.1z)),g(e,h)},g=4(e,i){8 s=e.1t("2M, 3v").K;F(0==s)17 i(),1y 0;8 n=0;e.1t("2M, 3v").1x(4(){t(G).4q("3w",4(){++n==s&&i()}).1x(4(){G.4r&&t(G).3w()})})},h=4(){F(o.2.1r&&"1S"!=o.2.j&&!o.2.1v){8 e="1h"==o.2.j?o.2.1a:o.2.11,i=o.5.3x(0,e).1i().1c("B-1i"),s=o.5.3x(-e).1i().1c("B-1i");r.1j(i).2H(s)}o.2G.1D(),S(),"1h"==o.2.j&&(o.2.1W=!0),o.J.1A(v()),r.2N(),o.2.3k(o.7.9),o.2O=!0,o.2.2w&&t(1R).1E("3y",Z),o.2.1l&&o.2.2B&&H(),o.2.1v&&L(),o.2.19&&q(o.2.1J),o.2.6&&W(),o.2.38&&!o.2.1v&&O()},v=4(){8 e=0,s=t();F("1h"==o.2.j||o.2.1W)F(o.1K){8 n=1==o.2.1w?o.7.9:o.7.9*m();2k(s=o.5.Q(n),i=1;i<=o.2.11-1;i++)s=n+i>=o.5.K?s.2P(o.5.Q(i-1)):s.2P(o.5.Q(n+i))}13 s=o.5.Q(o.7.9);13 s=o.5;17"1h"==o.2.j?(s.1x(4(){e+=t(G).2Q()}),o.2.1q>0&&(e+=o.2.1q*(o.2.1a-1))):e=1n.4s.4t(1n,s.4u(4(){17 t(G).2Q(!1)}).4v()),e},p=4(){8 t="2I%";17 o.2.1m>0&&(t="10"==o.2.j?o.2.11*o.2.1m+(o.2.11-1)*o.2.1q:o.2.1m),t},u=4(){8 t=o.2.1m,e=o.J.1g();17 0==o.2.1m||o.2.1m>e&&!o.1K||"1h"==o.2.j?t=e:o.2.11>1&&"10"==o.2.j&&(e>o.2E||e<o.2D&&(t=(e-o.2.1q*(o.2.1a-1))/o.2.1a)),t},f=4(){8 t=1;F("10"==o.2.j&&o.2.1m>0)F(o.J.1g()<o.2D)t=o.2.1a;13 F(o.J.1g()>o.2E)t=o.2.11;13{8 e=o.5.21().1g();t=1n.3r(o.J.1g()/e)}13"1h"==o.2.j&&(t=o.2.1a);17 t},x=4(){8 t=0;F(o.2.1w>0)F(o.2.1r)t=o.5.K/m();13 2k(8 e=0,i=0;e<o.5.K;)++t,e=i+f(),i+=o.2.1w<=f()?o.2.1w:f();13 t=1n.3z(o.5.K/f());17 t},m=4(){17 o.2.1w>0&&o.2.1w<=f()?o.2.1w:f()},S=4(){F(o.5.K>o.2.11&&o.7.1o&&!o.2.1r){F("10"==o.2.j){8 t=o.5.1o(),e=t.12();b(-(e.1b-(o.J.1g()-t.1g())),"1e",0)}13 F("1h"==o.2.j){8 i=o.5.K-o.2.1a,e=o.5.Q(i).12();b(-e.1d,"1e",0)}}13{8 e=o.5.Q(o.7.9*m()).12();o.7.9==x()-1&&(o.7.1o=!0),1y 0!=e&&("10"==o.2.j?b(-e.1b,"1e",0):"1h"==o.2.j&&b(-e.1d,"1e",0))}},b=4(t,e,i,s){F(o.2j){8 n="1h"==o.2.j?"3A(0, "+t+"3B, 0)":"3A("+t+"3B, 0, 0)";r.R("-"+o.1Z+"-2K-4w",i/4x+"s"),"22"==e?(r.R(o.1L,n),r.1E("2l 2m 2n 2o",4(){r.23("2l 2m 2n 2o"),D()})):"1e"==e?r.R(o.1L,n):"1v"==e&&(r.R("-"+o.1Z+"-2K-3t-4","3C"),r.R(o.1L,n),r.1E("2l 2m 2n 2o",4(){r.23("2l 2m 2n 2o"),b(s.2R,"1e",0),N()}))}13{8 a={};a[o.1L]=t,"22"==e?r.2p(a,i,o.2.1P,4(){D()}):"1e"==e?r.R(o.1L,t):"1v"==e&&r.2p(a,1u,"3C",4(){b(s.2R,"1e",0),N()})}},w=4(){2k(8 e="",i=x(),s=0;i>s;s++){8 n="";o.2.2e&&t.4y(o.2.2e)?(n=o.2.2e(s),o.1k.1c("B-4z-19")):(n=s+1,o.1k.1c("B-4A-19")),e+=\'<15 18="B-19-2S"><a 24="" 1C-22-9="\'+s+\'" 18="B-19-4B">\'+n+"</a></15>"}o.1k.25(e)},T=4(){o.2.2f?o.1k=t(o.2.2f):(o.1k=t(\'<15 18="B-19" />\'),o.2.2y?t(o.2.2y).25(o.1k):o.6.1z.1c("B-2T-19").1j(o.1k),w()),o.1k.2U("26","a",I)},C=4(){o.6.14=t(\'<a 18="B-14" 24="">\'+o.2.3e+"</a>"),o.6.1f=t(\'<a 18="B-1f" 24="">\'+o.2.3f+"</a>"),o.6.14.1E("26",y),o.6.1f.1E("26",z),o.2.2g&&t(o.2.2g).1j(o.6.14),o.2.2h&&t(o.2.2h).1j(o.6.1f),o.2.2g||o.2.2h||(o.6.2V=t(\'<15 18="B-6-3D" />\'),o.6.2V.1j(o.6.1f).1j(o.6.14),o.6.1z.1c("B-2T-6-3D").1j(o.6.2V))},E=4(){o.6.16=t(\'<15 18="B-6-1l-2S"><a 18="B-16" 24="">\'+o.2.3g+"</a></15>"),o.6.1N=t(\'<15 18="B-6-1l-2S"><a 18="B-1N" 24="">\'+o.2.3h+"</a></15>"),o.6.1p=t(\'<15 18="B-6-1l" />\'),o.6.1p.2U("26",".B-16",k),o.6.1p.2U("26",".B-1N",M),o.2.2z?o.6.1p.1j(o.6.16):o.6.1p.1j(o.6.16).1j(o.6.1N),o.2.2A?t(o.2.2A).25(o.6.1p):o.6.1z.1c("B-2T-6-1l").1j(o.6.1p),A(o.2.2B?"1N":"16")},P=4(){o.5.1x(4(){8 e=t(G).1t("2M:21").1U("4C");1y 0!=e&&(""+e).K&&t(G).1j(\'<15 18="B-3E"><3F>\'+e+"</3F></15>")})},y=4(t){o.2.1l&&r.1F(),r.27(),t.1G()},z=4(t){o.2.1l&&r.1F(),r.28(),t.1G()},k=4(t){r.29(),t.1G()},M=4(t){r.1F(),t.1G()},I=4(e){o.2.1l&&r.1F();8 i=t(e.4D),s=1X(i.1U("1C-22-9"));s!=o.7.9&&r.2q(s),e.1G()},q=4(e){8 i=o.5.K;17"4E"==o.2.3c?(o.2.11>1&&(i=1n.3z(o.5.K/o.2.11)),o.1k.25(e+1+o.2.3d+i),1y 0):(o.1k.1t("a").1V("7"),o.1k.1x(4(i,s){t(s).1t("a").Q(e).1c("7")}),1y 0)},D=4(){F(o.2.1r){8 t="";0==o.7.9?t=o.5.Q(0).12():o.7.9==x()-1&&o.1K?t=o.5.Q((x()-1)*m()).12():o.7.9==o.5.K-1&&(t=o.5.Q(o.5.K-1).12()),t&&("10"==o.2.j?b(-t.1b,"1e",0):"1h"==o.2.j&&b(-t.1d,"1e",0))}o.1Y=!1,o.2.3m(o.5.Q(o.7.9),o.2a,o.7.9)},A=4(t){o.2.2z?o.6.1p.25(o.6[t]):(o.6.1p.1t("a").1V("7"),o.6.1p.1t("a:4F(.B-"+t+")").1c("7"))},W=4(){1==x()?(o.6.1f.1c("1H"),o.6.14.1c("1H")):!o.2.1r&&o.2.2Z&&(0==o.7.9?(o.6.1f.1c("1H"),o.6.14.1V("1H")):o.7.9==x()-1?(o.6.14.1c("1H"),o.6.1f.1V("1H")):(o.6.1f.1V("1H"),o.6.14.1V("1H")))},H=4(){o.2.2C>0?4G(r.29,o.2.2C):r.29(),o.2.3j&&r.3G(4(){o.1B&&(r.1F(!0),o.2W=!0)},4(){o.2W&&(r.29(!0),o.2W=1s)})},L=4(){8 e=0;F("14"==o.2.2i)r.1j(o.5.1i().1c("B-1i"));13{r.2H(o.5.1i().1c("B-1i"));8 i=o.5.21().12();e="10"==o.2.j?-i.1b:-i.1d}b(e,"1e",0),o.2.19=!1,o.2.6=!1,o.2.1Q=!1,o.2.33&&!o.2j&&o.J.3G(4(){r.1N()},4(){8 e=0;o.5.1x(4(){e+="10"==o.2.j?t(G).2X(!0):t(G).2Q(!0)});8 i=o.2.1u/e,s="10"==o.2.j?"1b":"1d",n=i*(e-1n.2b(1X(r.R(s))));N(n)}),N()},N=4(t){1u=t?t:o.2.1u;8 e={1b:0,1d:0},i={1b:0,1d:0};"14"==o.2.2i?e=r.1t(".B-1i").21().12():i=o.5.21().12();8 s="10"==o.2.j?-e.1b:-e.1d,n="10"==o.2.j?-i.1b:-i.1d,a={2R:n};b(s,"1v",1u,a)},O=4(){o.U={16:{x:0,y:0},1O:{x:0,y:0}},o.J.1E("4H",X)},X=4(t){F(o.1Y)t.1G();13{o.U.2c=r.12();8 e=t.2Y;o.U.16.x=e.1I[0].2r,o.U.16.y=e.1I[0].2s,o.J.1E("3H",Y),o.J.1E("3I",V)}},Y=4(t){8 e=t.2Y,i=1n.2b(e.1I[0].2r-o.U.16.x),s=1n.2b(e.1I[0].2s-o.U.16.y);F(3*i>s&&o.2.3a?t.1G():3*s>i&&o.2.3b&&t.1G(),"1S"!=o.2.j&&o.2.39){8 n=0;F("10"==o.2.j){8 r=e.1I[0].2r-o.U.16.x;n=o.U.2c.1b+r}13{8 r=e.1I[0].2s-o.U.16.y;n=o.U.2c.1d+r}b(n,"1e",0)}},V=4(t){o.J.23("3H",Y);8 e=t.2Y,i=0;F(o.U.1O.x=e.1I[0].2r,o.U.1O.y=e.1I[0].2s,"1S"==o.2.j){8 s=1n.2b(o.U.16.x-o.U.1O.x);s>=o.2.2x&&(o.U.16.x>o.U.1O.x?r.27():r.28(),r.1F())}13{8 s=0;"10"==o.2.j?(s=o.U.1O.x-o.U.16.x,i=o.U.2c.1b):(s=o.U.1O.y-o.U.16.y,i=o.U.2c.1d),!o.2.1r&&(0==o.7.9&&s>0||o.7.1o&&0>s)?b(i,"1e",3J):1n.2b(s)>=o.2.2x?(0>s?r.27():r.28(),r.1F()):b(i,"1e",3J)}o.J.23("3I",V)},Z=4(){8 e=t(1R).1g(),i=t(1R).1A();(a!=e||l!=i)&&(a=e,l=i,r.2N(),o.2.3p.4I(r,o.7.9))};17 r.2q=4(e,i){F(!o.1Y&&o.7.9!=e)F(o.1Y=!0,o.2a=o.7.9,o.7.9=0>e?x()-1:e>=x()?0:e,o.2.3l(o.5.Q(o.7.9),o.2a,o.7.9),"14"==i?o.2.3n(o.5.Q(o.7.9),o.2a,o.7.9):"1f"==i&&o.2.3o(o.5.Q(o.7.9),o.2a,o.7.9),o.7.1o=o.7.9>=x()-1,o.2.19&&q(o.7.9),o.2.6&&W(),"1S"==o.2.j)o.2.1W&&o.J.1A()!=v()&&o.J.2p({1A:v()},o.2.2u),o.5.4J(":36").4K(o.2.1u).R({20:0}),o.5.Q(o.7.9).R("20",o.2.2d+1).4L(o.2.1u,4(){t(G).R("20",o.2.2d),D()});13{o.2.1W&&o.J.1A()!=v()&&o.J.2p({1A:v()},o.2.2u);8 s=0,n={1b:0,1d:0};F(!o.2.1r&&o.1K&&o.7.1o)F("10"==o.2.j){8 a=o.5.Q(o.5.K-1);n=a.12(),s=o.J.1g()-a.2X()}13{8 l=o.5.K-o.2.1a;n=o.5.Q(l).12()}13 F(o.1K&&o.7.1o&&"1f"==i){8 d=1==o.2.1w?o.2.11-m():(x()-1)*m()-(o.5.K-o.2.11),a=r.5(".B-1i").Q(d);n=a.12()}13 F("14"==i&&0==o.7.9)n=r.1t("> .B-1i").Q(o.2.11).12(),o.7.1o=!1;13 F(e>=0){8 c=e*m();n=o.5.Q(c).12()}F("4M"!=4N n){8 g="10"==o.2.j?-(n.1b-s):-n.1d;b(g,"22",o.2.1u)}}},r.27=4(){F(o.2.1r||!o.7.1o){8 t=1X(o.7.9)+1;r.2q(t,"14")}},r.28=4(){F(o.2.1r||0!=o.7.9){8 t=1X(o.7.9)-1;r.2q(t,"1f")}},r.29=4(t){o.1B||(o.1B=4O(4(){"14"==o.2.2i?r.27():r.28()},o.2.3i),o.2.1Q&&1!=t&&A("1N"))},r.1F=4(t){o.1B&&(3K(o.1B),o.1B=1s,o.2.1Q&&1!=t&&A("16"))},r.4P=4(){17 o.7.9},r.4Q=4(){17 o.5.Q(o.7.9)},r.4R=4(){17 o.5.K},r.2N=4(){o.5.2P(r.1t(".B-1i")).2X(u()),o.J.R("1A",v()),o.2.1v||S(),o.7.1o&&(o.7.9=x()-1),o.7.9>=x()&&(o.7.1o=!0),o.2.19&&!o.2.2f&&(w(),q(o.7.9))},r.3L=4(){o.2O&&(o.2O=!1,t(".B-1i",G).1D(),o.5.1x(4(){1y 0!=t(G).1C("1T")?t(G).1U("1M",t(G).1C("1T")):t(G).3M("1M")}),1y 0!=t(G).1C("1T")?G.1U("1M",t(G).1C("1T")):t(G).3M("1M"),t(G).3N().3N(),o.6.1z&&o.6.1z.1D(),o.6.14&&o.6.14.1D(),o.6.1f&&o.6.1f.1D(),o.1k&&o.2.6&&o.1k.1D(),t(".B-3E",G).1D(),o.6.1p&&o.6.1p.1D(),3K(o.1B),o.2.2w&&t(1R).23("3y",Z))},r.4S=4(t){1y 0!=t&&(n=t),r.3L(),d()},d(),G}}(4T);',62,304,'||settings||function|children|controls|active|var|index||||||||||mode||||||||||||||||||bx||||if|this|||viewport|length||||||eq|css|||touch||||||horizontal|maxSlides|position|else|next|div|start|return|class|pager|minSlides|left|addClass|top|reset|prev|width|vertical|clone|append|pagerEl|auto|slideWidth|Math|last|autoEl|slideMargin|infiniteLoop|null|find|speed|ticker|moveSlides|each|void|el|height|interval|data|remove|bind|stopAuto|preventDefault|disabled|changedTouches|startSlide|carousel|animProp|style|stop|end|easing|autoControls|window|fade|origStyle|attr|removeClass|adaptiveHeight|parseInt|working|cssPrefix|zIndex|first|slide|unbind|href|html|click|goToNextSlide|goToPrevSlide|startAuto|oldIndex|abs|originalPos|slideZIndex|buildPager|pagerCustom|nextSelector|prevSelector|autoDirection|usingCSS|for|transitionend|webkitTransitionEnd|oTransitionEnd|MSTransitionEnd|animate|goToSlide|pageX|pageY|slideSelector|adaptiveHeightSpeed|preloadImages|responsive|swipeThreshold|pagerSelector|autoControlsCombine|autoControlsSelector|autoStart|autoDelay|minThreshold|maxThreshold|parent|loader|prepend|100|relative|transition|none|img|redrawSlider|initialized|add|outerHeight|resetValue|item|has|on|directionEl|autoPaused|outerWidth|originalEvent|hideControlOnEnd|500|randomStart|captions|tickerHover|video|useCSS|visible|50|touchEnabled|oneToOneTouch|preventDefaultSwipeX|preventDefaultSwipeY|pagerType|pagerShortSeparator|nextText|prevText|startText|stopText|pause|autoHover|onSliderLoad|onSlideBefore|onSlideAfter|onSlideNext|onSlidePrev|onSliderResize|bxSlider|floor|all|timing|display|iframe|load|slice|resize|ceil|translate3d|px|linear|direction|caption|span|hover|touchmove|touchend|200|clearInterval|destroySlider|removeAttr|unwrap|full|Next|Prev|Start|Stop|4e3|fn|extend|random|document|createElement|WebkitPerspective|MozPerspective|OPerspective|msPerspective|in|replace|Perspective|toLowerCase|transform|wrap|wrapper|loading|215|swing|overflow|hidden|maxWidth|margin|0px|float|listStyle|marginRight|marginBottom|absolute|block|fitVids|after|one|complete|max|apply|map|get|duration|1e3|isFunction|custom|default|link|title|currentTarget|short|not|setTimeout|touchstart|call|filter|fadeOut|fadeIn|undefined|typeof|setInterval|getCurrentSlide|getCurrentSlideElement|getSlideCount|reloadSlider|jQuery'.split('|'),0,{}));