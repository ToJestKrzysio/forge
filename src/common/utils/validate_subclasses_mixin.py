class ValidateSubclassesMixin:
    """
    A mixin allowing for validation of settings in all child classes.
    """

    @classmethod
    def validate_class(cls):
        """Instantiate child class checking whether all required settings are provided."""
        cls()

    @classmethod
    def validate_subclasses(cls):
        """Validate whether all child classes can be instantiated."""
        cls.validate_class()

        for subclass in cls.__subclasses__():
            if subclass is cls:
                continue
            subclass.validate_subclasses()
