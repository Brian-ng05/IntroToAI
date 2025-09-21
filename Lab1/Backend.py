from enum import Enum

# Cứ hiểu Enum là một dạng list mà đều OOP đi.
# Lý do vì sao tụi mình nên chọn xài Enum: Cho ngầu B).

class GenderComments(Enum):
    Male= "Male"
    Female= "Female"

class OccasionComments(Enum):
    Date= "Date"
    Wedding= "Wedding"
    FamilyMeeting= "FamilyMeeting"
    Holiday= "Holiday"
    School= "School"
    Other= "Other"

class ColorComments(Enum):
    Black= "Black"
    White= "White"
    Blue= "Blue"
    Red= "Red"
    Green= "Green"
    Yellow= "Yellow"

def GetCommentsFromFakeAI(input: list[str]) -> str:
    GENDER_INPUT = input[0]
    OCCASION_INPUT = input[1]
    COLOR_INPUT = input[2]
    res = ""

    def GetCommentForInput(input: str, comments: Enum):
        try:
            for item in (comments):
                input_matches: bool = (item.name == input)

                if input_matches:
                    comment: str = item.value + " "
                    
                    return comment
        except Exception as e:
            print(e)
        
     
    res += GetCommentForInput(input= GENDER_INPUT, comments= GenderComments)
    res += GetCommentForInput(input= OCCASION_INPUT, comments= OccasionComments)
    res += GetCommentForInput(input= COLOR_INPUT, comments= ColorComments)               
        
    return res