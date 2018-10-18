# encoding: utf-8

'''Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
'''
from ckantoolkit import h
# Overwrite of get_facet_title to change the facet title of "organization" to "ministry"
def get_facet_title(name):
    '''Deprecated in ckan 2.0 '''
    # if this is set in the config use this
    config_title = config.get('search.facets.%s.title' % name)
    if config_title:
        return config_title

    facet_titles = {'organization': _('Ministries'),
                    'groups': _('Groups'),
                    'tags': _('Tags'),
                    'res_format': _('Formats'),
                    'license': _('Licenses'), }
    return facet_titles.get(name, name.capitalize())

h.get_facet_title = get_facet_title