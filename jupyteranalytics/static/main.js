define([
  'base/js/utils',
  'services/config'
], function(utils, configmod) {

  var load_ipython_extension = function() {
    var base_url = utils.get_body_data("baseUrl");
    var configSection = new configmod.ConfigSection('common', {base_url: base_url});

    // FIXME NOTE from @yuvipanda:
    // This seems to fetch the config again but attaching to a configSection.loaded
    // does not seem to work. No resolution on how to make it work.
    configSection.load().then(function() {
      if ("GoogleAnalytics" in configSection.data) {
        var conf = configSection.data.GoogleAnalytics;
        if ("tracking_id" in conf && conf.tracking_id) {
          setup_google_analytics(conf.tracking_id);
        } else {
          console.log("Google Analytics is disabled - no Tracking ID available");
        }
      } else {
        console.log("Google Analytics is disabled - no common configuration");
      }
    });

  }

  var setup_google_analytics = function(tracking_id) {
    // Get the Google Analytics Global Site Tag Script
    var ga_url = "https://www.googletagmanager.com/gtag/js?" + tracking_id;
    (function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', ga_url, 'gtag');

    // Activate the Global Site Tag
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}

    gtag('js', new Date());
    gtag('config', tracking_id);
  }

  return {
    load_ipython_extension: load_ipython_extension,
  };
});