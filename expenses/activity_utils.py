# pylint: disable=no-member, arguments-differ
from collections import OrderedDict
from decimal import Decimal
from .models import Expense, Comment

def _get_bulk_records(activities):
    '''
    Returns dictionary of records, grouped by dictionary
    It is expensive for database to do multiple queries for each loop in activities
    We insteads gather all the ids of records and query them once for each objects and create
    a dictionary map so we can use later.
    '''

    # capture the ids of expense and comments to do a bullk query for efficiency
    # creater_dict = {}

    expense_set = set()
    comment_set = set()

    for activity in activities:
        if activity.model_name.lower() == 'expense':
            expense_set.add(activity.record_ref)
        elif activity.model_name.lower() == 'comment':
            comment_set.add(activity.record_ref)
        else:
            # more things later
            pass

    expense_dict = {}
    comment_dict = {}

    # doing a bulk query
    if len(expense_set) > 0:
        for expense in Expense.objects.filter(pk__in=list(expense_set)):
            expense_dict[str(expense.id)] = expense

    if len(comment_set) > 0:
        for comment in Comment.objects.filter(pk__in=list(comment_set)):
            comment_dict[str(comment.id)] = comment

    # there must a shorter syntax of doing this
    return {
        'expense_dict': expense_dict,
        'comment_dict': comment_dict
    }


def _to_dictionary(instance_name, ref_id, record_dict):

    record_detail = {}
    if instance_name.lower() == 'expense':
        expense_inst = record_dict['expense_dict'][str(ref_id)]
        record_detail = {
            'amount' : str(Decimal(expense_inst.amount)),
            'split_type' : expense_inst.split_type
        }

    elif instance_name.lower() == 'comment':
        comment_inst = record_dict['comment_dict'][str(ref_id)]
        record_detail = {
            'text' : comment_inst.text,
            'expense_id' : str(comment_inst.expense.id)
        }

    return record_detail


def human_readable_activities(activities, return_single=False):
    '''
    This is to help the front end and create useful human readable info for each activity
    '''

    record_dict = _get_bulk_records(activities)

    all_activities = []

    for activity in activities:
        readable_activity = OrderedDict()
        readable_activity['id'] = str(activity.id)
        readable_activity['activity_type'] = activity.activity_type
        readable_activity['creator'] = activity.creator.to_dict(include_names=True)
        readable_activity['record_ref'] = activity.record_ref
        readable_activity['model_name'] = activity.model_name
        readable_activity['activity_detail'] = _to_dictionary(activity.model_name, activity.record_ref, record_dict)

        # intentionally not using the model serializer as it will query again - we already have enough data to create dictionary

        all_activities.append(readable_activity)

    return all_activities[0] if return_single and len(all_activities) == 1 else all_activities