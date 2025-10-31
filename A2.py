from abc import ABC, abstractmethod
from datetime import date

class Patient:
    __next_patient_id = 1

    def __init__(self, name, birthdate):
        self.__patient_id = Patient.__next_patient_id
        Patient.__next_patient_id += 1
        self.__name = name
        self.__birthdate = birthdate

    @property
    def patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_birthdate(self):
        return self.__birthdate

    def get_age(self):
        today = date.today()
        age = today.year - self.__birthdate.year - (
                (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day))
        return age

    def __str__(self):
        age = self.get_age()
        return f"Patient(id:{self.__patient_id}, name:{self.__name}, age:{age})"

class Session(ABC):
    __next_session_id = 1

    def __init__(self, patient, duration, base_rate):
        self.__session_id = Session.__next_session_id
        Session.__next_session_id += 1
        self.__patient = patient
        self.__duration = duration
        self.__base_rate = base_rate

    def get_session_id(self):
        return self.__session_id

    def get_patient(self):
        return self.__patient

    def get_duration(self):
        return self.__duration

    def get_base_rate(self):
        return self.__base_rate

    @abstractmethod
    def calculate_cost(self):
        pass

    def _round_to_nearest_10_cents(self, cost):
        # Round to nearest 10 cents
        # Multiply by 10, round, then divide by 10
        return round(cost * 10) / 10

    def _calculate_base_cost(self):
        # Calculate base cost from duration and base rate
        num_blocks = self.__duration / 30
        return num_blocks * self.__base_rate

    def _apply_senior_discount(self, cost):
        # Apply 20% discount for seniors (60+)
        if self.__patient.get_age() >= 60:
            return cost * 0.8
        return cost


class GeneralTherapy(Session):
    def __init__(self, patient, duration, base_rate, focus_area):
        super().__init__(patient, duration, base_rate)
        self.__focus_area = focus_area

    def get_focus_area(self):
        return self.__focus_area

    def calculate_cost(self):
        # Calculate base cost
        base_cost = self._calculate_base_cost()

        # Apply senior discount if applicable
        final_cost = self._apply_senior_discount(base_cost)

        # Round to nearest 10 cents
        return self._round_to_nearest_10_cents(final_cost)


class SportsInjury(Session):
    def __init__(self, patient, duration, base_rate, sport_type, injury_severity, pro_athlete):
        super().__init__(patient, duration, base_rate)
        self.__sport_type = sport_type
        self.__injury_severity = injury_severity
        self.__pro_athlete = pro_athlete

    def get_sport_type(self):
        return self.__sport_type

    def get_injury_severity(self):
        return self.__injury_severity

    def get_pro_athlete(self):
        return self.__pro_athlete

    def calculate_cost(self):
        # Calculate base cost
        base_cost = self._calculate_base_cost()

        # Apply professional athlete discount first (80% off = pay 20%)
        if self.__pro_athlete:
            base_cost = base_cost * 0.2

        # Apply senior discount if applicable
        final_cost = self._apply_senior_discount(base_cost)

        # Round to nearest 10 cents
        return self._round_to_nearest_10_cents(final_cost)


class PostSurgeryRehab(Session):
    def __init__(self, patient, duration, base_rate, surgery_type):
        super().__init__(patient, duration, base_rate)
        self.__surgery_type = surgery_type

    def get_surgery_type(self):
        return self.__surgery_type

    def calculate_cost(self):
        # Calculate base cost
        base_cost = self._calculate_base_cost()

        # Add 15% surcharge
        base_cost = base_cost * 1.15

        # Apply senior discount if applicable
        final_cost = self._apply_senior_discount(base_cost)

        # Round to nearest 10 cents
        return self._round_to_nearest_10_cents(final_cost)


class PaediatricTherapy(Session):
    def __init__(self, patient, duration, base_rate, guardian_name):
        super().__init__(patient, duration, base_rate)
        self.__guardian_name = guardian_name

    def get_guardian_name(self):
        return self.__guardian_name

    def calculate_cost(self):
        # Calculate base cost
        base_cost = self._calculate_base_cost()

        # Apply 10% discount
        base_cost = base_cost * 0.9

        # Round to nearest 10 cents
        return self._round_to_nearest_10_cents(base_cost)


class ClinicBookingSystem:
    def __init__(self):
        self.__patients = []
        self.__sessions = []

    def add_patient(self, name, birthdate):
        # Validate inputs
        if name is None or birthdate is None:
            return False

        # Handle string or date object for birthdate
        if isinstance(birthdate, str):
            try:
                parts = birthdate.split('-')
                if len(parts) != 3:
                    return False
                year, month, day = map(int, parts)
                birthdate_obj = date(year, month, day)
            except:
                return False
        elif isinstance(birthdate, date):
            birthdate_obj = birthdate
        else:
            return False

        # Create and add new patient
        try:
            new_patient = Patient(name, birthdate_obj)
            self.__patients.append(new_patient)
            return new_patient.patient_id
        except:
            return False

    def book_session(self, session_type, patient_id, duration, base_rate, **booking_args):
        # Validate basic inputs
        if session_type is None or patient_id is None or duration is None or base_rate is None:
            return False

        # Validate duration (must be in 30 minute blocks)
        if not isinstance(duration, (int, float)) or duration <= 0 or duration % 30 != 0:
            return False

        # Validate base_rate
        if not isinstance(base_rate, (int, float)) or base_rate <= 0:
            return False

        # Find patient
        patient = self.get_patient(patient_id)
        if patient == False or patient is None:
            return False

        # Validate paediatric age requirement
        if session_type == "Paediatric":
            if patient.get_age() > 18:
                return False

        # Create appropriate session type
        try:
            if session_type == "General":
                if "focus_area" not in booking_args:
                    return False
                focus_area = booking_args["focus_area"]
                if focus_area is None or not isinstance(focus_area, str) or focus_area.strip() == "":
                    return False
                new_session = GeneralTherapy(patient, duration, base_rate, focus_area)

            elif session_type == "Sports":
                if "sport_type" not in booking_args or "injury_severity" not in booking_args or "pro_athlete" not in booking_args:
                    return False
                sport_type = booking_args["sport_type"]
                injury_severity = booking_args["injury_severity"]
                pro_athlete = booking_args["pro_athlete"]

                # Validate sport_type
                if sport_type is None or not isinstance(sport_type, str) or sport_type.strip() == "":
                    return False

                # Validate injury_severity (1-3)
                if not isinstance(injury_severity, int) or injury_severity < 1 or injury_severity > 3:
                    return False

                # Validate pro_athlete
                if not isinstance(pro_athlete, bool):
                    return False

                new_session = SportsInjury(patient, duration, base_rate,
                                           sport_type, injury_severity, pro_athlete)

            elif session_type == "PostSurgery":
                if "surgery_type" not in booking_args:
                    return False
                surgery_type = booking_args["surgery_type"]
                if surgery_type is None or not isinstance(surgery_type, str) or surgery_type.strip() == "":
                    return False
                new_session = PostSurgeryRehab(patient, duration, base_rate, surgery_type)

            elif session_type == "Paediatric":
                if "guardian_name" not in booking_args:
                    return False
                guardian_name = booking_args["guardian_name"]
                if guardian_name is None or not isinstance(guardian_name, str) or guardian_name.strip() == "":
                    return False
                new_session = PaediatricTherapy(patient, duration, base_rate, guardian_name)
            else:
                return False

            self.__sessions.append(new_session)
            return True
        except:
            return False

    def get_patient(self, patient_id):
        # Validate patient_id
        if patient_id is None or not isinstance(patient_id, int) or patient_id <= 0:
            return False

        for patient in self.__patients:
            if patient.patient_id == patient_id:
                return patient
        return False

    def get_sessions(self, patient_id):
        # Validate patient_id
        if patient_id is None or not isinstance(patient_id, int) or patient_id <= 0:
            return False

        # Check if patient exists
        if self.get_patient(patient_id) == False:
            return False

        # Get all sessions for this patient
        patient_sessions = []
        for session in self.__sessions:
            if session.get_patient().patient_id == patient_id:
                patient_sessions.append(session)
        return patient_sessions
