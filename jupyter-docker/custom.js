var importJQuery = document.createElement('script')
importJQuery.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
importJQuery.type = "text/javascript"
document.getElementsByTagName('head')[0].appendChild(importJQuery)

var logo = document.createElement('img')
    logo.setAttribute('id', 'logo')
    logo.setAttribute('src', 'https://github.com/fga-eps-mds/2019.1-PyLearner/raw/master/docs/img/Logo_text.jpg')

  var waitForRocketchat = function(selector, callback){
    if (jQuery(selector).length){
      callback()
    } else {
      setTimeout(function(){
        waitForRocketchat(selector, callback)
      }, 1000)
    }
  }

  define([
    'base/js/namespace',
    'base/js/events'
    ], function(events) {
      
     events.on('app_initialized.DashboardApp', function(w, d, s, u) {
      host = 'http://localhost:3000';
  
      w.RocketChat = function(c) { w.RocketChat._.push(c) }; w.RocketChat._ = []; w.RocketChat.url = u;
      var h = d.getElementsByTagName(s)[0], j = d.createElement(s);
      j.async = true; j.src = host + '/packages/rocketchat_livechat/assets/rocketchat-livechat.min.js?_=201702160944';
      h.parentNode.insertBefore(j, h);
      
      //return document.getElementsByClassName('rocketchat-widget')
      waitForRocketchat('.rocketchat-widget', function(){
        var container  = document.createElement('div')
        container.setAttribute('id', 'container')
        document.body.append(container)
        var notebookContainer = document.createElement('div')
        notebookContainer.setAttribute('id', 'notebook__container')
        
        var notebook = document.getElementById('site')
        var header = document.getElementById('header')
        notebook.setAttribute('class', 'display__side')
        var chat_window = document.getElementsByClassName('rocketchat-widget')
        container.append(logo)
        container.append(chat_window[0])
        container.append(notebookContainer)
        notebookContainer.append(header)
        notebookContainer.append(notebook)
      })
     }(window, document, 'script', 'http://localhost:3000' + '/livechat'))
  });


