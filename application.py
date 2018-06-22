from app import create_app

# # BEGIN CELERY
# from celery import Celery
#
#
# def make_celery(application):
#     # celery = Celery(application.import_name, broker=application.config['CELERY_BROKER_URL'])
#     celery = Celery("flask-es", broker=application.config['CELERY_BROKER_URL'])
#     celery.conf.update(application.config)
#     celery.conf.broker_transport_options = {'region': 'us-west-1'}
#     TaskBase = celery.Task
#     class ContextTask(TaskBase):
#         abstract = True
#         def __call__(self, *args, **kwargs):
#             with application.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#     celery.Task = ContextTask
#     return celery
# # DONE CELERY

application = create_app()

# celery = make_celery(application)
#
#
#
# @application.route('/test', methods=['GET', 'POST'])
# def take_test():
#     print("test1")
#     get_location.delay("")
#     print("test2")
#     return "test"
#
if __name__ == '__main__':
    application.debug = True
    application.run()

# app.run(host='0.0.0.0', port=5001, debug=True)
