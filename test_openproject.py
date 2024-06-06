from open_project import *

import pytest
from http import HTTPStatus


def test_get_project_by_id(authenticated_session):
    project_id = "12"
    expected_name = "nice project"
    expected_description = "new description"

    response = get_project_by_id(authenticated_session, project_id)
    assert response.status_code == HTTPStatus.OK
    
    project = response.json()
    assert project["name"] == expected_name
    assert project["description"]["raw"] == expected_description

def test_update_project_description_by_id(authenticated_session):
    project_id = "12"
    expected_description = 'new description'

    response = update_project_description_by_id(authenticated_session, project_id, expected_description)
    assert response.status_code == HTTPStatus.OK
    
    project = response.json()
    assert project["description"]["raw"] == expected_description
    
def test_create_and_delete_project(authenticated_session):
    project_name = 'new project'
    
    response = create_project(authenticated_session, project_name)
    assert response.status_code == HTTPStatus.CREATED
    project = response.json()
    assert project["name"] == project_name

    project_id = project["id"]
    response = delete_project_by_id(authenticated_session, project_id)
    assert response.status_code == HTTPStatus.NO_CONTENT   


def test_get_work_package_by_id(authenticated_session):
    work_package_id = 38
    expected_subject = "My Task 1"
    
    response = get_work_package_by_id(authenticated_session, work_package_id)
    assert response.status_code == HTTPStatus.OK
    
    work_package = response.json()
    assert work_package["subject"] == expected_subject

def test_update_work_package_description_by_id(authenticated_session):
    work_package_id = 38
    new_description = "new description"
    
    response = update_work_package_description_by_id(authenticated_session, work_package_id, new_description)
    assert response.status_code == HTTPStatus.OK
    
    work_package = response.json()
    assert work_package["description"]["raw"] == new_description

def test_create_and_delete_work_package(authenticated_session):
    project_id = 12
    subject = "My Task 2"
    
    response = create_work_package(authenticated_session, project_id, subject)
    assert response.status_code == HTTPStatus.CREATED
    work_package = response.json()
    assert work_package["subject"] == subject

    work_package_id = work_package["id"]
    response = delete_work_package_by_id(authenticated_session, work_package_id)
    assert response.status_code == HTTPStatus.NO_CONTENT 


if __name__ == "__main__":
     pytest.main()
