from ckan.controllers.user import UserController
import ckan.lib.base as base
import ckan.model as model
from ckan.common import _, c, request, response
import ckan.logic as logic
import ckan.lib.helpers as h

get_action = logic.get_action
render = base.render

class CustomUserController(UserController):
    def news_feed(self, id, offset=0):
        '''Render this user's public news feed page.'''
        context = {'model': model, 'session': model.Session,
                   'user': c.user, 'auth_user_obj': c.userobj,
                   'for_view': True}
        data_dict = {'id': id, 'user_obj': c.userobj, 'offset': offset,
                     'include_num_followers': True}
        self._setup_template_variables(context, data_dict)

        q = request.params.get('q', u'')
        filter_type = request.params.get('type', u'')
        filter_id = request.params.get('name', u'')

        c.followee_list = get_action('followee_list')(
            context, {'id': c.userobj.id, 'q': q})
        c.dashboard_activity_stream_context = self._get_dashboard_context(
            filter_type, filter_id, q)
        c.dashboard_activity_stream = h.dashboard_activity_stream(
            c.userobj.id, filter_type, filter_id, offset
        )

        # Mark the user's new activities as old whenever they view their
        # dashboard page.
        get_action('dashboard_mark_activities_old')(context, {})

        return render('user/news_feed.html')