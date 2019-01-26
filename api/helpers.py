class Validator:
    def __init__(self, attrs = {}):
        self.errors = {}
        self.attributes = attrs

    def validate(self):
        raise Exception('You must implement the validate() function in a subclass')

    def is_valid(self):
        self.errors = {}
        self.validate()

        return len(self.errors) == 0

    def assert_present(self, attr, message = "not_present"):
        if self.attributes.get(attr) is None:
            self._add_error(attr, message)
            return False

        return True

    def assert_list(self, attr, message="not_valid"):
        lst = self.attributes.get(attr)

        if type(lst) is not list:
            self._add_error(attr, message)

            return False

        return True

    def assert_not_present(self, attr, message="not_allowed"):
        if self.attributes.get(attr) is not None:
            self._add_error(attr, message)
            return False
        else:
            return True

    def _add_error(self, attr, error):
        if self.errors.get(attr) is None:
            self.errors[attr] = []

        self.errors[attr].append(error)

def app_to_dict(app):
    return {
        "id": app.id,
        "name": app.name,
        "env_name": app.env_name,
        "env_file": app.env_file
    }

def apps_to_dict(apps):
    app_list = []

    for a in apps:
        app_list.append(app_to_dict(a))

    return app_list

