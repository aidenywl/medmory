from huey.contrib.djhuey import db_periodic_task, db_task, periodic_task, task
import datetime
from .twilio_api import send_message

# @db_task()
# def do_some_queries():
# This task executes queries. Once the task finishes, the connection
# will be closed.


# @db_periodic_task(crontab(minute='*/5'))
# def every_five_mins():
# This is a periodic task that executes queries.

@task()
def test_task(message):
    print('message: ' + str(datetime.datetime.utcnow()) + '; ' + message)
    return


@task()
def send_reminder(patient, message):
    print('send reminder: ' + str(datetime.datetime.utcnow()) +
          '; ' + patient['phone_number'] + '; ' + message)
    send_message(patient['phone_number'], message)
    # schedule check
    check_reminder.schedule(args=(patient))
    return


@db_task()
def check_reminder(phone_number, message):
    # print('check reminder: ' + str(datetime.datetime.utcnow()) +
    #       '; ' + patient['phone_number'] + '; ' + message)
    # send_message(phone_number, message)
    # completed = False
    # if not completed:
    #     send_reminder()
    # else:
    #         # complete
    return

# @periodic_task(crontab(minute='*/5'))
# def every_five_mins():
#     print('Every five minutes this will be printed by the consumer')
