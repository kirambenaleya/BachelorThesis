class Survey(object):
    def __init__(self, first_name, last_name, age, experience, gender, bachelor, major, matriculation_number, teammate,
                 schedule, email, attempt):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.attempt = attempt
        self.bachelor = bachelor
        self.major = major
        self.matriculation_number = matriculation_number
        self.teammate = teammate
        self.schedule = schedule
        self.email = email
        self.experience = experience

    @staticmethod
    def from_dict(source):
        if source:
            return Survey(source['First Name'], source['Last Name'], source['Age'], source['Gender'],
                          source['Bachelor/Master'], source['Major/Minor'], source['Matriculation Number'],
                          source['Teammate'], source['Schedule'], source['Email'], source['Attempt'],
                          source['Experience'])
        else:
            return None

    def to_dict(self):
        return {'First Name': self.first_name, 'Last Name': self.last_name, 'Age': self.age, 'Gender': self.gender,
                'Bachelor/Master': self.bachelor, 'Major/Minor': self.major,
                'Matriculation Number': self.matriculation_number, 'Teammate': self.teammate, 'Schedule': self.schedule,
                'Email': self.email, 'Attempt': self.attempt, 'Experience': self.experience}

    def __repr__(self):
        return (
            f'Survey(\
                First Name={self.first_name}, \
                Last Name={self.last_name}, \
                Age={self.age}, \
                Gender={self.gender}, \
                Bachelor/Master={self.bachelor}\
                Major/Minor={self.major}\
                Matriculation Number={self.matriculation_number}\
                Teammate={self.teammate}\
                Schedule={self.schedule}\
                Email={self.email}\
                Attempt={self.attempt}\
                Experience={self.experience}\
            )'
        )


class Student(object):
    def __init__(self, first_name, last_name, age, gender, bachelor, matriculation_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.bachelor = bachelor
        self.matriculation_number = matriculation_number
        self.email = email

    @staticmethod
    def from_dict(source):
        if source:
            return Student(source['First Name'], source['Last Name'], source['Age'], source['Gender'],
                           source['Bachelor/Master'], source['Matriculation Number'], source['Email'])
        else:
            return None

    def to_dict(self):
        return {'First Name': self.first_name, 'Last Name': self.last_name, 'Age': self.age, 'Gender': self.gender,
                'Bachelor/Master': self.bachelor, 'Matriculation Number': self.matriculation_number,
                'Email': self.email}

    def __repr__(self):
        return (
            f'Survey(\
                First Name={self.first_name}, \
                Last Name={self.last_name}, \
                Age={self.age}, \
                Gender={self.gender}, \
                Bachelor/Master={self.bachelor}\
                Matriculation Number={self.matriculation_number}\
                Email={self.email}\
            )'
        )


class Weights(object):
    def __init__(self, weight_age, weight_gender, weight_bachelor, weight_major, weight_teammate, weight_schedule,
                 weight_attempt, weight_experience, matriculation_number):
        self.weight_age = weight_age
        self.weight_gender = weight_gender
        self.weight_attempt = weight_attempt
        self.weight_bachelor = weight_bachelor
        self.weight_major = weight_major
        self.weight_teammate = weight_teammate
        self.weight_schedule = weight_schedule
        self.weight_experience = weight_experience
        self.matriculation_number = matriculation_number

    @staticmethod
    def from_dict(source):
        if source:
            return Weights(source['Matriculation Number'], source['Weight Age'], source['Weight Gender'],
                           source['Weight Bachelor/Master'], source['Weight Major/Minor'], source['Weight Teammate'],
                           source[' Weight Schedule'], source['Weight Attempt'], source['Weight Experience'])
        else:
            return None

    def to_dict(self):
        return {'Matriculation Number': self.matriculation_number, 'Weight Age': self.weight_age,
                'Weight Gender': self.weight_gender, 'Weight Bachelor/Master': self.weight_bachelor,
                'Weight Major/Minor': self.weight_major, 'Weight Teammate': self.weight_teammate,
                'Weight Schedule': self.weight_schedule, 'Weight Attempt': self.weight_attempt,
                'Weight Experience': self.weight_experience}

    def __repr__(self):
        return (
            f'Age(\
                Matriculation Number={self.matriculation_number}\
                Weight Age={self.weight_age}, \
                Weight Gender={self.weight_gender}, \
                Weight Bachelor/Master={self.weight_bachelor}\
                Weight Major/Minor={self.weight_major}\
                Weight Teammate={self.weight_teammate}\
                Weight Schedule={self.weight_schedule}\
                Weight Attempt={self.weight_attempt}\
                Weight Experience={self.weight_experience}\
            )'
        )


class Feedback(object):
    def __init__(self, satisfaction, outcome, experience, recommendation, fairness, visibility,
                 understanding, capability, diversity, email):
        self.satisfaction = satisfaction
        self.outcome = outcome
        self.experience = experience
        self.recommendation = recommendation
        self.fairness = fairness
        self.visibility = visibility
        self.understanding = understanding
        self.capability = capability
        self.diversity = diversity
        self.email = email

    @staticmethod
    def from_dict(source):
        if source:
            return Feedback(source['Matriculation Number'], source['satisfaction'], source['outcome'],
                            source['experience'], source['recommendation'], source['fairness'], source['visibility'],
                            source['understanding'], source['capability'], source['diversity'])
        else:
            return None

    def to_dict(self):
        return {'Email': self.email, 'satisfaction': self.satisfaction,
                'outcome': self.outcome, 'experience': self.experience, 'recommendation': self.recommendation,
                'fairness': self.fairness, 'visibility': self.visibility, 'understanding': self.understanding,
                'capability': self.capability, 'diversity': self.diversity}

    def __repr__(self):
        return (
            f'Feedback(\
                Email={self.email}\
                satisfaction={self.satisfaction}, \
                outcome={self.outcome}, \
                experience={self.experience}\
                recommendation={self.recommendation}\
                fairness={self.fairness}\
                visibility={self.visibility}\
                understanding={self.understanding}\
                capability={self.capability}\
                diversity={self.diversity}\
            )'
        )


class PeerReview(object):
    def __init__(self, name_teammate1, performance_teammate1, name_teammate2, performance_teammate2, name_teammate3,
                 performance_teammate3, name_teammate4, performance_teammate4, email):
        self.name_teammate1 = name_teammate1
        self.performance_teammate1 = performance_teammate1
        self.name_teammate2 = name_teammate2
        self.performance_teammate2 = performance_teammate2
        self.name_teammate3 = name_teammate3
        self.performance_teammate3 = performance_teammate3
        self.name_teammate4 = name_teammate4
        self.performance_teammate4 = performance_teammate4
        self.email = email

    @staticmethod
    def from_dict(source):
        if source:
            return PeerReview(source['Email'], source['Name Teammate 1'],
                              source['Performance Teammate 1'], source['Name Teammate 2'],
                              source['Performance Teammate 2'], source['Name Teammate 3'],
                              source['Performance Teammate 3'], source['Name Teammate 4'],
                              source['Performance Teammate 4'])
        else:
            return None

    def to_dict(self):
        return {'Email': self.email, 'Name Teammate 1': self.name_teammate1,
                'Performance Teammate 1': self.performance_teammate1, 'Name Teammate 2': self.name_teammate2,
                'Performance Teammate 2': self.performance_teammate2, 'Name Teammate 3': self.name_teammate3,
                'Performance Teammate 3': self.performance_teammate3, 'Name Teammate 4': self.name_teammate4,
                'Performance Teammate 4': self.performance_teammate4}

    def __repr__(self):
        return (
            f'Feedback(\
                Email={self.email}\
                Name Teammate 1={self.name_teammate1}, \
                Performance Teammate 1={self.performance_teammate1}, \
                Name Teammate 2={self.name_teammate2}\
                Performance Teammate 2={self.performance_teammate2}\
                Name Teammate 3={self.name_teammate3}\
                Performance Teammate 3={self.performance_teammate3}\
                Name Teammate 4={self.name_teammate4}\
                Performance Teammate 4={self.performance_teammate4}\
            )'
        )
