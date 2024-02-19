from app.models.task_model import Task
from app.models.model import db
from ..helpers.time import time_now
from ..errors.error_factory import unauthorized_error
from sqlalchemy import and_


def create_task(user_id, title, description, category_id):
    task = Task(
        user_id=user_id, title=title, description=description, category_id=category_id
    )
    db.session.add(task)
    db.session.commit()
    return task.as_dict()


def find_all_tasks_by_user_id(user_id, page, per_page, category_ids, completed):
    conditions = [Task.deleted_at.is_(None), Task.user_id == user_id]

    if category_ids:
        conditions.append(Task.category_id.in_(category_ids))

    if completed is not None:
        conditions.append(Task.completed == completed)

    paginated_tasks = (
        Task.query.filter(and_(*conditions))
        .order_by(Task.completed)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    serialized_tasks = []

    for task in paginated_tasks.items:
        serialized_task = task.as_dict()
        serialized_tasks.append(serialized_task)

    return {
        "tasks": serialized_tasks,
        "total_pages": paginated_tasks.pages,
        "current_page": page,
        "per_page": per_page,
    }


def find_one_by_id(task_id, user_id):
    task = Task.query.filter(Task.deleted_at.is_(None), Task.id == task_id).first()

    if task is None:
        return None

    if task.user_id != user_id:
        return unauthorized_error()

    task_as_dict = task.as_dict()

    return task_as_dict


def handle_task_complete_by_id(task_id, user_id):
    task = Task.query.filter(Task.deleted_at.is_(None), Task.id == task_id).first()

    if task.user_id != user_id:
        return unauthorized_error()

    task.completed = not task.completed

    if task.completed:
        task.finished_at = time_now()
    else:
        task.finished_at = None
    db.session.commit()


def update_task(task_id, update_payload={}):
    task = Task.query.filter(Task.id == task_id).first()

    if update_payload.get("title") and task.title != update_payload.get("title"):
        task.title = update_payload.get("title")

    if (
        "description" in update_payload
        and task.description != update_payload["description"]
    ):
        task.description = update_payload["description"]

    if (
        "category_id" in update_payload
        and task.category_id != update_payload["category_id"]
    ):
        task.category_id = update_payload["category_id"]

    db.session.commit()
    return task.as_dict()


def remove_task(task_id, user_id):
    task = Task.query.filter(Task.id == task_id, Task.user_id == user_id).first()
    task.deleted_at = time_now()

    db.session.commit()
    return None
