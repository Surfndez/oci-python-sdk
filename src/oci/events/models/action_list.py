# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionList(object):
    """
    A list of Action objects associated with a rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActionList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param actions:
            The value to assign to the actions property of this ActionList.
        :type actions: list[Action]

        """
        self.swagger_types = {
            'actions': 'list[Action]'
        }

        self.attribute_map = {
            'actions': 'actions'
        }

        self._actions = None

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this ActionList.
        A list of one or more Action objects.


        :return: The actions of this ActionList.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this ActionList.
        A list of one or more Action objects.


        :param actions: The actions of this ActionList.
        :type: list[Action]
        """
        self._actions = actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
