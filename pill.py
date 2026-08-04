class PillManager:


    def __init__(self):

        pass




    def calculate_days(
        self,
        total_count,
        daily_count
    ):

        """
        남은 복용 가능 일수 계산

        total_count:
            현재 약 개수

        daily_count:
            하루 복용 개수
        """



        if daily_count <= 0:

            return 0



        return total_count / daily_count





    def format_days(
        self,
        days
    ):

        """
        UI 표시용 문자열 변환
        """

        return f"{days:.1f} 일"