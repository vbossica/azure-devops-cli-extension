# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_git_client,
                                      resolve_instance,
                                      resolve_instance_project_and_repo)


def list_branches(repository=None, project=None, team_instance=None, detect=None):
    """List branches of a Git repository.
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        return client.get_branches(repository_id=repository, project=project)
    except Exception as ex:
        handle_command_exception(ex)


def show_branch(name, repository=None, project=None, team_instance=None, detect=None):
    """Get the details of a branch.
    :param str name: Name of the branch.
    :param str project: Name or ID of the team project.
    :param str repository: Name or ID of the repository.
    """
    try:
        team_instance, project, repository = resolve_instance_project_and_repo(
            detect=detect, team_instance=team_instance, project=project, repo=repository)
        client = get_git_client(team_instance)
        return client.get_branch(repository, name, project)
    except Exception as ex:
        handle_command_exception(ex)
