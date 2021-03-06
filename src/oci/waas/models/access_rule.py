# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRule(object):
    """
    A content access rule. An access rule specifies an action to take if a set of criteria is matched by a request.
    """

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "BYPASS"
    ACTION_BYPASS = "BYPASS"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "REDIRECT"
    ACTION_REDIRECT = "REDIRECT"

    #: A constant which can be used with the block_action property of a AccessRule.
    #: This constant has a value of "SET_RESPONSE_CODE"
    BLOCK_ACTION_SET_RESPONSE_CODE = "SET_RESPONSE_CODE"

    #: A constant which can be used with the block_action property of a AccessRule.
    #: This constant has a value of "SHOW_ERROR_PAGE"
    BLOCK_ACTION_SHOW_ERROR_PAGE = "SHOW_ERROR_PAGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "JS_CHALLENGE"
    BYPASS_CHALLENGES_JS_CHALLENGE = "JS_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "DEVICE_FINGERPRINT_CHALLENGE"
    BYPASS_CHALLENGES_DEVICE_FINGERPRINT_CHALLENGE = "DEVICE_FINGERPRINT_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "HUMAN_INTERACTION_CHALLENGE"
    BYPASS_CHALLENGES_HUMAN_INTERACTION_CHALLENGE = "HUMAN_INTERACTION_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "CAPTCHA"
    BYPASS_CHALLENGES_CAPTCHA = "CAPTCHA"

    #: A constant which can be used with the redirect_response_code property of a AccessRule.
    #: This constant has a value of "MOVED_PERMANENTLY"
    REDIRECT_RESPONSE_CODE_MOVED_PERMANENTLY = "MOVED_PERMANENTLY"

    #: A constant which can be used with the redirect_response_code property of a AccessRule.
    #: This constant has a value of "FOUND"
    REDIRECT_RESPONSE_CODE_FOUND = "FOUND"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AccessRule.
        :type name: str

        :param criteria:
            The value to assign to the criteria property of this AccessRule.
        :type criteria: list[AccessRuleCriteria]

        :param action:
            The value to assign to the action property of this AccessRule.
            Allowed values for this property are: "ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param block_action:
            The value to assign to the block_action property of this AccessRule.
            Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type block_action: str

        :param block_response_code:
            The value to assign to the block_response_code property of this AccessRule.
        :type block_response_code: int

        :param block_error_page_message:
            The value to assign to the block_error_page_message property of this AccessRule.
        :type block_error_page_message: str

        :param block_error_page_code:
            The value to assign to the block_error_page_code property of this AccessRule.
        :type block_error_page_code: str

        :param block_error_page_description:
            The value to assign to the block_error_page_description property of this AccessRule.
        :type block_error_page_description: str

        :param bypass_challenges:
            The value to assign to the bypass_challenges property of this AccessRule.
            Allowed values for items in this list are: "JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type bypass_challenges: list[str]

        :param redirect_url:
            The value to assign to the redirect_url property of this AccessRule.
        :type redirect_url: str

        :param redirect_response_code:
            The value to assign to the redirect_response_code property of this AccessRule.
            Allowed values for this property are: "MOVED_PERMANENTLY", "FOUND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type redirect_response_code: str

        """
        self.swagger_types = {
            'name': 'str',
            'criteria': 'list[AccessRuleCriteria]',
            'action': 'str',
            'block_action': 'str',
            'block_response_code': 'int',
            'block_error_page_message': 'str',
            'block_error_page_code': 'str',
            'block_error_page_description': 'str',
            'bypass_challenges': 'list[str]',
            'redirect_url': 'str',
            'redirect_response_code': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'criteria': 'criteria',
            'action': 'action',
            'block_action': 'blockAction',
            'block_response_code': 'blockResponseCode',
            'block_error_page_message': 'blockErrorPageMessage',
            'block_error_page_code': 'blockErrorPageCode',
            'block_error_page_description': 'blockErrorPageDescription',
            'bypass_challenges': 'bypassChallenges',
            'redirect_url': 'redirectUrl',
            'redirect_response_code': 'redirectResponseCode'
        }

        self._name = None
        self._criteria = None
        self._action = None
        self._block_action = None
        self._block_response_code = None
        self._block_error_page_message = None
        self._block_error_page_code = None
        self._block_error_page_description = None
        self._bypass_challenges = None
        self._redirect_url = None
        self._redirect_response_code = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AccessRule.
        The unique name of the access rule.


        :return: The name of this AccessRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AccessRule.
        The unique name of the access rule.


        :param name: The name of this AccessRule.
        :type: str
        """
        self._name = name

    @property
    def criteria(self):
        """
        **[Required]** Gets the criteria of this AccessRule.
        The list of access rule criteria.


        :return: The criteria of this AccessRule.
        :rtype: list[AccessRuleCriteria]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this AccessRule.
        The list of access rule criteria.


        :param criteria: The criteria of this AccessRule.
        :type: list[AccessRuleCriteria]
        """
        self._criteria = criteria

    @property
    def action(self):
        """
        **[Required]** Gets the action of this AccessRule.
        The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.

        - **ALLOW:** Takes no action, just logs the request.

        - **DETECT:** Takes no action, but creates an alert for the request.

        - **BLOCK:** Blocks the request by returning specified response code or showing error page.

        - **BYPASS:** Bypasses some or all challenges.

        - **REDIRECT:** Redirects the request to the specified URL.

        Regardless of action, no further rules are processed once the rule is matched.

        Allowed values for this property are: "ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this AccessRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AccessRule.
        The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.

        - **ALLOW:** Takes no action, just logs the request.

        - **DETECT:** Takes no action, but creates an alert for the request.

        - **BLOCK:** Blocks the request by returning specified response code or showing error page.

        - **BYPASS:** Bypasses some or all challenges.

        - **REDIRECT:** Redirects the request to the specified URL.

        Regardless of action, no further rules are processed once the rule is matched.


        :param action: The action of this AccessRule.
        :type: str
        """
        allowed_values = ["ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def block_action(self):
        """
        Gets the block_action of this AccessRule.
        The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to `SET_RESPONSE_CODE`.

        Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The block_action of this AccessRule.
        :rtype: str
        """
        return self._block_action

    @block_action.setter
    def block_action(self, block_action):
        """
        Sets the block_action of this AccessRule.
        The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to `SET_RESPONSE_CODE`.


        :param block_action: The block_action of this AccessRule.
        :type: str
        """
        allowed_values = ["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"]
        if not value_allowed_none_or_none_sentinel(block_action, allowed_values):
            block_action = 'UNKNOWN_ENUM_VALUE'
        self._block_action = block_action

    @property
    def block_response_code(self):
        """
        Gets the block_response_code of this AccessRule.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are met. If unspecified, defaults to `403`.


        :return: The block_response_code of this AccessRule.
        :rtype: int
        """
        return self._block_response_code

    @block_response_code.setter
    def block_response_code(self, block_response_code):
        """
        Sets the block_response_code of this AccessRule.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are met. If unspecified, defaults to `403`.


        :param block_response_code: The block_response_code of this AccessRule.
        :type: int
        """
        self._block_response_code = block_response_code

    @property
    def block_error_page_message(self):
        """
        Gets the block_error_page_message of this AccessRule.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'


        :return: The block_error_page_message of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_message

    @block_error_page_message.setter
    def block_error_page_message(self, block_error_page_message):
        """
        Sets the block_error_page_message of this AccessRule.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'


        :param block_error_page_message: The block_error_page_message of this AccessRule.
        :type: str
        """
        self._block_error_page_message = block_error_page_message

    @property
    def block_error_page_code(self):
        """
        Gets the block_error_page_code of this AccessRule.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access rules'.


        :return: The block_error_page_code of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_code

    @block_error_page_code.setter
    def block_error_page_code(self, block_error_page_code):
        """
        Sets the block_error_page_code of this AccessRule.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access rules'.


        :param block_error_page_code: The block_error_page_code of this AccessRule.
        :type: str
        """
        self._block_error_page_code = block_error_page_code

    @property
    def block_error_page_description(self):
        """
        Gets the block_error_page_description of this AccessRule.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'


        :return: The block_error_page_description of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_description

    @block_error_page_description.setter
    def block_error_page_description(self, block_error_page_description):
        """
        Sets the block_error_page_description of this AccessRule.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'


        :param block_error_page_description: The block_error_page_description of this AccessRule.
        :type: str
        """
        self._block_error_page_description = block_error_page_description

    @property
    def bypass_challenges(self):
        """
        Gets the bypass_challenges of this AccessRule.
        The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.

        - **JS_CHALLENGE:** Bypasses JavaScript Challenge.

        - **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge.

        - **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge.

        - **CAPTCHA:** Bypasses CAPTCHA Challenge.

        Allowed values for items in this list are: "JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The bypass_challenges of this AccessRule.
        :rtype: list[str]
        """
        return self._bypass_challenges

    @bypass_challenges.setter
    def bypass_challenges(self, bypass_challenges):
        """
        Sets the bypass_challenges of this AccessRule.
        The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.

        - **JS_CHALLENGE:** Bypasses JavaScript Challenge.

        - **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge.

        - **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge.

        - **CAPTCHA:** Bypasses CAPTCHA Challenge.


        :param bypass_challenges: The bypass_challenges of this AccessRule.
        :type: list[str]
        """
        allowed_values = ["JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA"]
        if bypass_challenges:
            bypass_challenges[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in bypass_challenges]
        self._bypass_challenges = bypass_challenges

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this AccessRule.
        The target to which the request should be redirected, represented as a URI reference.


        :return: The redirect_url of this AccessRule.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this AccessRule.
        The target to which the request should be redirected, represented as a URI reference.


        :param redirect_url: The redirect_url of this AccessRule.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_response_code(self):
        """
        Gets the redirect_response_code of this AccessRule.
        The response status code to return when `action` is set to `REDIRECT`.

        - **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301).

        - **FOUND:** Used for designating the temporary movement of a page (numerical code - 302).

        Allowed values for this property are: "MOVED_PERMANENTLY", "FOUND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The redirect_response_code of this AccessRule.
        :rtype: str
        """
        return self._redirect_response_code

    @redirect_response_code.setter
    def redirect_response_code(self, redirect_response_code):
        """
        Sets the redirect_response_code of this AccessRule.
        The response status code to return when `action` is set to `REDIRECT`.

        - **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301).

        - **FOUND:** Used for designating the temporary movement of a page (numerical code - 302).


        :param redirect_response_code: The redirect_response_code of this AccessRule.
        :type: str
        """
        allowed_values = ["MOVED_PERMANENTLY", "FOUND"]
        if not value_allowed_none_or_none_sentinel(redirect_response_code, allowed_values):
            redirect_response_code = 'UNKNOWN_ENUM_VALUE'
        self._redirect_response_code = redirect_response_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
