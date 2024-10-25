from abc import abstractmethod


class Component:
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def on_service_success(self):
        pass

    @abstractmethod
    def on_service_fail(self):
        pass

    @property
    @abstractmethod
    def service(self):
        pass
