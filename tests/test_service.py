import os
from nitrado import Service
from nitrado import Client


def set_client():
    if Service.CLIENT:
        return
    url = "https://api.nitrado.net/"
    if not Client.CLIENT:
        Client.CLIENT = Client(url, key=os.environ['NITRADO_KEY'])
    Service.CLIENT = Client.CLIENT


def test_services():
    set_client()
    services = Service.all()
    assert len(services) > 0


def test_logs():
    set_client()
    service = Service.all()[0]
    logs = service.logs()
    assert type(logs) == list


def test_tasks():
    set_client()
    service = Service.all()[0]
    tasks = service.tasks()
    assert type(tasks) == list


def test_notifications():
    set_client()
    service = Service.all()[0]
    notif = service.notifications()
    assert type(notif) == list


def tests():
    test_services()
    test_notifications()
    test_logs()
    test_tasks()


if __name__ == "__main__":
    tests()
    print("passing")
