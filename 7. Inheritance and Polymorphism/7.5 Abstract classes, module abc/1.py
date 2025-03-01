from abc import ABC, abstractmethod
from statistics import harmonic_mean, median_grouped, median_high


class Middle(ABC):
    def __init__(self, user_votes, expert_votes):  
        self.uv, self.ev = user_votes, expert_votes      

    def get_correct_user_votes(self, to_sort=False):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.uv if 10 < vote < 90]
        return sorted(votes) if to_sort else votes

    def get_correct_expert_votes(self, to_sort=False):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.ev if 5 < vote < 95]
        return sorted(votes) if to_sort else votes

    @abstractmethod
    def get_average(self, users=True, to_sort=False):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes(to_sort)
        else:
            votes = self.get_correct_expert_votes(to_sort)
        return votes


class Average(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return sum(votes) / len(votes)


class Median(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return median_high(votes)


class Harmonic(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return harmonic_mean(votes)



print(issubclass(Average, Middle))
print(issubclass(Median, Middle))
print(issubclass(Harmonic, Middle))