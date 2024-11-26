import abc

class CreateCourseInterface(abc.ABC):
    @abc.abstractmethod
    def create_course(self, name, instructor):
        pass

class CreateLabInterface(abc.ABC):
    @abc.abstractmethod
    def create_lab(self, lab_name, course_name, ta):
        pass

class CheckPermissionInterface(abc.ABC):
    @abc.abstractmethod
    def check_admin(self, user):
        pass

    @abc.abstractmethod
    def check_instructor(self, user):
        pass