import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class OntarioThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ontario_theme')

    @staticmethod
    def before_map(map):
        map.connect('user_news_feed', '/user/news_feed/{id}', controller='ckanext.ontario_theme.controller:CustomUserController',
                  action='news_feed', ckan_icon='clock-o')
        return map