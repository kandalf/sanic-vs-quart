from .helpers import Validator

class ApplicationValidator(Validator):
    def validate(self):
        self.assert_present("env_name")

        if self.assert_present("name"):
            if len(self.attributes["name"]) < 5:
                self._add_error("name", "not_valid")
