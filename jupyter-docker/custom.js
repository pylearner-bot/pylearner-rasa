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
   }(window, document, 'script', 'http://localhost:3000' + '/livechat')
 )});

 var container  = document.createElement('div')
 container.setAttribute('id', 'container')
 document.body.append(container)
 var rocketchat = document.getElementsByClassName('rocketchat-widget')
 var notebook = document.getElementById('site')
 notebook.setAttribute('class', 'display__side')

 container.append(rocketchat)
 container.append(notebook)

var versionUpdate = (new Date()).getTime()
var script = document.createElement('script')
script.type = 'text/javascript'
script.src = '.jupyter/custom.js?v=' + versionUpdate
document.body.append(script)
  