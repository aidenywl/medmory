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
def send_reminder(patient, reminder_id, message):
    # print('send reminder: ' + str(datetime.datetime.now()) + '; ' + patient['phone_number'] + '; ' + message)
    send_message(patient['phone_number'], message)
    # schedule check in 5 min
    now = datetime.datetime.now()
    scheduled_time = now + (datetime.timedelta(seconds=300))
    check_reminder.schedule(
        args=(patient, reminder_id, message,), eta=scheduled_time)
    return


@db_task()
def check_reminder(patient, reminder_id, message):
    # print('check reminder: ' + str(datetime.datetime.utcnow()) +
    #       '; ' + patient['phone_number'] + '; ' + message)
    #  check sql for completion
    reminder = Reminder.objects.get(id=reminder_id)
    completed = getattr(reminder, 'completed')
    if not completed:
        send_reminder(patient, reminder_id, message,)
    return

# @periodic_task(crontab(minute='*/5'))
# def every_five_mins():
#     print('Every five minutes this will be printed by the consumer')
