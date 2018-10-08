import logging

from flask_restful import reqparse
from flask_restful import Resource

import pajbot.modules
import pajbot.utils
import pajbot.web.utils
from pajbot.managers.adminlog import AdminLogManager
from pajbot.models.autoresponse import AutoresponseManager
from pajbot.managers.db import DBManager
from pajbot.models.autoresponse import Autoresponse
from pajbot.models.sock import SocketClientManager

log = logging.getLogger(__name__)


class APIAutoresponseRemove(Resource):
    @pajbot.web.utils.requires_level(500)
    def get(self, autoresponse_id, **options):
        with DBManager.create_session_scope() as db_session:
            autoresponse = db_session.query(Autoresponse).filter_by(id=autoresponse_id).one_or_none()
            if autoresponse is None:
                return {'error': 'Invalid autoresponse ID'}, 404
            AdminLogManager.post('Autoresponse removed', options['user'], autoresponse.phrase)
            db_session.delete(autoresponse)
            db_session.delete(autoresponse.data)
            SocketClientManager.send('autoresponse.remove', {'id': autoresponse.id})
            return {'success': 'good job'}, 200


class APIAutoresponseToggle(Resource):
    def __init__(self):
        super().__init__()

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('new_state', required=True)

    @pajbot.web.utils.requires_level(500)
    def post(self, row_id, **options):
        args = self.post_parser.parse_args()

        try:
            new_state = int(args['new_state'])
        except (ValueError, KeyError):
            return {'error': 'Invalid `new_state` parameter.'}, 400

        with DBManager.create_session_scope() as db_session:
            row = db_session.query(Autoresponse).filter_by(id=row_id).one_or_none()

            if not row:
                return {
                        'error': 'Autoresponse with this ID not found'
                        }, 404

            row.enabled = True if new_state == 1 else False
            db_session.commit()
            payload = {
                    'id': row.id,
                    'new_state': row.enabled,
                    }
            AdminLogManager.post('Autoresponse toggled',
                    options['user'],
                    'Enabled' if row.enabled else 'Disabled',
                    row.phrase)
            SocketClientManager.send('autoresponse.update', payload)
            return {'success': 'successful toggle', 'new_state': new_state}


class APIAutoresponseTest(Resource):
    def __init__(self):
        super().__init__()

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('message', required=True)

    def post(self, **options):
        args = self.post_parser.parse_args()

        autoresponse_manager = AutoresponseManager(None).load()

        try:
            message = str(args['message'])
        except (ValueError, KeyError):
            return {'error': 'Invalid `message` parameter.'}, 400

        if len(message) == 0:
            return {'error': 'Parameter `message` cannot be empty.'}, 400

        ret = {
                'banned': False,
                'input_message': message
                }

        res = autoresponse_manager.check_message(message, None)

        if res is not False:
            ret['banned'] = True
            ret['autoresponse_data'] = res

        return ret


def init(api):
    api.add_resource(APIAutoresponseRemove, '/autoresponses/remove/<int:autoresponse_id>')
    api.add_resource(APIAutoresponseToggle, '/autoresponses/toggle/<int:row_id>')

    # Test a message against autoresponses
    api.add_resource(APIAutoresponseTest, '/autoresponses/test')
