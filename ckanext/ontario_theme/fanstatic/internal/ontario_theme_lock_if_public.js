// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('lock_if_public', function ($) {  
  return {
    initialize: function () {
      var public_id = $(this.el).val()
      if (!!public_id) {
        $(".lock_if_public textarea, .lock_if_public input").prop("readonly","readonly")
        $(".lock_if_public select").attr("readonly","readonly")
      }
      return null
    }
  };
});