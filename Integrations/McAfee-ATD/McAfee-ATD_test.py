from McAfee-ATD import prettify_current_user_res, prettify_task_status_by_taskId_res


def test_prettify_current_user_res():
    expected_user_dict = dict({
        'APIVersion': "1.0", 'IsAdmin': "True", 'SessionId': "42", 'UserId': 101})
    prettify_user_res = prettify_current_user_res(
        {'apiVersion': "1.0", 'isAdmin': "1", 'session': "42", 'userId': 101})
    assert expected_user_dict == prettify_user_res


def test_prettify_task_status_by_taskId_res():
    expected_rtask_status = dict({
        'taskId': "41", 'jobId': "42", 'status': "finished", 'filename': "my_name", 'MDx5': "my_md5", 'submitTime': "010101"})
    prettify_task_status_res = prettify_task_status_by_taskId_res(
        {'taskid': "41", 'jobid': "42", 'status': "finished", 'filename': "my_name", 'MD5': "my_md5", 'submitTime': "010101"})
    assert expected_rtask_status == prettify_task_status_res