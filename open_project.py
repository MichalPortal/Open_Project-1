from config import BASE_URL
from http import HTTPStatus


def get_project_by_id(session, project_id):
    url = f'{BASE_URL}/projects/{project_id}'
    response = session.get(url)
    return response

def update_project_description_by_id(session, project_id, description):
    url = f'{BASE_URL}/projects/{project_id}'
    data = {
        "description": {
            "raw": description
        }
    }
    response = session.patch(url, json=data)
    return response

def create_project(session, project_name):
    url = f'{BASE_URL}/projects'
    data = {
        "name": project_name
    }
    response = session.post(url, json=data)
    return response

def delete_project_by_id(session,project_id):
    url = f'{BASE_URL}/projects/{project_id}'
    response = session.delete(url)
    return response


def get_work_package_by_id(session, work_package_id):
    url = f"{BASE_URL}/work_packages/{work_package_id}"
    response = session.get(url)
    return response

def update_work_package_description_by_id(session, work_package_id, new_description):
    response = get_work_package_by_id(session, work_package_id)
    if response.status_code != HTTPStatus.OK:
        print(f"Failed. Status code: {response.status_code}")
        return response
    
    work_package = response.json()
    lock_version = work_package["lockVersion"]
    
    url = f"{BASE_URL}/work_packages/{work_package_id}"
    data = {
        "lockVersion": lock_version,
        "description": {
            "raw": new_description
        }
    }
    response = session.patch(url, json=data)
    return response

def create_work_package(session, project_id, subject):
    url = f"{BASE_URL}/work_packages"
    data = {
        "subject": subject,
        "_links": {
            "type": {
                "href": f"/api/v3/types/1"
            },
            "project": {
                "href": f"/api/v3/projects/{project_id}"
            }
        }
    }
    response = session.post(url, json=data)
    return response

def delete_work_package_by_id(session, work_package_id):
    url = f'{BASE_URL}/work_packages/{work_package_id}'
    response = session.delete(url)
    return response


if __name__ == "__main__":
    pass
