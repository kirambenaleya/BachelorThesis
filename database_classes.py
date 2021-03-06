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
                 understanding, capability, diversity, fulfillment, importance_fulfillment, recommendation_instead,
                 fairness_reason, visibility_reason, understanding_reason, capability_reason, diversity_reason,
                 overall_prototype, improvements, further_improvements):
        self.satisfaction = satisfaction
        self.outcome = outcome
        self.experience = experience
        self.recommendation = recommendation
        self.fairness = fairness
        self.visibility = visibility
        self.understanding = understanding
        self.capability = capability
        self.diversity = diversity
        self.fulfillment = fulfillment
        self.importance_fulfillment = importance_fulfillment
        self.recommendation_instead = recommendation_instead
        self.fairness_reason = fairness_reason
        self.visibility_reason = visibility_reason
        self.understanding_reason = understanding_reason
        self.capability_reason = capability_reason
        self.diversity_reason = diversity_reason
        self.overall_prototype = overall_prototype
        self.improvements = improvements
        self.further_improvements = further_improvements

    @staticmethod
    def from_dict(source):
        if source:
            return Feedback(source['satisfaction'], source['outcome'], source['experience'], source['recommendation'],
                            source['fairness'], source['visibility'],
                            source['understanding'], source['capability'], source['diversity'], source['fulfillment'],
                            source['importance_fulfillment'], source['recommendation_instead'],
                            source['fairness_reason'], source['visibility_reason'],
                            source['understanding_reason'], source['capability_reason'], source['diversity_reason'],
                            source['overall_prototype'],
                            source['improvements'], source['further_improvements'])
        else:
            return None

    def to_dict(self):
        return {'satisfaction': self.satisfaction,
                'outcome': self.outcome, 'experience': self.experience, 'recommendation': self.recommendation,
                'fairness': self.fairness, 'visibility': self.visibility, 'understanding': self.understanding,
                'capability': self.capability, 'diversity': self.diversity, 'fulfillment': self.fulfillment, 'importance_fulfillment': self.importance_fulfillment,
                'recommendation_instead': self.recommendation_instead, 'fairness_reason': self.fairness_reason, 'visibility_reason': self.visibility_reason,
                'understanding_reason': self.understanding_reason, 'capability_reason': self.capability_reason, 'diversity_reason': self.diversity_reason,
                'overall_prototype': self.overall_prototype, 'improvements': self.improvements, 'further_improvements': self.further_improvements}

    def __repr__(self):
        return (
            f'Feedback(\
                satisfaction={self.satisfaction}, \
                outcome={self.outcome}, \
                experience={self.experience}\
                recommendation={self.recommendation}\
                fairness={self.fairness}\
                visibility={self.visibility}\
                understanding={self.understanding}\
                capability={self.capability}\
                diversity={self.diversity}\
                fulfillment={self.fulfillment}\
                importance_fulfillment={self.importance_fulfillment}\
                recommendation_instead={self.recommendation_instead}\
                fairness_reason={self.fairness_reason}\
                visibility_reason={self.visibility_reason}\
                understanding_reason={self.understanding_reason}\
                capability_reason={self.capability_reason}\
                diversity_reason={self.diversity_reason}\
                overall_prototype={self.overall_prototype}\
                improvements={self.improvements}\
                further_improvements={self.further_improvements}\
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


class InitialFeedback(object):
    def __init__(self, satisfaction, outcome, reassignment, experience, recommendation, fairness, visibility,
                 understanding, capability, diversity, mental, simplicity, delight, surprise, frustration, lack,
                 design, pref_teammate, assignment, importance, impact, diversity_score, influence, influence_grade,
                 performance, belief, email):
        self.satisfaction = satisfaction
        self.outcome = outcome
        self.reassignment = reassignment
        self.experience = experience
        self.recommendation = recommendation
        self.fairness = fairness
        self.visibility = visibility
        self.understanding = understanding
        self.capability = capability
        self.diversity = diversity
        self.mental = mental
        self.simplicity = simplicity
        self.delight = delight
        self.surprise = surprise
        self.frustration = frustration
        self.lack = lack
        self.design = design
        self.pref_teammate = pref_teammate
        self.assignment = assignment
        self.importance = importance
        self.impact = impact
        self.diversity_score = diversity_score
        self.influence = influence
        self.influence_grade = influence_grade
        self.performance = performance
        self.belief = belief
        self.email = email

    @staticmethod
    def from_dict(source):
        if source:
            return InitialFeedback(source['Matriculation Number'], source['satisfaction'], source['outcome'],
                                   source['reassignment'], source['experience'], source['recommendation'],
                                   source['fairness'], source['visibility'], source['understanding'],
                                   source['capability'], source['diversity'], source['mental'], source['simplicity'],
                                   source['delight'], source['surprise'], source['frustration'], source['lack'],
                                   source['design'], source['pref_teammate'], source['assignment'],
                                   source['importance'], source['impact'], source['diversity_score'],
                                   source['influence'], source['influence_grade'], source['performance'],
                                   source['belief'])
        else:
            return None

    def to_dict(self):
        return {'Email': self.email, 'satisfaction': self.satisfaction, 'reassignment': self.reassignment,
                'outcome': self.outcome, 'experience': self.experience, 'recommendation': self.recommendation,
                'fairness': self.fairness, 'visibility': self.visibility, 'understanding': self.understanding,
                'capability': self.capability, 'diversity': self.diversity, 'mental': self.mental,
                'simplicity': self.simplicity, 'delight': self.delight, 'surprise': self.surprise,
                'frustration': self.frustration, 'lack': self.lack, 'design': self.design,
                'pref_teammate': self.pref_teammate, 'assignment': self.assignment, 'importance': self.importance,
                'impact': self.impact, 'diversity_score': self.diversity_score, 'influence': self.influence,
                'influence_grade': self.influence_grade, 'performance': self.performance, 'belief': self.belief}

    def __repr__(self):
        return (
            f'Feedback(\
                Email={self.email}\
                satisfaction={self.satisfaction}, \
                reassignment={self.reassignment}, \
                outcome={self.outcome}, \
                experience={self.experience}\
                recommendation={self.recommendation}\
                fairness={self.fairness}\
                visibility={self.visibility}\
                understanding={self.understanding}\
                capability={self.capability}\
                diversity={self.diversity}\
                mental={self.mental}\
                delight={self.delight}\
                surprise={self.surprise}\
                frustration={self.frustration}\
                lack={self.lack}\
                design={self.design}\
                pref_teammate={self.pref_teammate}\
                assignment={self.assignment}\
                importance={self.importance}\
                impact={self.impact}\
                diversity_score={self.diversity_score}\
                influence={self.influence}\
                influence_grade={self.influence_grade}\
                performance={self.performance}\
                belief={self.belief}\
            )'
        )


class Demographics(object):
    def __init__(self, orientation, wake_up, nationality, leader, effort, english,
                 german):
        self.orientation = orientation
        self.wake_up = wake_up
        self.nationality = nationality
        self.leader = leader
        self.effort = effort
        self.english = english
        self.german = german

    @staticmethod
    def from_dict(source):
        if source:
            return Demographics(source['Orientation'], source['Wake Up'], source['Nationality'], source['Leader'],
                                source['Effort'], source['English'], source['German'])
        else:
            return None

    def to_dict(self):
        return {'Orientation': self.orientation, 'Wake Up': self.wake_up,
                'Nationality': self.nationality, 'Leader': self.leader, 'Effort': self.effort,
                'English': self.english, 'German': self.german}

    def __repr__(self):
        return (
            f'Feedback(\
                Orientation={self.orientation}\
                Wake Up={self.wake_up}, \
                Nationality={self.nationality}, \
                Leader={self.leader}\
                Effort={self.effort}\
                English={self.english}\
                German={self.german}\
            )'
        )
