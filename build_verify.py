src = open('index.html').read()
inj = '''<style id="__vo">
#preloader{display:none!important}
#ayoh-fallback{opacity:1!important}
.reveal-up,.reveal-solid-up{opacity:1!important;transform:none!important}
.slide-in-right{transform:none!important}
.header-item{opacity:1!important;visibility:visible!important;animation:none!important}
.hand-up{opacity:1!important;transform:none!important}
html.lenis,body{height:auto!important}
#hero-spacer{height:0!important}
#hero-section{position:static!important;height:auto!important;min-height:40vh!important}
#about{height:auto!important;max-height:none!important;min-height:0!important;padding:30px 0!important}
#about .card-shadow-wrapper{min-height:160px!important}
</style></head>'''
open('__verify3.html', 'w').write(src.replace('</head>', inj, 1))
print('ok')
