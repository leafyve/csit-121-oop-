class Trainee:
    def __init__(self, trainee_id,name,birthdate,email):
        self.__trainee_id = trainee_id
        self.__name = name
        self.__birthdate = birthdate
        self.__email = email

    def get_age(self):
        return 2025 - self.__birthdate

    def __str__(self):
        return f"Trainee Id: {self.__trainee_id} Name:{self.__name} Birthdate: {self.__birthdate} Email: {self.__email}"

class Trainer:
    def __init__(self, trainer_id, name):
        self.__trainer_id = trainer_id
        self.__name = name

    def __str__(self):
        return f"Trainer Id: {self.__trainer_id} Name: {self.__name}"

class ExerciseSession:
    def __int__(self, session_id, duration, intensity, date):
        self.__session_id = session_id
        # to do: link the class trainer id
        #        and trainee id
        self.__duration = duration
        self.__intensity = intensity
        self.__date = date

# to do: link the 3 objects together
class PersonalTrainingManagementSystem:
    def add_trainer(self, id, name):
        pass

    def add_trainee(self, id, name, birthdate, email):
        pass

    def create_session(self, id, trainer_id, trainee_id, duration, intensity, date):
        pass

    def get_trainer(self, trainer_id):
        return self.__trainer_id

    def get_trainee(self, trainee_id):
        return self.__trainee_id

    def get_session(self, session_id):
        return self.__session_id

    def get_trainee_total_duration(self, trainee_id, duration):
        pass
        # to do: calculate total exercise duration of all sessions

    def get_trainee_ave_intensity(self,trainee_id, intensity):
        pass

    def get_trainer_total_duration(self,trainer_id, duration):
        pass

    def get_trainer_total_duration_with_trainee(self, trainer_id, trainee_id):
        pass

    def remove_session(self, session_id):
        pass

# need user input?
Trainee1 = Trainee("123","Bob","2000","123@gmail.com")
Trainer1 = Trainer("123","Alex")
print(Trainee1)
print(Trainer1)